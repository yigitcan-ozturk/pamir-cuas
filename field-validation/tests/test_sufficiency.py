from pamir_cuas_field.sufficiency import assess_evidence

def test_empty_evidence_is_insufficient():
 r=assess_evidence(observations=0,modalities=0,source_hashes=False,temporal_status="UNKNOWN",reproducibility={})
 assert r["status"]=="INSUFFICIENT_EVIDENCE"

def test_complete_evidence_is_sufficient():
 r=assess_evidence(observations=3,modalities=3,source_hashes=True,temporal_status="SUFFICIENT",reproducibility={"source_sha256":"x","code_commit":"x","parameters":{},"output_sha256":"x"})
 assert r["status"]=="SUFFICIENT"
