# Project Scope

## Research Question

Among open ECG datasets, how do classical filtering, wavelet/time-frequency methods, and lightweight deep-learning denoisers compare in reducing common ECG noise while preserving clinically relevant waveform morphology?

## Clinical Motivation

ECG monitoring is central to cardiology, emergency medicine, intensive care, and wearable health systems. Denoising can improve interpretability and downstream automated classification, but aggressive preprocessing may distort clinically meaningful waveform morphology.

## Signal Focus

Version 1 is limited to ECG. Other physiological signals, including EEG, EMG, PPG, and PCG, are excluded from the initial benchmark to preserve methodological clarity.

## Noise Classes

- Baseline wander
- Muscle artifact
- Electrode-motion artifact
- Powerline interference
- Mixed wearable or ICU monitoring noise

## Method Families

- Classical filters
- Adaptive filters
- Wavelet and time-frequency methods
- Lightweight deep-learning denoisers

## Primary Contribution

This project contributes a reproducible review-benchmark framework that separates signal-quality improvement from preservation of clinically relevant ECG morphology.

## Exclusions

- Proprietary device algorithms
- Non-ECG signals in v1
- Large opaque deep-learning models without reproducible implementation
- Claims of diagnostic improvement without downstream validation

## Phase 1 Deliverables

- Dataset inventory
- Noise taxonomy
- Method review matrix
- Benchmark protocol
- Classical filter baseline
- Wavelet baseline
