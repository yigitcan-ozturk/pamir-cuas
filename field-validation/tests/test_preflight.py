from pamir_cuas_field.preflight import preflight_cfv01

def rec(sensor,idx=1):
 return {"sensor":sensor,"target":"T","distance_m":2,"sample_index":idx,"source_file":sensor+".mat","sha256":"a"*64}

def test_preflight_accepts_aligned_triplet():
 r=preflight_cfv01([rec("CW_RADAR"),rec("FMCW_RADAR"),rec("RF_RECEIVER")])
 assert r["ready"]

def test_preflight_rejects_misaligned_triplet():
 r=preflight_cfv01([rec("CW_RADAR",1),rec("FMCW_RADAR",1),rec("RF_RECEIVER",2)])
 assert not r["ready"]
