from src.models.anomaly_detection import RainfallAnomalyDetector


def test_rainfall_anomaly_detector() -> None:
    detector = RainfallAnomalyDetector(contamination=0.1)
    detector.fit([2, 3, 4, 5, 4, 3, 5, 4, 6, 5, 4, 3])
    result = detector.predict(1000)
    assert result.is_anomaly is True
    assert result.label == "abnormal"
