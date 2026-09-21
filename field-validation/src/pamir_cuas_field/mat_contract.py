def expected_contract(sensor:str)->dict:
    sensor=sensor.upper()
    contracts={
      "CW_RADAR":{"variable":"data","shape":(16384,)},
      "RF_RECEIVER":{"variable":"data","shape":(262144,)},
      "FMCW_RADAR":{"variable":"RD","shape":(161,4096)},
    }
    if sensor not in contracts: raise ValueError(f"Unsupported sensor: {sensor}")
    return contracts[sensor]

def validate_loaded(sensor:str,variables:dict)->dict:
    c=expected_contract(sensor)
    if c["variable"] not in variables:
        return {"valid":False,"reason":"MISSING_EXPECTED_VARIABLE","expected":c}
    value=variables[c["variable"]]
    shape=tuple(getattr(value,"shape",()))
    normalized=tuple(x for x in shape if x!=1)
    expected=tuple(x for x in c["shape"] if x!=1)
    return {"valid":normalized==expected,"variable":c["variable"],"observed_shape":shape,"expected_shape":c["shape"]}
