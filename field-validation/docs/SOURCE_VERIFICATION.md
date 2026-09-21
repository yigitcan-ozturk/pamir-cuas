# TSMS-Drone source verification record

Verified against the 2026 Scientific Data descriptor and dataset citation.

The source contains CW radar, FMCW radar and RF receiver measurements from four commercial drones and one non-drone target, measured from 2 m through 30 m at 2 m increments with 500 repetitions per condition.

Temporal alignment is software-based: one MATLAB master loop controls acquisition and advances only after all three sensors complete logging. Files use a sequential index as the cross-sensor alignment key. The paper explicitly states that GPS/PPS hardware triggers are not used and describes the result as sub-second temporal alignment.

Published measurement contracts used by this harness are CW data complex vector with 16,384 samples, RF data complex vector with 262,144 samples, and FMCW RD 161 x 4096 range-Doppler array. Measurement files use .mat and corresponding visualizations are .png.

The article Data Availability statement says the dataset is publicly accessible under CC BY 4.0. The journal article itself has a separate CC BY-NC-ND 4.0 publication licence; these licences must not be conflated.

Payload-level checksums remain pending until actual source files are acquired. No measurement result is asserted by this record.
