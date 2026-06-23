"""WFDB loading helpers for real Phase 1 PhysioNet data.

Raw waveform files stay outside git. These functions either stream from
PhysioNet through wfdb or read from a local data cache created by scripts.
"""

from __future__ import annotations

from dataclasses import dataclass

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


def read_remote_signal(record_name: str, pn_dir: str, channel: int = 0, sampto: int | None = None) -> tuple[np.ndarray, float]:
    """Read a single channel from PhysioNet through wfdb."""
    record = wfdb.rdrecord(record_name, pn_dir=pn_dir, channels=[channel], sampto=sampto)
    signal = np.asarray(record.p_signal[:, 0], dtype=float)
    sample_rate = float(record.fs)
    return signal, sample_rate


def load_nstdb_pair(row: NstdbRecord, channel: int = 0, sampto: int | None = None) -> SignalPair:
    """Load aligned NSTDB noisy ECG and corresponding clean MITDB record."""
    noisy, noisy_fs = read_remote_signal(row.record, row.noisy_pn_dir, channel=channel, sampto=sampto)
    clean, clean_fs = read_remote_signal(row.clean_record, row.clean_pn_dir, channel=channel, sampto=len(noisy))
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
