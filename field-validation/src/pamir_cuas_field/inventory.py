import json
from pathlib import Path
from .integrity import sha256_file
from .tsms import parse_source_file

SENSORS = ("CW_RADAR", "FMCW_RADAR", "RF_RECEIVER")


def inventory_file(path, sensor, target, distance_m):
    r = parse_source_file(path, sensor, target, distance_m)
    return {
        "sensor": r.sensor,
        "target": r.target,
        "distance_m": r.distance_m,
        "sample_index": r.sample_index,
        "source_file": r.path,
        "representation": r.representation,
        "sha256": sha256_file(path),
    }


def write_manifest(records, output):
    payload = {
        "dataset_id": "TSMS-Drone",
        "hash_algorithm": "SHA-256",
        "immutability_policy": "SOURCE_FILES_READ_ONLY",
        "files": sorted(records, key=lambda x: (x["target"], x["distance_m"], x["sample_index"], x["sensor"])),
    }
    Path(output).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload
