# ECG Noise Taxonomy

## Baseline Wander

Baseline wander is a low-frequency drift commonly caused by respiration, body movement, or electrode impedance changes. It can obscure ST-segment interpretation and distort low-frequency morphology.

## Muscle Artifact

Muscle artifact reflects electromyographic contamination from skeletal muscle activity. It is common in ambulatory and wearable ECG and may obscure P waves, QRS onset, and repolarization features.

## Electrode-Motion Artifact

Electrode-motion artifact occurs when electrode-skin contact changes during movement. It is clinically important because it may mimic arrhythmia, obscure QRS complexes, or create false waveform deviations.

## Powerline Interference

Powerline interference is narrow-band environmental contamination, commonly near 50 or 60 Hz depending on region. It is usually addressed with notch or adaptive filtering, but aggressive filtering can distort nearby spectral content.

## Mixed ICU or Wearable Noise

Real-world monitoring noise is often mixed rather than isolated. ICU and wearable ECG may combine motion artifact, baseline drift, equipment interference, and physiologic signal overlap.

## Benchmark Handling

| Noise Class | Phase 1 Handling | Phase 2 Handling |
|---|---|---|
| Baseline wander | MIT-BIH NSTDB noise injection | ICU/wearable validation |
| Muscle artifact | MIT-BIH NSTDB noise injection | ICU/wearable validation |
| Electrode-motion artifact | MIT-BIH NSTDB noise injection | ICU/wearable validation |
| Powerline interference | Synthetic injection | Site-specific extension |
| Mixed noise | Limited v1 handling | MIMIC waveform extension |
