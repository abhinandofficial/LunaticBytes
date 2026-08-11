from __future__ import annotations

import hashlib


def get_satellite_features(latitude: float, longitude: float) -> dict:
    """Deterministic mock Sentinel-2-compatible features."""
    key = f"{latitude:.6f}:{longitude:.6f}".encode()
    seed = int(hashlib.sha256(key).hexdigest()[:8], 16)
    ndvi = 0.25 + (seed % 50) / 100.0
    ndwi = 0.10 + ((seed // 50) % 50) / 100.0
    return {
        "source": "mock-sentinel-2-compatible",
        "ndvi": round(min(ndvi, 0.99), 3),
        "ndwi": round(min(ndwi, 0.99), 3),
    }
