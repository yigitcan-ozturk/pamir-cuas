def confidence_state(sensor_scores: dict[str,float], minimum_modalities: int=2) -> dict:
    valid={k:v for k,v in sensor_scores.items() if v is not None}
    if len(valid)<minimum_modalities:
        return {"state":"INSUFFICIENT_EVIDENCE","confidence":None,"modalities":len(valid)}
    values=list(valid.values())
    mean=sum(values)/len(values)
    spread=max(values)-min(values)
    return {"state":"COLLAPSED" if mean<0.5 or spread>0.6 else "STABLE","confidence":mean,"spread":spread,"modalities":len(valid)}
