from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RiskResult:
    score: float
    category: str
    factors: list[str]


class FloodRiskModel:
    """Transparent baseline scorer; not a validated hydrological model."""

    def predict(
        self,
        rainfall_mm: float,
        elevation_m: float,
        slope_deg: float,
        ndvi: float = 0.5,
    ) -> RiskResult:
        rainfall = min(max(rainfall_mm / 150.0, 0.0), 1.0)
        elevation = 1.0 - min(max(elevation_m / 100.0, 0.0), 1.0)
        slope = 1.0 - min(max(slope_deg / 30.0, 0.0), 1.0)
        vegetation = 1.0 - min(max(ndvi, 0.0), 1.0)

        score = round(float(min(max(
            0.45 * rainfall + 0.25 * elevation + 0.20 * slope + 0.10 * vegetation,
            0.0, 1.0
        ))), 4)

        if score >= 0.75:
            category = "critical"
        elif score >= 0.55:
            category = "high"
        elif score >= 0.30:
            category = "moderate"
        else:
            category = "low"

        factors = []
        if rainfall >= 0.6:
            factors.append("high rainfall")
        if elevation >= 0.6:
            factors.append("low elevation")
        if slope >= 0.6:
            factors.append("low slope")
        if vegetation >= 0.6:
            factors.append("low vegetation indicator")

        return RiskResult(score=score, category=category, factors=factors)
