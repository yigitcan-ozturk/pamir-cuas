# Minimum executable real-world slice

The first evidence-producing slice is deliberately small and deterministic.

Selection:
- one published target;
- one published distance;
- one sequential loop index;
- exactly one matching CW, FMCW and RF measurement file.

Required evidence:
- repository file identifier and source URL;
- repository checksum when supplied;
- local SHA-256;
- sensor, target, distance and sequential index;
- successful published MAT variable/shape contract check.

This slice is sufficient to exercise the complete provenance → alignment → observation → evidence-sufficiency → Evidence Object → reproduction path. It is not sufficient to make population-level detection-performance claims. Scaling to the full corpus occurs only after this path reproduces deterministically.
