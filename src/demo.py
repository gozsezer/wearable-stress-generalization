"""Synthetic example only. No empirical conclusions may be drawn from these results."""
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, roc_auc_score


def run_demo(seed=42):
    X, y = make_classification(n_samples=600, n_features=8, n_informative=4,
                               weights=[0.6, 0.4], random_state=seed)
    groups = np.repeat(np.arange(30), 20)
    split = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=seed)
    train, test = next(split.split(X, y, groups))
    assert set(groups[train]).isdisjoint(set(groups[test]))
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, random_state=seed))
    model.fit(X[train], y[train])
    probabilities = model.predict_proba(X[test])[:, 1]
    result = {
        "train_subjects": len(np.unique(groups[train])),
        "test_subjects": len(np.unique(groups[test])),
        "balanced_accuracy": float(balanced_accuracy_score(y[test], probabilities >= 0.5)),
        "auroc": float(roc_auc_score(y[test], probabilities)),
    }
    return result


if __name__ == "__main__":
    print("SYNTHETIC DEMONSTRATION — NOT STUDY RESULTS")
    for key, value in run_demo().items():
        print(f"{key}: {value}")