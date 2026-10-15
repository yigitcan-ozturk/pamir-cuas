# PAMIR-CUAS — Pilot Acceptance Protocol v1.0 (DRAFT)

**Status:** PROPOSED / NOT EXECUTED  
**Owner:** PAMILANGA LIMITED  
**Scope:** Counter-UAS Evidence Fabric — evidence reconstruction and assurance only.

## Change control
This document does not modify PAMIR v0.1.0, the frozen PAMIR-CUAS demonstrator, the frozen website, or NATO Data Challenge source materials. The protocol is separate from field qualification and operational certification.

## Evidence provenance
Each test must record dataset identifier and license/access class; raw-file SHA-256; sensor type; original vs injected/derived observations; ground-truth availability; software commit; environment; parameter manifest; command; start/end timestamps; output SHA-256; and complete logs.

## Acceptance test families
| ID | Family | Required observation | Failure conditions |
|---|---|---|---|
| PA-01 | False positive | Reconstruct non-drone alarm and evidence chain | Unsupported classification or missing provenance |
| PA-02 | Missed detection | Identify absent detection window against available reference | Treating missing ground truth as a confirmed miss |
| PA-03 | Sensor disagreement | Preserve radar/RF observations and disagreement chronology | Collapsing conflicting observations without trace |
| PA-04 | Timing and synchronization | Record clock offset, ordering, and uncertainty | Untraceable timestamps or fabricated synchronization |
| PA-05 | Track association | Trace association changes and first divergence | Missing association provenance |
| PA-06 | Confidence evolution | Reproduce confidence timeline and collapse | Non-reproducible confidence values |
| PA-07 | Counterfactual replay | Re-run a declared, bounded perturbation with recorded parameters | Conflating counterfactual and measured evidence |
| PA-08 | Evidence integrity | Verify canonical outputs and SHA-256 manifests | Hash mismatch, missing source, or non-deterministic result without explanation |

## Outcome rules
- **PASS:** Required artifacts are present, integrity checks pass, and pre-frozen test-specific tolerances are satisfied.
- **PARTIAL:** Some requirements are met but a stated gap remains; record exactly which.
- **FAIL:** A required test assertion or integrity check fails; preserve original logs.
- **NOT RUN:** Execution has not occurred; never convert this to PASS.
- **BLOCKED:** External data, interface definition, authorization, or environment is unavailable.

Numerical thresholds, latency budgets, ground-truth matching tolerances and acceptance-critical assertions must be agreed and frozen **before** partner-controlled unseen-data execution. No retrospective threshold tuning.

## Independence and dataset separation
Development fixtures, synthetic perturbations, and any previously inspected recordings are **not** blind-validation evidence. A partner controls unseen inputs, execution conditions and independent review. Public or real-world origin alone does not establish blind independence.

## Institutional gates
| Gate | Status | Required next evidence |
|---|---|---|
| G01 Technical Annex | CLOSED (per Annex v1.0) | Preserve frozen record |
| G02 Interface selection | OPEN | Data class, ICD/profile and mapping contract |
| G03 Security/data handling | OPEN | Authorized environment, access and retention plan |
| G04 Blind criteria freeze | OPEN | Agreed metrics, tolerances, ground-truth access |
| G05 Partner execution | NOT RUN | Unseen dataset and immutable output package |
| G06 Independent review | NOT RUN | Reproduction and signed disposition |
| G07 Integration pilot decision | OPEN | Review result and bounded estimate |
| G08 Field qualification | FUTURE | Programme-specific authorization and evidence |

## Current evidence boundary
The prior Technical Annex v1.0 reports 39/39 passing tests and successful CI for its own frozen demonstrator commit. Those historical results are **not** execution results for this protocol. All PA-01–PA-08 tests are currently **NOT RUN** under this protocol.

## Next execution sequence
1. Inventory accessible dataset and code versions without changing baselines.
2. Map existing C-FV01–C-FV07 cases to PA-01–PA-08, noting uncovered requirements.
3. Pre-register deterministic assertions and tolerances.
4. Execute reproducibility and integrity checks on accessible non-blind data.
5. Retain failure logs and publish an evidence matrix.
6. Request partner-controlled unseen data and independent sign-off.
