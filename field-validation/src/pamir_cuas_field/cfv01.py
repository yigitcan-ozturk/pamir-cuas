from .model import ObservationSet

EXPECTED_SENSORS = {"FMCW_RADAR", "CW_RADAR", "RF_RECEIVER"}


def evaluate_nominal_agreement(frame: ObservationSet) -> dict:
    present = set(frame.sensors)
    missing = sorted(EXPECTED_SENSORS - present)
    return {
        "case_id": "C-FV01",
        "evidence_origin": "REAL_MEASUREMENT",
        "sample_index": frame.sample_index,
        "sensor_availability": sorted(present),
        "missing_sensors": missing,
        "evidence_sufficiency": "SUFFICIENT" if not missing else "PARTIALLY_SUPPORTED",
        "status": "READY_FOR_MEASUREMENT_THRESHOLDS" if not missing else "INCOMPLETE_SENSOR_SET",
    }
