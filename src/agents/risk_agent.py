from __future__ import annotations

from src.models.risk_model import FloodRiskModel
from src.tools.satellite import get_satellite_features
from src.tools.terrain import get_terrain


class RiskAgent:
    name = "risk_agent"

    def __init__(self, model: FloodRiskModel | None = None) -> None:
        self.model = model or FloodRiskModel()

    def run(self, latitude: float, longitude: float, rainfall_mm: float,
            elevation_m: float | None = None,
            slope_deg: float | None = None,
            ndvi: float | None = None) -> dict:
        terrain = get_terrain(latitude, longitude)
        satellite = get_satellite_features(latitude, longitude)
        elevation = terrain.elevation_m if elevation_m is None else elevation_m
        slope = terrain.slope_deg if slope_deg is None else slope_deg
        vegetation = satellite["ndvi"] if ndvi is None else ndvi

        result = self.model.predict(rainfall_mm, elevation, slope, vegetation)
        return {
            "agent": self.name,
            "risk": result.__dict__,
            "terrain": {"elevation_m": elevation, "slope_deg": slope},
            "satellite": satellite,
        }
