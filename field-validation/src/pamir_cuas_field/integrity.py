import hashlib
from pathlib import Path


def sha256_file(path: str | Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def temporal_integrity(sample_indices: list[int]) -> dict:
    if not sample_indices:
        return {"status": "UNKNOWN", "reason": "NO_OBSERVATIONS"}
    ordered = all(b > a for a, b in zip(sample_indices, sample_indices[1:]))
    unique = len(sample_indices) == len(set(sample_indices))
    return {
        "status": "SUFFICIENT" if ordered and unique else "INSUFFICIENT_EVIDENCE",
        "strictly_increasing": ordered,
        "unique_indices": unique,
    }
