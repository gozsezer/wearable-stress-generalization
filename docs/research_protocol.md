# Research protocol (draft)

## Primary goal
Quantify participant-level generalization of wearable stress classifiers and the trade-off between coverage and error when a model abstains.

## Analysis safeguards
1. Freeze definitions of outcome, prediction horizon, and signal availability before training.
2. Audit class distribution and missingness by participant and dataset.
3. Split by participant; keep every transformation within the corresponding training fold.
4. Use nested participant-group validation for tuning; select confidence thresholds on validation predictions only.
5. Evaluate selective risk and coverage, calibration, discrimination and subgroup uncertainty with subject-level uncertainty estimates.
6. Treat independent datasets as external tests only if outcome definitions are harmonizable and data licenses allow use.
7. Publish seeds, package versions, participant-level splitting logic and reporting checklists without exposing identifiable data.

**No WESAD results have been computed in this starter repository.**