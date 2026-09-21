from pamir_cuas_field.cfv01 import evaluate_nominal_agreement
from pamir_cuas_field.model import Observation, ObservationSet
from pamir_cuas_field.perturbations import drop_sensor, delay_sensor


def frame():
    return ObservationSet(1, tuple(Observation(s, 1, 1.0, "fixture", 1.0) for s in ("FMCW_RADAR","CW_RADAR","RF_RECEIVER")))


def test_cfv01_requires_three_modalities():
    assert evaluate_nominal_agreement(frame())["evidence_sufficiency"] == "SUFFICIENT"


def test_dropout_is_explicit():
    changed = drop_sensor(frame(), "RF_RECEIVER")
    result = evaluate_nominal_agreement(changed)
    assert result["missing_sensors"] == ["RF_RECEIVER"]


def test_delay_marks_controlled_metadata():
    changed = delay_sensor(frame(), "RF_RECEIVER", 0.25)
    rf = next(o for o in changed.observations if o.sensor == "RF_RECEIVER")
    assert rf.timestamp_s == 1.25
    assert rf.metadata["controlled_delay_s"] == 0.25
