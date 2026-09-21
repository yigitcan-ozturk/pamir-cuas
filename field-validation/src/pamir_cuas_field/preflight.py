from .acquisition import select_minimal_triplet,provenance_complete

def preflight_cfv01(records:list[dict])->dict:
    triplet=select_minimal_triplet(records)
    if not triplet:
        return {"ready":False,"reason":"NO_INDEX_ALIGNED_THREE_SENSOR_TRIPLET"}
    incomplete=[r.get("source_file") for r in triplet if not provenance_complete(r)]
    if incomplete:
        return {"ready":False,"reason":"INCOMPLETE_PROVENANCE","files":incomplete}
    return {"ready":True,"reason":"SOURCE_GATE_PASSED","selection":triplet}
