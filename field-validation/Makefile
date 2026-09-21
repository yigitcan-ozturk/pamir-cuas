PYTHONPATH=src
export PYTHONPATH

.PHONY: test

test:
	python -m pytest -q

inventory:
	python scripts/build_source_manifest.py acquisition_records.json --output source_manifest.json

# Usage: make gate CASE=C-FV01
gate:
	python scripts/run_case.py $(CASE) source_manifest.json

# Evidence pack assembly intentionally requires explicit case-summary inputs.
