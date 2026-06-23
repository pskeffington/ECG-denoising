"""Offline benchmark runner for synthetic placeholder data."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ecg_denoising.methods.classical import bandpass_placeholder
from ecg_denoising.metrics.signal_quality import pearson_corr, prd, rmse, snr_improvement
from ecg_denoising.noise.inject import add_noise_at_snr
from ecg_denoising.noise.synth import synthetic_ecg, white_noise


@dataclass(frozen=True)
class BenchmarkResult:
    """Single synthetic benchmark result row."""

    method: str
    snr_level_db: float
    rmse: float
    prd: float
    pearson_corr: float
    snr_improvement_db: float


def run_synthetic_baseline(length: int = 1000, snr_level_db: float = 0.0, seed: int = 1729) -> BenchmarkResult:
    """Run one offline synthetic placeholder benchmark.

    This does not use clinical data and does not imply clinical validation.
    """
    clean = synthetic_ecg(length=length)
    noise = white_noise(length=length, seed=seed)
    noisy = add_noise_at_snr(clean, noise, snr_level_db)
    denoised = bandpass_placeholder(noisy)
    return BenchmarkResult(
        method="bandpass_placeholder",
        snr_level_db=float(snr_level_db),
        rmse=rmse(clean, denoised),
        prd=prd(clean, denoised),
        pearson_corr=pearson_corr(clean, denoised),
        snr_improvement_db=snr_improvement(clean, noisy, denoised),
    )


def result_as_row(result: BenchmarkResult) -> dict[str, float | str]:
    """Return a CSV-ready dictionary for a benchmark result."""
    return {
        "method": result.method,
        "snr_level_db": result.snr_level_db,
        "rmse": result.rmse,
        "prd": result.prd,
        "pearson_corr": result.pearson_corr,
        "snr_improvement_db": result.snr_improvement_db,
    }
