# PAMIR-CUAS — Local PA-02/PA-05 Unit Test Record

**Date:** 2026-10-20  
**Status:** LOCAL UNIT TEST PASS — NOT GITHUB ACTIONS / NOT FIELD VALIDATION  
**Source branch:** `docs/pilot-acceptance-v1`  
**Source code:** `tools/pilot_validation.py`, `tests/test_pilot_validation.py`

## Execution

A local reconstruction of the GitHub-fetched functions and their ten test cases was executed in an isolated Python runtime using:

```sh
python -m unittest discover -s tests -v
```

**Result: 10 tests run; 10 passed; 0 failures; 0 errors.**

This execution used a manually reconstructed local copy of the two GitHub files, **not** a Git clone or a GitHub Actions runner. Accordingly, the result is a useful local algorithm check but **not** a source-exact CI attestation. Full repository CI status remains unverified.

## Covered behaviors

- Reference time matching with a fixed tolerance
- Missing independent reference rejection
- One-to-one detection reuse prevention
- Negative tolerance rejection
- First association divergence
- Missing expected association lineage rejection
- Adversarial maximum-cardinality matching
- Non-finite timestamp rejection
- Duplicate timestamp detection reuse prevention
- Identical association lineage agreement

## Limitations / next gates

1. Obtain a GitHub Actions run with a verifiable workflow URL, job logs and commit SHA.
2. Execute the full 15-test suite from an exact checkout of the committed repository.
3. Ground Truth-backed PA-02 needs target identity and spatial gating; temporal-only matching cannot establish a real missed-detection metric.
4. PA-05 expected lineage must come from independent labeled reference evidence.
5. No partner-controlled unseen data or independent blind review has been executed.
6. Test harness runtime and data manifest SHA-256 should be archived for any institutional acceptance run.

**No institutional PASS, sensor detection accuracy, or field qualification is claimed.**
