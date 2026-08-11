from src.agents.coordination_agent import CoordinationAgent


def test_coordination_workflow() -> None:
    result = CoordinationAgent().run({
        "latitude": 10.5276, "longitude": 76.2144, "rainfall_mm": 85,
        "elevation_m": 12, "slope_deg": 2.5, "ndvi": 0.42,
        "affected_population": 100, "location_name": "Test Area",
    })
    assert result["workflow"] == "Detect → Predict → Prioritize → Deploy → Alert → Audit"
    assert result["risk"]["risk"]["category"] in {"low", "moderate", "high", "critical"}
    assert len(result["audit"]) >= 5
    assert result["alert"]["sent"] is False
