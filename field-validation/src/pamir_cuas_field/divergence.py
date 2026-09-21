def first_divergence(sequence: list[dict], predicate) -> dict|None:
    for position,item in enumerate(sequence):
        if predicate(item):
            return {"position":position,"sample_index":item.get("sample_index"),"observation":item}
    return None
