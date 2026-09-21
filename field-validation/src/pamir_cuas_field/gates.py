def institutional_gate(cases:list[dict])->dict:
    required={f"C-FV0{i}" for i in range(1,8)}
    by_id={c.get("case_id"):c for c in cases}
    missing=sorted(required-set(by_id))
    unreproduced=sorted(i for i,c in by_id.items() if i in required and c.get("reproduction_status") not in ("PASS","REPRODUCED"))
    insufficient=sorted(i for i,c in by_id.items() if i in required and c.get("evidence_sufficiency") in ("INSUFFICIENT_EVIDENCE","UNKNOWN"))
    ready=not missing and not unreproduced and not insufficient
    return {"institutional_evidence_pack_ready":ready,"missing_cases":missing,"unreproduced_cases":unreproduced,"insufficient_cases":insufficient}
