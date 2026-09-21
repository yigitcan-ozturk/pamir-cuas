# TSMS-Drone adapter contract

The source dataset is aligned by sequential loop index rather than hardware GPS/PPS timestamps.

Expected source hierarchy is sensor → distance → target → Raw File/Image File. Source files remain read-only.

Adapter output fields:
- sensor
- target
- distance_m
- sample_index
- source_file
- source_sha256
- representation
- measurement payload reference

C-FV01 requires index-matched FMCW, CW and RF observations. No synthetic timestamp is promoted to a source timestamp.
