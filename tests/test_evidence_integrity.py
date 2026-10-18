import tempfile
import unittest
from pathlib import Path
from tools.evidence_integrity import create_manifest, verify_manifest, safe_path

class EvidenceIntegrityTests(unittest.TestCase):
    def test_valid_manifest(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "sample.bin").write_bytes(b"radar-test")
            manifest = create_manifest(root)
            self.assertEqual(verify_manifest(root, manifest)["status"], "PASS")

    def test_tamper_detected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            path = root / "sample.bin"
            path.write_bytes(b"original")
            manifest = create_manifest(root)
            path.write_bytes(b"changed!")
            self.assertEqual(verify_manifest(root, manifest)["status"], "FAIL")

    def test_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                safe_path(Path(d), "../outside")

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            path = root / "file.bin"
            path.write_bytes(b"x")
            manifest = create_manifest(root)
            path.unlink()
            self.assertEqual(verify_manifest(root, manifest)["status"], "FAIL")

    def test_deterministic_manifest(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "a.txt").write_text("a")
            self.assertEqual(create_manifest(root), create_manifest(root))

if __name__ == "__main__":
    unittest.main()
