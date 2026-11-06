# Wearable Stress Generalization

**Status:** Work in progress — methodological starter repository; no empirical study results are claimed here.

## Research question
Can wearable-sensor stress classifiers generalize across participants, and does abstaining from low-confidence predictions improve reliability at a transparent cost in coverage?

## Planned study
- Dataset: publicly available WESAD, subject to its original license and access conditions; independent validation datasets only if labels, modalities and ethics permit meaningful comparisons.
- Unit of separation: participant, not window. No participant may appear in both training and test data.
- Features: physiological signals with preprocessing defined per dataset; no participant identifiers used as predictors.
- Baselines: regularized logistic regression and tree-based classifiers; optional temporal models only when justified by sample size.
- Evaluation: leave-one-subject-out or grouped nested validation; AUROC and AUPRC when both classes occur; balanced accuracy, sensitivity, specificity, calibration, coverage–risk curves and confidence intervals.
- Leakage prevention: fit normalization, feature selection, sampling and tuning on training folds only. Select abstention thresholds on validation data, never on the held-out participant.
- External validation: only after prespecified label harmonization; report dataset shift and missing modalities.

## Repository structure
- `src/demo.py`: runnable synthetic-data demonstration of group-disjoint evaluation.
- `tests/test_demo.py`: checks participant separation and output ranges.
- `requirements.txt`: minimal dependencies.
- `docs/research_protocol.md`: planned analysis and reporting safeguards.

## Quick start
```bash
python -m pip install -r requirements.txt
python src/demo.py
python -m unittest discover -s tests
```

## Important limitations
The demonstration uses **synthetic data**, not WESAD or nurse participant data. Its metrics are only software checks and must never be cited as scientific results. Do not commit identifiable participant records or data without redistribution permission.

## License and data
Code license: MIT. Third-party datasets retain their original terms; this repository does not redistribute them.