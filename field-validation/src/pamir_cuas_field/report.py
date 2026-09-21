import json
from pathlib import Path

def case_summary(evidence:dict)->dict:
    suff=evidence.get("evidence_sufficiency",{})
    return {
      "case_id":evidence.get("case_id"),
      "evidence_origin":evidence.get("evidence_origin"),
      "evidence_sufficiency":suff.get("status",suff if isinstance(suff,str) else "UNKNOWN"),
      "first_divergence":evidence.get("first_divergence"),
      "causal_reconstruction":evidence.get("causal_reconstruction"),
      "reproduction_status":evidence.get("reproducibility",{}).get("reproduction_status","NOT_RUN")
    }

def write_case_summary(evidence,path):
    Path(path).write_text(json.dumps(case_summary(evidence),indent=2,sort_keys=True)+"\n",encoding="utf-8")
