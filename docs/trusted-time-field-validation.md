# Trusted Time Field Validation — PAMIR-CUAS

## Goal

Extend the real-world field-validation lane so temporal integrity is evidenced,
not assumed.

This work does not modify the frozen PAMIR-CUAS demonstrator or the PAMIR v0.1
baseline.

## Validation mapping

| Case | Temporal evidence objective |
|---|---|
| C-FV01 nominal agreement | Confirm consistent clock provenance across available sensors |
| C-FV04 stale/delayed observation | Distinguish stale sensor data from clock-reference degradation |
| C-FV05 synchronization perturbation | Detect the first temporal divergence and preserve the clock state that caused it |
| C-FV02 radar/RF disagreement | Test whether apparent sensor disagreement is explained by time misalignment |

## Required per-source evidence

For each radar/RF/EO or supporting data source, capture when available:

- event timestamp
- clock source kind
- clock/reference identifier
- stratum
- NTS authentication state
- hardware timestamping state
- offset
- root delay / root dispersion
- last synchronization age
- holdover / source-switch state
- raw-vs-derived provenance

Missing fields are represented explicitly as unknown evidence.

## Architecture rule

Local PTP/PPS/hardware timestamping and remote NTP validation serve different
roles. Internet NTP is not treated as evidence of nanosecond sensor-to-sensor
alignment.

External GNSS/PPS/NTS Stratum-1 sources can be used as independent UTC anchors
and cross-validation references. The implementation remains provider-neutral;
the Alastyr Stratum-1 service is one candidate for a Türkiye-based validation
reference.

## Acceptance criteria

A C-FV05 run is considered evidence-complete only when the generated Evidence
Object can answer:

1. Which clock/reference was each observation using?
2. What was the measured offset/dispersion or why is it unknown?
3. When did the first temporal divergence occur?
4. Did a source switch, stale sync or holdover state precede it?
5. Can the same conclusion be reproduced from the saved evidence without a live
   time service?

## Next implementation step

Adopt the ARGUS `TimeProvenance` contract for field-data adapters and emit the
temporal-integrity summary into the CUAS Evidence Object/manifest lane.
