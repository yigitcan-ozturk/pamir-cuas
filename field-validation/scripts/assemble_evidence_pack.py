#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from pamir_cuas_field.gates import institutional_gate

def main():
 p=argparse.ArgumentParser(); p.add_argument("summaries",nargs="+"); p.add_argument("--output",default="evidence_pack_index.json"); a=p.parse_args()
 cases=[json.loads(Path(x).read_text(encoding="utf-8")) for x in a.summaries]
 gate=institutional_gate(cases)
 out={"programme":"PAMIR-CUAS Real-World Field Validation Programme","cases":cases,"gate":gate}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print(json.dumps(gate,indent=2))
 raise SystemExit(0 if gate["institutional_evidence_pack_ready"] else 3)
if __name__=="__main__": main()
