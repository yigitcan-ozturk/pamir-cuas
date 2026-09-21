REQUIRED_REPRO_FIELDS={"source_sha256","code_commit","parameters","output_sha256"}

def assess_evidence(*, observations:int, modalities:int, source_hashes:bool, temporal_status:str, reproducibility:dict)->dict:
    missing=[]
    if observations<=0: missing.append("observations")
    if modalities<=0: missing.append("modalities")
    if not source_hashes: missing.append("source_sha256")
    if temporal_status in ("UNKNOWN","INSUFFICIENT_EVIDENCE"): missing.append("temporal_integrity")
    missing_repro=sorted(k for k in REQUIRED_REPRO_FIELDS if not reproducibility.get(k))
    if missing_repro: missing.extend("reproducibility."+k for k in missing_repro)
    if not observations or not modalities: status="INSUFFICIENT_EVIDENCE"
    elif missing: status="PARTIALLY_SUPPORTED"
    else: status="SUFFICIENT"
    return {"status":status,"missing":missing}
