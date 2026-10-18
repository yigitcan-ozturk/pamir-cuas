# PAMIR-CUAS — Field-to-Pilot Traceability Matrix v0.1

**Status:** PROPOSED MAPPING — NOT EXECUTED  
**Basis:** `field-validation/README.md` scenario descriptions and `docs/PILOT_ACCEPTANCE_PROTOCOL_v1.0.md` on `docs/pilot-acceptance-v1`.  
**Scope:** Assurance, incident reconstruction, and reproducible evidence only.

| Field scenario | Primary pilot acceptance family | Secondary checks | Execution status |
|---|---|---|---|
| C-FV01 Nominal multi-sensor agreement | PA-08 Evidence integrity | PA-03 disagreement baseline; PA-06 confidence evolution | NOT RUN |
| C-FV02 Radar/RF disagreement | PA-03 Sensor disagreement | PA-05 association trace; PA-08 integrity | NOT RUN |
| C-FV03 Missing sensor evidence | PA-02 Missed detection **only when reference truth exists** | PA-08 completeness | NOT RUN |
| C-FV04 Stale/delayed observation | PA-04 Timing and synchronization | PA-05 first divergence | NOT RUN |
| C-FV05 Synchronization perturbation | PA-04 Timing and synchronization | PA-07 counterfactual replay | NOT RUN |
| C-FV06 Confidence collapse | PA-06 Confidence evolution | PA-07 counterfactual replay | NOT RUN |
| C-FV07 Non-drone false-positive stress | PA-01 False positive | PA-08 integrity | NOT RUN |

## Coverage gaps and non-equivalence

1. **PA-02 missed detection:** Missing sensor evidence is not automatically proof of a missed detection. Requires independent reference/GT and a frozen matching rule.
2. **PA-05 track association:** No dedicated C-FV case explicitly tests incorrect track association. Add a separate, bounded association fixture and independently verified expected lineage.
3. **PA-07 counterfactual replay:** Perturbation scenarios can support replay, but only if baseline, perturbation, parameters, and output hashes are retained separately.
4. **PA-08 evidence integrity:** Apply as a cross-cutting requirement to every scenario, not only C-FV01.
5. **Blind independence:** None of the above becomes a partner-controlled blind result without unseen data and independent review.

## Required artifact checklist per executed case

- Input manifest with dataset ID, source/access class, sensor modality, raw SHA-256
- Reference-truth status and permitted evaluation use
- Original vs synthetic/perturbed data labeling
- Code commit SHA and dependency/environment lock
- Frozen test assertions and tolerances, registered before execution
- Deterministic command/configuration and random seed if applicable
- Time/provenance/association/confidence lineage as applicable
- Output report SHA-256 and complete stdout/stderr logs
- Reviewer disposition: PASS, PARTIAL, FAIL, NOT RUN or BLOCKED

## Immediate engineering backlog

1. Inventory repository tree, actual executable test harnesses, data schemas and licenses.
2. Create a read-only evidence inventory; do not mutate frozen baselines.
3. Implement schema checks for manifests and deterministic integrity assertions on a separate development branch.
4. Add dedicated PA-05 association test and ground-truth-backed PA-02 missed detection test.
5. Execute non-blind reproducibility tests, preserving negative results.
6. Freeze acceptance thresholds with a partner before any unseen-data run.

**Evidence statement:** This document is a planning and traceability artifact. No test execution or measured PASS is claimed.
