from .sufficiency import assess_evidence

def finalize_case(evidence:dict)->dict:
    obs=evidence.get("observations",[])
    modalities=len({o.get("sensor") for o in obs if o.get("sensor")})
    source_hashes=all(bool(o.get("source_sha256")) for o in obs) if obs else False
    temporal=evidence.get("timestamp_integrity",{}).get("status","UNKNOWN")
    repro=evidence.get("reproducibility",{})
    evidence["evidence_sufficiency"]=assess_evidence(observations=len(obs),modalities=modalities,source_hashes=source_hashes,temporal_status=temporal,reproducibility=repro)
    return evidence
