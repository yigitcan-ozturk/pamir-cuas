"""Strict CSV/JSON adapter for pre-labeled PAMIR-CUAS 2D validation records.

Only reads existing local files; does not infer coordinate frames or truth.
"""
import csv
import json
from pathlib import Path

FIELDS = ("time_s", "x_m", "y_m", "target_id")


def _unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def load_records(path, *, max_records=100000):
    path = Path(path)
    if path.suffix.lower() == ".json":
        with path.open("r", encoding="utf-8") as handle:
            raw = json.load(handle, object_pairs_hook=_unique_pairs)
    elif path.suffix.lower() == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)):
                raise ValueError("missing or duplicate CSV headers")
            if set(reader.fieldnames) != set(FIELDS):
                raise ValueError("CSV schema must contain exactly required fields")
            raw = []
            for row in reader:
                if len(raw) >= max_records:
                    raise ValueError("record limit exceeded")
                if None in row:
                    raise ValueError("extra CSV columns")
                raw.append(row)
    else:
        raise ValueError("only .json and .csv supported")
    if not isinstance(raw, list) or len(raw) > max_records:
        raise ValueError("expected bounded array of records")
    records = []
    for index, item in enumerate(raw):
        if not isinstance(item, dict) or set(item) != set(FIELDS):
            raise ValueError(f"record {index}: unexpected or missing fields")
        if any(isinstance(item[key], bool) or item[key] is None for key in FIELDS[:3]):
            raise ValueError(f"record {index}: invalid numeric type")
        try:
            row = {
                "time_s": float(item["time_s"]),
                "x_m": float(item["x_m"]),
                "y_m": float(item["y_m"]),
                "target_id": item["target_id"],
            }
        except (ValueError, TypeError, OverflowError) as exc:
            raise ValueError(f"record {index}: invalid numeric value") from exc
        from tools.spatial_validation import _record
        _record(row)
        records.append(row)
    if any(records[i]["time_s"] > records[i + 1]["time_s"] for i in range(len(records) - 1)):
        raise ValueError("records not sorted by time")
    return records
