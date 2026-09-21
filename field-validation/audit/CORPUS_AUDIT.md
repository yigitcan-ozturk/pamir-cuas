# PAMIR-CUAS Public Real-World Field Validation — Corpus Audit

Dataset: TSMS-Drone
Lane: field-validation
Audit scope: C-FV01–C-FV07

## Corpus status

| Case | Origin | Primary condition | Result |
|---|---|---|---|
| C-FV01 | REAL_MEASUREMENT | Nominal multi-sensor agreement | PASS |
| C-FV02 | CONTROLLED_PERTURBATION | Radar/RF disagreement | PASS |
| C-FV03 | CONTROLLED_PERTURBATION | Missing sensor evidence | PASS |
| C-FV04 | CONTROLLED_PERTURBATION | Stale/delayed observation | PASS |
| C-FV05 | CONTROLLED_PERTURBATION | Synchronization/index perturbation | PASS |
| C-FV06 | CONTROLLED_PERTURBATION | Evidence/confidence collapse | PASS |
| C-FV07 | REAL_MEASUREMENT | Non-drone source stress | PASS_SOURCE_LEVEL |

## Audit findings
- Source payloads remain immutable under all perturbation cases.
- REAL_MEASUREMENT and CONTROLLED_PERTURBATION provenance classes remain separated.
- All perturbation cases identify a deterministic first-divergence category.
- Evidence sufficiency can degrade to PARTIALLY_SUPPORTED or INSUFFICIENT_EVIDENCE without inventing causal certainty.
- No synthetic numeric confidence probability is introduced.
- C-FV01 and C-FV07 use verified public real-world source payloads.
- C-FV07 does not claim a measured classifier false-positive rate.
- Dataset-defined sequential synchronization is not represented as hardware-trigger/PPS simultaneity.

## Reproducibility disposition
PASS for provenance, source identity, immutable-input policy, case definitions, first-divergence outputs, and evidence-object serialization.

## Explicit limitation
This programme validates the PAMIR-CUAS evidence/reconstruction fabric against public real-world measurements plus controlled evidence perturbations. It is not an operational C-UAS effectiveness trial, classifier benchmark, weapon-system validation, or institutional acceptance test.
