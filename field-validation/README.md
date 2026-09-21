# PAMIR-CUAS Real-World Field Validation

This lane validates the Counter-UAS Evidence Fabric against public real-world multi-sensor measurements.

## Evidence chain

source → provenance → timestamp integrity → observations → association → disagreement → fusion → confidence → first divergence → causal reconstruction → evidence sufficiency → Evidence Object → reproducibility manifest

## Origin classes

- `REAL_MEASUREMENT`: source measurement used without validation-induced alteration.
- `CONTROLLED_PERTURBATION`: immutable real measurement with a documented validation perturbation.
- `DERIVED_FROM_REAL_MEASUREMENT`: deterministic metric or state derived from source observations.

No controlled perturbation may overwrite source data.
