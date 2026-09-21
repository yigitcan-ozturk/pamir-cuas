# Claim boundaries

PAMIR-CUAS field-validation reports must distinguish observation from inference.

- Dataset measurements are source observations.
- Sequential filename indices are alignment keys, not hardware clock timestamps.
- A controlled index offset is a synchronization perturbation, not evidence that the original experiment experienced clock drift.
- Sensor dropout injected by the harness is not a naturally observed sensor failure.
- A confidence-collapse result is derived from declared inputs and a versioned rule; it is not ground truth about target identity.
- A false-positive result requires a declared detection rule and a source-labelled non-drone reference.
- When required evidence is absent, the result must remain PARTIALLY_SUPPORTED, INSUFFICIENT_EVIDENCE, or UNKNOWN.

No field-validation result may be used to claim weapon effectiveness, targeting performance, engagement performance, or interceptor guidance performance.
