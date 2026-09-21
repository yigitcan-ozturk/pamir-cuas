from .model import Observation, ObservationSet


def offset_index(frame: ObservationSet, sensor: str, offset: int) -> ObservationSet:
    if offset == 0: return frame
    out=[]
    for o in frame.observations:
        if o.sensor == sensor:
            out.append(Observation(o.sensor,o.sample_index+offset,o.value,o.source_file,o.timestamp_s,{**o.metadata,"controlled_index_offset":offset}))
        else: out.append(o)
    return ObservationSet(frame.sample_index,tuple(out))


def synchronization_state(frame: ObservationSet) -> dict:
    indices={o.sensor:o.sample_index for o in frame.observations}
    vals=set(indices.values())
    return {"indices":indices,"aligned":len(vals)<=1,"spread_index":(max(vals)-min(vals)) if vals else None}
