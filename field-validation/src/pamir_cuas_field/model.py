from dataclasses import dataclass, field
from typing import Any, Mapping

@dataclass(frozen=True)
class Observation:
    sensor: str
    sample_index: int
    value: float
    source_file: str
    timestamp_s: float | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)

@dataclass(frozen=True)
class ObservationSet:
    sample_index: int
    observations: tuple[Observation, ...]

    @property
    def sensors(self) -> tuple[str, ...]:
        return tuple(sorted(o.sensor for o in self.observations))
