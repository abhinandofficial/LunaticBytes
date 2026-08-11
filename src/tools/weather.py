from __future__ import annotations

import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(latitude: float, longitude: float) -> dict:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENWEATHER_API_KEY is not configured.")

    response = requests.get(
        BASE_URL,
        params={"lat": latitude, "lon": longitude, "appid": api_key, "units": "metric"},
        timeout=15,
    )
    response.raise_for_status()
    data = response.json()

    return {
        "latitude": latitude,
        "longitude": longitude,
        "temperature_c": data.get("main", {}).get("temp"),
        "humidity_pct": data.get("main", {}).get("humidity"),
        "rainfall_mm": float(data.get("rain", {}).get("1h", 0.0)),
        "description": (data.get("weather") or [{}])[0].get("description"),
        "source": "OpenWeatherMap",
    }
