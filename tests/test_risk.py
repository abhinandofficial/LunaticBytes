from src.models.risk_model import FloodRiskModel


def test_high_rainfall_low_terrain_produces_elevated_risk() -> None:
    result = FloodRiskModel().predict(120, 5, 2, 0.2)
    assert 0 <= result.score <= 1
    assert result.category in {"moderate", "high", "critical"}
    assert "high rainfall" in result.factors
