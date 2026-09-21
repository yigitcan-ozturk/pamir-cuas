# C-FV01 Modality-Specific Observation Contract

Status: FROZEN FOR C-FV01 v0.1

## Purpose
Define evidence-preserving observation semantics for the verified TSMS-Drone tuple Inspire 2 / 2 m / index 001 without inventing detector thresholds or calibrated physical quantities.

## Source synchronization semantics
TSMS-Drone's published acquisition method uses one MATLAB-controlled multi-sensor acquisition framework. A master loop governs acquisition, each file is stored with a sequential index preserving temporal order, and the loop advances only after all sensors complete logging. Therefore the shared index is accepted as a dataset-defined synchronized acquisition tuple. This does not imply hardware-trigger/PPS simultaneity or zero inter-sensor latency.

## CW_RADAR
Input: complex raw vector `data`, 16384 samples.
Observation domain: Doppler / micro-Doppler.
Permitted deterministic transform: magnitude/frequency representation using the dataset-described CW preprocessing.
Semantic claim allowed at this gate: valid CW observation associated with the labeled Inspire 2 acquisition tuple.
Semantic claim NOT allowed from one sample alone: independently calibrated drone-detection probability.

## FMCW_RADAR
Input: complex matrix `RD`, 161 x 4096.
Observation domain: range-Doppler relative signal representation.
Published limitation: magnitude is relative signal strength, not calibrated power or radar cross section.
Semantic claim allowed: valid FMCW range-Doppler observation associated with the labeled Inspire 2 tuple.
Semantic claim NOT allowed: calibrated RCS/power or independently validated detector confidence.

## RF_RECEIVER
Input: complex raw vector `data`, 131072 samples.
Observation domain: RF spectral activity.
Dataset-described transform: Welch PSD using 256-point Hanning window, 120-sample overlap and 1024-point FFT.
Semantic claim allowed: valid RF observation associated with the labeled Inspire 2 tuple.
Semantic claim NOT allowed: demodulated identity or independently calibrated detection probability.

## Cross-modal agreement rule
For C-FV01 v0.1, nominal agreement requires:
1. source integrity PASS for all three modalities;
2. same dataset-defined target/distance/sequential index;
3. each payload parseable and non-degenerate;
4. no contradictory provenance at the observation layer.

This is an evidence-layer agreement criterion, not a trained-classifier performance claim.

## Confidence rule
No synthetic probability is assigned. Confidence remains EVIDENCE_SUFFICIENCY based until a validated modality-specific detector/calibration model is introduced.

## Safety / scope
No weapon control, targeting, engagement, interceptor guidance, HPM or laser parameters.
