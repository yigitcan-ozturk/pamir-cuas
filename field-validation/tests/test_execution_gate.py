from pamir_cuas_field.validate import validate_inventory

def test_source_gate_fails_closed_without_payload():
 r=validate_inventory([])
 assert r["ready_for_cfv01"] is False
 assert r["source_hashes_present"] is False
