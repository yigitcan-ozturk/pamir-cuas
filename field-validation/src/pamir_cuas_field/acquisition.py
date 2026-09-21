"""Selection and provenance helpers for source acquisition."""
from collections import defaultdict

def select_minimal_triplet(records:list[dict], *, target:str|None=None, distance_m:int|None=None)->list[dict]:
    groups=defaultdict(dict)
    for r in records:
        if target is not None and r.get("target")!=target: continue
        if distance_m is not None and r.get("distance_m")!=distance_m: continue
        key=(r.get("target"),r.get("distance_m"),r.get("sample_index"))
        groups[key][r.get("sensor")]=r
    expected={"CW_RADAR","FMCW_RADAR","RF_RECEIVER"}
    for key in sorted(groups, key=lambda x:(str(x[0]),x[1] or -1,x[2] or -1)):
        if expected <= set(groups[key]):
            return [groups[key][s] for s in sorted(expected)]
    return []

def provenance_complete(record:dict)->bool:
    return all(record.get(k) not in (None,"") for k in ("source_file","sha256","sensor","target","distance_m","sample_index"))
