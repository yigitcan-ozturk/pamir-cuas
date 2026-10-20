import json
import tempfile
import unittest
from pathlib import Path
from tools.record_adapter import load_records


class RecordAdapterTests(unittest.TestCase):
    def test_json_valid(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "sample.json"
            p.write_text(json.dumps([{"time_s": 1, "x_m": 2, "y_m": 3, "target_id": "A"}]))
            self.assertEqual(load_records(p)[0]["target_id"], "A")

    def test_csv_valid(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "sample.csv"
            p.write_text("time_s,x_m,y_m,target_id\n1,2,3,A\n")
            self.assertEqual(load_records(p)[0]["x_m"], 2)

    def test_duplicate_json_key(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "sample.json"
            p.write_text('[{"time_s":1,"time_s":2,"x_m":2,"y_m":3,"target_id":"A"}]')
            with self.assertRaises(ValueError):
                load_records(p)

    def test_missing_field(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "sample.json"
            p.write_text('[{"time_s":1,"x_m":2,"y_m":3}]')
            with self.assertRaises(ValueError):
                load_records(p)

    def test_nan_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "sample.csv"
            p.write_text("time_s,x_m,y_m,target_id\nnan,2,3,A\n")
            with self.assertRaises(ValueError):
                load_records(p)

    def test_unsorted_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "sample.csv"
            p.write_text("time_s,x_m,y_m,target_id\n2,2,3,A\n1,2,3,A\n")
            with self.assertRaises(ValueError):
                load_records(p)


if __name__ == "__main__":
    unittest.main()
