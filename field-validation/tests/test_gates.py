from pamir_cuas_field.gates import institutional_gate

def test_gate_rejects_empty_pack():
 r=institutional_gate([])
 assert not r["institutional_evidence_pack_ready"] and len(r["missing_cases"])==7

def test_gate_accepts_complete_reproduced_pack():
 cases=[{"case_id":f"C-FV0{i}","reproduction_status":"REPRODUCED","evidence_sufficiency":"SUFFICIENT"} for i in range(1,8)]
 assert institutional_gate(cases)["institutional_evidence_pack_ready"]
