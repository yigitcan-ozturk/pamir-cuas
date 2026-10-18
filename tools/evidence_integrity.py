#!/usr/bin/env python3
"""PAMIR-CUAS evidence manifest verifier. Standard library only."""
import argparse
import hashlib
import json
from pathlib import Path

SCHEMA = "pamir-cuas-integrity-v1"

def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def safe_path(root, name):
    if not isinstance(name, str) or not name or "\\\\" in name:
        raise ValueError("invalid relative path")
    rel = Path(name)
    if rel.is_absolute() or ".." in rel.parts or rel.as_posix() != name:
        raise ValueError("unsafe relative path")
    resolved = (root / rel).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError("path escapes root")
    return resolved

def create_manifest(root):
    root = root.resolve()
    entries = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError("symlinks not supported")
        if path.is_file():
            entries.append({"path": path.relative_to(root).as_posix(),
                            "size_bytes": path.stat().st_size,
                            "sha256": sha256_file(path)})
    return {"schema": SCHEMA, "files": entries}

def verify_manifest(root, manifest):
    failures = []
    if not isinstance(manifest, dict) or manifest.get("schema") != SCHEMA or not isinstance(manifest.get("files"), list):
        return {"status": "FAIL", "failures": ["invalid manifest schema"]}
    seen = set()
    for entry in manifest["files"]:
        try:
            name = entry["path"]
            if name in seen:
                raise ValueError("duplicate path")
            seen.add(name)
            path = safe_path(root, name)
            if not path.is_file() or path.is_symlink():
                raise ValueError("file missing or symlink")
            if not isinstance(entry["size_bytes"], int) or isinstance(entry["size_bytes"], bool) or entry["size_bytes"] < 0:
                raise ValueError("invalid size")
            if path.stat().st_size != entry["size_bytes"]:
                raise ValueError("size mismatch")
            digest = entry["sha256"]
            if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
                raise ValueError("invalid digest")
            if sha256_file(path) != digest:
                raise ValueError("sha256 mismatch")
        except (KeyError, TypeError, ValueError, OSError) as exc:
            failures.append({"path": entry.get("path", "?") if isinstance(entry, dict) else "?", "reason": str(exc)})
    return {"status": "FAIL" if failures else "PASS", "checked": len(manifest["files"]), "failures": failures}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["create", "verify"])
    parser.add_argument("root", type=Path)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error("root must be a directory")
    if args.mode == "create":
        # Manifest must be stored outside root to avoid self-inclusion.
        if args.manifest.resolve().is_relative_to(args.root.resolve()):
            parser.error("manifest output must be outside root")
        args.manifest.write_text(json.dumps(create_manifest(args.root), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        result = verify_manifest(args.root, json.loads(args.manifest.read_text(encoding="utf-8")))
        print(json.dumps(result, sort_keys=True))
        if result["status"] != "PASS":
            raise SystemExit(1)

if __name__ == "__main__":
    main()
