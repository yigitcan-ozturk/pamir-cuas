"""Reference-backed validation of detection misses and association lineage.

These functions audit supplied evidence; they do not infer ground truth.
"""
from math import isfinite


def _time(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value):
        raise ValueError("timestamps must be finite numbers")
    return float(value)


def missed_detections(reference_times, detection_times, tolerance_s):
    """Match detections one-to-one to references within a frozen time tolerance.

    Returns unmatched reference indices. This is a temporal coverage check only:
    spatial/identity matching must be validated separately.
    """
    tolerance = _time(tolerance_s)
    if tolerance < 0:
        raise ValueError("negative tolerance")
    if reference_times is None or detection_times is None:
        raise ValueError("independent reference and detections are required")
    refs = [_time(t) for t in reference_times]
    dets = [_time(t) for t in detection_times]
    if refs != sorted(refs) or dets != sorted(dets):
        raise ValueError("timestamps must be sorted")
    candidates = sorted(
        (abs(r - d), i, j)
        for i, r in enumerate(refs)
        for j, d in enumerate(dets)
        if abs(r - d) <= tolerance
    )
    used_refs, used_dets = set(), set()
    for _, i, j in candidates:
        if i not in used_refs and j not in used_dets:
            used_refs.add(i)
            used_dets.add(j)
    return {"reference_count": len(refs), "matched_count": len(used_refs),
            "unmatched_reference_indices": [i for i in range(len(refs)) if i not in used_refs],
            "evaluation": "TEMPORAL_ONLY_NOT_FULL_MISSED_DETECTION"}


def association_divergence(expected, observed):
    """Compare ordered (timestamp, track_id, observation_id) lineage records.

    Missing independent expected lineage is a hard error, not a PASS.
    """
    if expected is None or observed is None:
        raise ValueError("expected and observed lineage are required")
    if not isinstance(expected, list) or not isinstance(observed, list):
        raise ValueError("lineages must be lists")
    for records in (expected, observed):
        for rec in records:
            if not isinstance(rec, (list, tuple)) or len(rec) != 3:
                raise ValueError("each lineage record must have three fields")
            _time(rec[0])
    for i in range(max(len(expected), len(observed))):
        left = expected[i] if i < len(expected) else None
        right = observed[i] if i < len(observed) else None
        if left != right:
            return {"status": "DIVERGENCE", "first_index": i,
                    "expected": left, "observed": right}
    return {"status": "AGREEMENT", "first_index": None}
