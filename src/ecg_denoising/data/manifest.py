"""Dataset manifest records for the research benchmark."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DatasetRecord:
    """Metadata-only dataset record.

    The manifest records sources and roles only. It does not store raw waveform
    samples, patient identifiers, credentials, or local access notes.
    """

    name: str
    role: str
    source: str
    phase: str
    access: str


def load_manifest(path: Path) -> list[DatasetRecord]:
    """Placeholder manifest loader.

    A future pass should parse a small CSV or JSON manifest stored in git.
    Raw waveform data remain outside the repository.
    """
    if not path.exists():
        raise FileNotFoundError(f"manifest not found: {path}")
    raise NotImplementedError("manifest parsing is planned for the next scaffold pass")
