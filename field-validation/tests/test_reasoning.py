from pamir_cuas_field.model import Observation,ObservationSet
from pamir_cuas_field.sync import offset_index,synchronization_state
from pamir_cuas_field.confidence import confidence_state
from pamir_cuas_field.divergence import first_divergence

def base():
 return ObservationSet(1,tuple(Observation(s,1,1.0,"fixture") for s in ("FMCW_RADAR","CW_RADAR","RF_RECEIVER")))

def test_sync_perturbation_is_detectable():
 x=offset_index(base(),"RF_RECEIVER",1)
 assert not synchronization_state(x)["aligned"]

def test_missing_confidence_is_not_zero():
 x=confidence_state({"RF_RECEIVER":None})
 assert x["state"]=="INSUFFICIENT_EVIDENCE" and x["confidence"] is None

def test_first_divergence():
 seq=[{"sample_index":1,"bad":False},{"sample_index":2,"bad":True}]
 assert first_divergence(seq,lambda x:x["bad"])["sample_index"]==2
