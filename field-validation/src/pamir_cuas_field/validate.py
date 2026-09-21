from collections import defaultdict

EXPECTED = {"CW_RADAR", "FMCW_RADAR", "RF_RECEIVER"}


def validate_inventory(records):
    groups = defaultdict(set)
    hashes_ok = True
    for r in records:
        groups[(r["target"], r["distance_m"], r["sample_index"])].add(r["sensor"])
        hashes_ok &= len(r.get("sha256", "")) == 64
    complete = [k for k,v in groups.items() if EXPECTED <= v]
    incomplete = [{"key": k, "missing": sorted(EXPECTED-v)} for k,v in groups.items() if not EXPECTED <= v]
    return {
        "source_hashes_present": bool(records) and hashes_ok,
        "aligned_complete_sets": len(complete),
        "incomplete_sets": incomplete,
        "ready_for_cfv01": bool(complete) and hashes_ok,
    }
