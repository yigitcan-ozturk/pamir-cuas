# PAMIR-CUAS

**Counter-UAS Evidence Fabric**

> Every detection, miss and disagreement should be reconstructable, explainable and reproducible.

PAMIR-CUAS provides evidence-grade validation and incident reconstruction for Counter-UAS systems.

## Real-World Field Validation Programme

This repository hosts the independent PAMIR-CUAS development lane. The current programme moves validation from synthetic scenarios to public real-world multi-sensor measurements and reproducible evidence objects.

Validation progression:

`Synthetic → Public Real-World → Independent Reproduction → Partner Data → Controlled Range Trial → Institutional Validation`

### Initial corpus

- C-FV01 — nominal multi-sensor agreement
- C-FV02 — radar/RF disagreement
- C-FV03 — missing sensor evidence
- C-FV04 — stale/delayed observation
- C-FV05 — synchronization perturbation
- C-FV06 — confidence collapse
- C-FV07 — non-drone false-positive stress

Real measurements and controlled perturbations are explicitly distinguished in every evidence object and manifest.

## Scope boundary

PAMIR-CUAS is an evidence, assurance and validation layer. It does **not** implement weapon control, targeting, engagement logic, interceptor guidance, or HPM/laser attack parameters.

## Repository policy

The PAMIR v0.1 frozen baseline, frozen PAMIR-CUAS demonstrator, and frozen website are outside this repository and are not modified by this programme.
