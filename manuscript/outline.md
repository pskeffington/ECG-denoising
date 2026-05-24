# Manuscript Outline

## Working Title

ECG Noise Reduction for Wearable and ICU Monitoring: A Reproducible Review of Classical, Wavelet, and Deep Learning Denoising Methods Using Open PhysioNet Benchmarks

## 1. Introduction

ECG monitoring is central to clinical cardiology, emergency medicine, intensive care, and wearable health systems. ECG interpretation is degraded by baseline wander, muscle artifact, electrode-motion artifact, and environmental interference. Denoising can improve automated interpretation, but aggressive preprocessing may distort clinically meaningful waveform morphology.

## 2. Rationale

Most ECG denoising work reports signal-quality metrics, but fewer studies systematically evaluate whether denoising preserves clinically relevant ECG features. This review-benchmark addresses that gap by comparing method families under a common open-data protocol.

## 3. Datasets

The benchmark uses the MIT-BIH Noise Stress Test Database for noise injection and stress testing, PTB-XL/PTB-XL+ for clinical ECG morphology and feature preservation, and MIMIC-IV-ECG as a Phase 2 extension for large-scale diagnostic ECG validation.

## 4. Methods Reviewed

The review covers classical filtering, adaptive filtering, wavelet/time-frequency methods, and lightweight deep-learning denoisers.

## 5. Benchmark Protocol

Clean ECG segments are paired with standardized noise injections across multiple SNR levels. Denoising outputs are evaluated with signal-quality metrics and morphology-preservation metrics.

## 6. Clinical Interpretation

The key clinical question is whether denoising improves interpretability without suppressing or distorting medically meaningful ECG features.

## 7. Limitations

The first-stage benchmark uses controlled noise injection and may not fully represent bedside ICU or wearable noise. Credentialed datasets are reserved for secondary validation.

## 8. Conclusion

A reproducible ECG denoising benchmark can clarify which methods improve signal quality while preserving clinically relevant morphology.
