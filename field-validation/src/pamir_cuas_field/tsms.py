import re
from dataclasses import dataclass
from pathlib import Path

_INDEX = re.compile(r"_(\d{3,})$")

@dataclass(frozen=True)
class SourceRecord:
    sensor: str
    target: str
    distance_m: int
    sample_index: int
    path: str
    representation: str


def parse_source_file(path: str | Path, sensor: str, target: str, distance_m: int) -> SourceRecord:
    p = Path(path)
    m = _INDEX.search(p.stem)
    if not m:
        raise ValueError(f"Cannot derive sequential index from {p.name}")
    suffix = p.suffix.lower()
    representation = "MEASUREMENT" if suffix == ".mat" else "VISUALIZATION" if suffix == ".png" else "UNKNOWN"
    return SourceRecord(sensor.upper(), target, int(distance_m), int(m.group(1)), str(p), representation)


def align_by_index(*streams: list[SourceRecord]) -> list[tuple[SourceRecord, ...]]:
    if not streams:
        return []
    maps = [{r.sample_index: r for r in stream} for stream in streams]
    common = sorted(set.intersection(*(set(m) for m in maps)))
    return [tuple(m[i] for m in maps) for i in common]
