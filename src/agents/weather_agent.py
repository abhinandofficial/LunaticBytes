from __future__ import annotations

from src.models.anomaly_detection import RainfallAnomalyDetector
from src.tools.weather import get_weather


class WeatherAgent:
    name = "weather_agent"

    def __init__(self, detector: RainfallAnomalyDetector | None = None) -> None:
        self.detector = detector

    def run(self, latitude: float, longitude: float,
            rainfall_override_mm: float | None = None) -> dict:
        if rainfall_override_mm is None:
            weather = get_weather(latitude, longitude)
        else:
            weather = {
                "latitude": latitude, "longitude": longitude,
                "rainfall_mm": float(rainfall_override_mm),
                "source": "manual/mock input",
            }

        anomaly = None
        if self.detector is not None:
            anomaly = self.detector.predict(
                float(weather.get("rainfall_mm", 0.0))
            ).__dict__

        return {"agent": self.name, "weather": weather,
                "rainfall_anomaly": anomaly}
