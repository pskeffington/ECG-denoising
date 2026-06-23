"""WFDB loading helpers for real Phase 1 PhysioNet data.

Raw waveform files stay outside git. These functions either stream from
PhysioNet through wfdb or read from a local data cache created by scripts.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import wfdb

from ecg_denoising.data.records import NstdbRecord


@dataclass(frozen=True)
class SignalPair:
    """Aligned clean and noisy ECG signal arrays."""

    clean: np.ndarray
    noisy: np.ndarray
    sample_rate: float
    record: str
    clean_record: str
    snr_db: int
    channel: int = 0


def _as_signal(record: object, channel: int = 0) -> tuple[np.ndarray, float]:
    """Convert a WFDB record object into one channel and sample rate."""
    signal_matrix = getattr(record, "p_signal")
    sample_rate = float(getattr(record, "fs"))
    signal = np.asarray(signal_matrix[:, channel], dtype=float)
    return signal, sample_rate


def read_remote_signal(record_name: str, pn_dir: str, channel: int = 0, sampto: int | None = None) -> tuple[np.ndarray, float]:
    """Read a single channel from PhysioNet through wfdb."""
    record = wfdb.rdrecord(record_name, pn_dir=pn_dir, channels=[channel], sampto=sampto)
    signal = np.asarray(record.p_signal[:, 0], dtype=float)
    sample_rate = float(record.fs)
    return signal, sample_rate


def read_local_signal(data_root: Path, subdir: str, record_name: str, channel: int = 0, sampto: int | None = None) -> tuple[np.ndarray, float]:
    """Read a single channel from a local WFDB cache outside git."""
    record_path = data_root / subdir / record_name
    record = wfdb.rdrecord(str(record_path), sampto=sampto)
    return _as_signal(record, channel=channel)


def load_nstdb_pair(
    row: NstdbRecord,
    channel: int = 0,
    sampto: int | None = None,
    data_root: Path | None = None,
) -> SignalPair:
    """Load aligned NSTDB noisy ECG and corresponding clean MITDB record.

    When ``data_root`` is provided, the loader reads from ``data_root/nstdb``
    and ``data_root/mitdb``. Otherwise it streams records from PhysioNet.
    """
    if data_root is None:
        noisy, noisy_fs = read_remote_signal(row.record, row.noisy_pn_dir, channel=channel, sampto=sampto)
        clean, clean_fs = read_remote_signal(row.clean_record, row.clean_pn_dir, channel=channel, sampto=len(noisy))
    else:
        noisy, noisy_fs = read_local_signal(data_root, "nstdb", row.record, channel=channel, sampto=sampto)
        clean, clean_fs = read_local_signal(data_root, "mitdb", row.clean_record, channel=channel, sampto=len(noisy))

    if noisy_fs != clean_fs:
        raise ValueError(f"sample-rate mismatch: noisy={noisy_fs}, clean={clean_fs}")
    n = min(len(clean), len(noisy))
    return SignalPair(
        clean=clean[:n],
        noisy=noisy[:n],
        sample_rate=noisy_fs,
        record=row.record,
        clean_record=row.clean_record,
        snr_db=row.snr_db,
        channel=channel,
    )
