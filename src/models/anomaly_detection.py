from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from sklearn.ensemble import IsolationForest


@dataclass
class AnomalyResult:
    is_anomaly: bool
    score: float
    label: str


class RainfallAnomalyDetector:
    """Starter anomaly detector. Replace with a validated regional model."""

    def __init__(self, contamination: float = 0.1) -> None:
        self.model = IsolationForest(
            contamination=contamination,
            random_state=42,
            n_estimators=100,
        )
        self._fitted = False

    def fit(self, rainfall_mm: list[float] | np.ndarray) -> "RainfallAnomalyDetector":
        values = np.asarray(rainfall_mm, dtype=float).reshape(-1, 1)
        if len(values) < 5:
            raise ValueError("At least 5 rainfall observations are required.")
        self.model.fit(values)
        self._fitted = True
        return self

    def predict(self, rainfall_mm: float) -> AnomalyResult:
        if not self._fitted:
            raise RuntimeError("Call fit() before predict().")
        value = np.asarray([[float(rainfall_mm)]])
        prediction = int(self.model.predict(value)[0])
        score = float(self.model.decision_function(value)[0])
        return AnomalyResult(
            is_anomaly=prediction == -1,
            score=score,
            label="abnormal" if prediction == -1 else "normal",
        )
