# Field-validation methodology

## Evidence classes

1. REAL_MEASUREMENT — unmodified public source measurement.
2. CONTROLLED_PERTURBATION — a documented transformation applied by the validation harness while retaining the immutable source reference.
3. DERIVED_FROM_REAL_MEASUREMENT — deterministic analysis derived from source observations.

## Temporal claim boundary

TSMS-Drone uses a software master loop and sequential file indices for cross-sensor alignment. PAMIR-CUAS therefore treats the sequential loop index as the source alignment key and does not manufacture hardware timestamps.

## Causal claim boundary

A reconstruction may report a first observable divergence and evidence-supported hypotheses. Missing evidence must resolve to PARTIALLY_SUPPORTED, INSUFFICIENT_EVIDENCE, or UNKNOWN rather than an invented cause.

## Reproduction rule

A case is independently reproducible only when source file hashes, code commit, parameters, perturbation specification (if any), and output hashes are recorded.
