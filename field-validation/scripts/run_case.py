#!/usr/bin/env python3
"""Fail-closed execution entry point for PAMIR-CUAS field-validation cases."""
import argparse,json
from pathlib import Path
from pamir_cuas_field.validate import validate_inventory

CASES={f"C-FV0{i}" for i in range(1,8)}

def main():
 p=argparse.ArgumentParser(); p.add_argument("case_id",choices=sorted(CASES)); p.add_argument("manifest"); p.add_argument("--output",default="run_gate.json"); a=p.parse_args()
 manifest=json.loads(Path(a.manifest).read_text(encoding="utf-8"))
 check=validate_inventory(manifest.get("files",[]))
 result={"case_id":a.case_id,"source_gate":check,"execution_status":"READY" if check["ready_for_cfv01"] else "BLOCKED_SOURCE_INTEGRITY"}
 Path(a.output).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(result,indent=2))
 raise SystemExit(0 if result["execution_status"]=="READY" else 2)
if __name__=="__main__": main()
