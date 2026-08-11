from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TerrainSample:
    elevation_m: float
    slope_deg: float


def get_terrain(latitude: float, longitude: float) -> TerrainSample:
    """Prototype GEBCO adapter. Replace with raster-backed terrain lookup."""
    del latitude, longitude
    return TerrainSample(elevation_m=25.0, slope_deg=4.0)
