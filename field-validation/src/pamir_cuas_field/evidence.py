from typing import Any


def build_evidence_object(*, case_id: str, source: dict[str, Any], origin: str, timestamp_integrity: dict[str, Any], observations: list[dict[str, Any]], sufficiency: str, reproducibility: dict[str, Any], perturbation=None, **derived):
    obj = {
        "case_id": case_id,
        "source": source,
        "evidence_origin": origin,
        "perturbation": perturbation,
        "timestamp_integrity": timestamp_integrity,
        "observations": observations,
        "evidence_sufficiency": sufficiency,
        "reproducibility": reproducibility,
    }
    obj.update(derived)
    return obj
