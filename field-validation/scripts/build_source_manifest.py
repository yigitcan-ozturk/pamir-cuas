#!/usr/bin/env python3
"""Build immutable TSMS-Drone source inventory after local acquisition.

This script never modifies source files. Populate RECORDS from acquired files or
wrap this module in an environment-specific discovery script.
"""
import argparse, json
from pamir_cuas_field.inventory import inventory_file, write_manifest
from pamir_cuas_field.validate import validate_inventory


def main():
    p=argparse.ArgumentParser()
    p.add_argument("records_json", help="JSON array: path,sensor,target,distance_m")
    p.add_argument("--output", default="source_manifest.json")
    a=p.parse_args()
    specs=json.load(open(a.records_json, encoding="utf-8"))
    records=[inventory_file(**x) for x in specs]
    manifest=write_manifest(records,a.output)
    print(json.dumps(validate_inventory(manifest["files"]), indent=2))

if __name__=="__main__": main()
