# PAMIR-CUAS Public Real-World Field Validation Report

**Release candidate:** FV-2026-09-RC1  
**Validation lane:** `field-validation`  
**Dataset:** TSMS-Drone — Time-Synchronized Multi-Sensor Drone Dataset  
**Scope:** Evidence-grade validation and incident reconstruction. No weapon control, targeting, engagement or interceptor guidance.

## Executive result

PAMIR-CUAS completed a seven-case public real-world field-validation corpus using verified CW radar, FMCW radar and RF receiver measurements, together with explicitly separated controlled evidence perturbations.

The programme demonstrates that PAMIR-CUAS can preserve source provenance, identify evidence-layer disagreement and insufficiency, localize first divergence, reconstruct controlled causal conditions, and serialize reproducible Evidence Objects without modifying the underlying real source measurements.

## Validated real source tuples

### Nominal drone tuple — C-FV01
- Target: Inspire 2
- Distance: 2 m
- Sequential sample index: 001
- Modalities: CW Radar + FMCW Radar + RF Receiver
- Source integrity: PASS
- Evidence-layer nominal multi-sensor agreement: PASS

### Non-drone reference tuple — C-FV07
- Target: Corner Reflector
- Distance: 2 m
- Sequential sample index: 001
- Modalities: CW Radar + FMCW Radar + RF Receiver
- Source-level non-drone stress: PASS_SOURCE_LEVEL
- Classifier false-positive rate: NOT EVALUATED

## Case matrix

| Case | Evidence origin | Condition | Disposition |
|---|---|---|---|
| C-FV01 | REAL_MEASUREMENT | Nominal multi-sensor agreement | PASS |
| C-FV02 | CONTROLLED_PERTURBATION | Radar/RF disagreement | PASS |
| C-FV03 | CONTROLLED_PERTURBATION | Missing sensor evidence | PASS |
| C-FV04 | CONTROLLED_PERTURBATION | Stale/delayed observation | PASS |
| C-FV05 | CONTROLLED_PERTURBATION | Synchronization/index perturbation | PASS |
| C-FV06 | CONTROLLED_PERTURBATION | Evidence/confidence collapse | PASS |
| C-FV07 | REAL_MEASUREMENT | Non-drone source stress | PASS_SOURCE_LEVEL |

## Evidence controls

- Original real measurement payloads are immutable.
- Source payloads used for canonical validation are cryptographically identified by SHA-256.
- REAL_MEASUREMENT and CONTROLLED_PERTURBATION are distinct provenance classes.
- Controlled cases alter evidence state/association semantics, not original source samples.
- No artificial numeric confidence probability is generated where calibration is absent.
- Evidence insufficiency is represented explicitly rather than replaced with an unsupported causal conclusion.
- Dataset-defined sequential synchronization is not represented as GPS/PPS or zero-latency hardware simultaneity.

## Reproducibility

The repository contains provenance records, case definitions, perturbation declarations, Evidence Objects, reproducibility manifests and corpus audit material. Reproduction requires reacquiring the cited public dataset payloads and verifying them against the recorded source hashes before case execution.

## Claims supported by this release candidate

This release candidate supports the statement that PAMIR-CUAS has been evaluated against public real-world multi-sensor measurements and controlled evidence perturbations using a reproducible evidence chain.

## Claims NOT supported

This release candidate does **not** establish:
- operational Counter-UAS effectiveness;
- detection/classification accuracy or measured false-positive rate;
- combat performance;
- hardware-trigger/PPS synchronization;
- weapon-system performance;
- institutional acceptance or certification.

## Next validation tier

**Independent Industry Validation:** externally supplied unseen sensor/evidence datasets, preferably from multiple independent organisations, followed by blind reconstruction and ground-truth comparison.

---
PAMIR-CUAS — Counter-UAS Evidence Fabric  
“Every detection, miss and disagreement should be reconstructable, explainable and reproducible.”
