from __future__ import annotations

import numpy as np

from ecg_denoising.noise.inject import add_noise_at_snr, scale_noise_to_snr, signal_power
from ecg_denoising.noise.synth import synthetic_ecg, white_noise


def test_white_noise_is_deterministic() -> None:
    first = white_noise(128, seed=7)
    second = white_noise(128, seed=7)
    np.testing.assert_allclose(first, second)


def test_noise_injection_preserves_shape() -> None:
    clean = synthetic_ecg(length=512)
    noise = white_noise(length=512, seed=11)
    noisy = add_noise_at_snr(clean, noise, snr_db=0.0)
    assert noisy.shape == clean.shape


def test_scaled_noise_power_matches_zero_db_snr() -> None:
    clean = synthetic_ecg(length=512)
    noise = white_noise(length=512, seed=13)
    scaled = scale_noise_to_snr(clean, noise, snr_db=0.0)
    assert np.isclose(signal_power(clean), signal_power(scaled), rtol=1e-6)
