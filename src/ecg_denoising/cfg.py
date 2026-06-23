"""Configuration helpers for offline benchmark runs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BenchmarkConfig:
    """Local paths and deterministic controls for offline research runs.

    This object must not contain credentials or patient-specific identifiers.
    Raw data paths should point to local files outside git.
    """

    data_root: Path
    output_root: Path = Path("results")
    seed: int = 1729

    def ensure_output_root(self) -> Path:
        """Create and return the output directory."""
        self.output_root.mkdir(parents=True, exist_ok=True)
        return self.output_root
