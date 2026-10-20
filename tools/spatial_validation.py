"""Conservative reference-backed spatial and temporal evidence matching.

Coordinates must be in a common metric frame. No coordinate conversion is implied.
"""
from math import hypot, isfinite


def _record(value):
    if not isinstance(value, dict):
        raise ValueError("record must be an object")
    required = ("time_s", "x_m", "y_m", "target_id")
    if any(key not in value for key in required):
        raise ValueError("missing required field")
    for key in required[:3]:
        number = value[key]
        if isinstance(number, bool) or not isinstance(number, (int, float)) or not isfinite(number):
            raise ValueError("non-finite or invalid measurement")
    if not isinstance(value["target_id"], str) or not value["target_id"].strip():
        raise ValueError("missing target identity")
    return value


def match_reference_tracks(references, detections, time_tolerance_s, distance_tolerance_m):
    """One-to-one maximum-cardinality matches gated by time, XY and target identity.

    This is an audit of pre-labeled reference and detection records, not a tracker.
    Thresholds must be fixed before running an acceptance test.
    """
    for value in (time_tolerance_s, distance_tolerance_m):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value) or value < 0:
            raise ValueError("invalid acceptance tolerance")
    if references is None or detections is None:
        raise ValueError("independent references and detections are required")
    refs = [_record(r) for r in references]
    dets = [_record(d) for d in detections]
    if any(refs[i]["time_s"] > refs[i + 1]["time_s"] for i in range(len(refs) - 1)):
        raise ValueError("reference times not ordered")
    if any(dets[i]["time_s"] > dets[i + 1]["time_s"] for i in range(len(dets) - 1)):
        raise ValueError("detection times not ordered")

    neighbors = []
    for ref in refs:
        candidates = []
        for j, det in enumerate(dets):
            dt = abs(ref["time_s"] - det["time_s"])
            dist = hypot(ref["x_m"] - det["x_m"], ref["y_m"] - det["y_m"])
            if (dt <= time_tolerance_s and dist <= distance_tolerance_m
                    and ref["target_id"] == det["target_id"]):
                candidates.append((dt, dist, j))
        neighbors.append([j for _, _, j in sorted(candidates)])

    owner = {}

    def augment(i, visited):
        for j in neighbors[i]:
            if j in visited:
                continue
            visited.add(j)
            if j not in owner or augment(owner[j], visited):
                owner[j] = i
                return True
        return False

    for i in range(len(refs)):
        augment(i, set())
    matched_refs = set(owner.values())
    return {
        "status": "MATCHED_WITH_REFERENCE" if refs else "NO_REFERENCE_EVENTS",
        "reference_count": len(refs),
        "detection_count": len(dets),
        "matched_count": len(matched_refs),
        "unmatched_reference_indices": [i for i in range(len(refs)) if i not in matched_refs],
        "unmatched_detection_indices": [j for j in range(len(dets)) if j not in owner],
        "scope": "LABELED_2D_METRIC_COORDINATES_ONLY",
    }
