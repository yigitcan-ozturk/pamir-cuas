# Execution runbook

## 1. Acquire source
Resolve the published TSMS-Drone record, capture repository metadata, then acquire the selected source payloads outside Git. Source payloads remain immutable.

## 2. Build provenance manifest
Create acquisition_records.json locally with path, sensor, target and distance_m for each selected source measurement. Run the inventory command to independently compute SHA-256.

## 3. Source-integrity gate
Run the requested C-FV case gate. Execution is blocked unless at least one complete FMCW/CW/RF index-aligned source set with hashes is available.

## 4. Execute
C-FV01 and C-FV07 must use unmodified measurements. C-FV02 uses observed disagreement if available; otherwise it must be explicitly controlled. C-FV03–05 use declared perturbations. C-FV06 is derived/controlled according to its recorded inputs.

## 5. Evidence object
Record source provenance, observations, alignment integrity, disagreement/fusion/confidence outputs, first divergence, bounded causal reconstruction, evidence sufficiency and reproducibility metadata.

## 6. Independent reproduction
Re-acquire from the published dataset record and compare evidence-relevant fields and hashes under the documented policy.

## 7. Evidence Pack gate
Only assemble a release candidate after all case summaries exist. The institutional gate fails closed for missing, insufficient or unreproduced cases.
