from .model import Observation, ObservationSet


def drop_sensor(frame: ObservationSet, sensor: str) -> ObservationSet:
    return ObservationSet(frame.sample_index, tuple(o for o in frame.observations if o.sensor != sensor))


def delay_sensor(frame: ObservationSet, sensor: str, delay_s: float) -> ObservationSet:
    if delay_s < 0:
        raise ValueError("delay_s must be non-negative")
    out = []
    for o in frame.observations:
        if o.sensor == sensor:
            base = 0.0 if o.timestamp_s is None else o.timestamp_s
            out.append(Observation(o.sensor, o.sample_index, o.value, o.source_file, base + delay_s, {**o.metadata, "controlled_delay_s": delay_s}))
        else:
            out.append(o)
    return ObservationSet(frame.sample_index, tuple(out))
