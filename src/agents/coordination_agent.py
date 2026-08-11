from __future__ import annotations

from datetime import datetime, timezone

from src.agents.alert_agent import AlertAgent
from src.agents.resource_agent import ResourceAgent
from src.agents.risk_agent import RiskAgent
from src.tools.routing import calculate_route


class CoordinationAgent:
    """Starter orchestrator with an in-memory audit trail."""

    name = "coordination_agent"

    def __init__(self) -> None:
        self.risk_agent = RiskAgent()
        self.resource_agent = ResourceAgent()
        self.alert_agent = AlertAgent()
        self.audit_log: list[dict] = []

    def _audit(self, stage: str, output: dict) -> None:
        self.audit_log.append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent": self.name, "stage": stage, "output": output,
        })

    def run(self, payload: dict) -> dict:
        lat, lon = float(payload["latitude"]), float(payload["longitude"])
        rainfall = float(payload["rainfall_mm"])

        weather = {
            "agent": "weather_agent",
            "weather": {
                "latitude": lat, "longitude": lon,
                "rainfall_mm": rainfall, "source": "request"
            },
            "rainfall_anomaly": {
                "is_anomaly": rainfall >= payload.get("rainfall_anomaly_threshold_mm", 50),
                "label": "abnormal" if rainfall >= payload.get(
                    "rainfall_anomaly_threshold_mm", 50
                ) else "normal",
            },
        }
        self._audit("detect", weather)

        risk = self.risk_agent.run(
            lat, lon, rainfall,
            payload.get("elevation_m"),
            payload.get("slope_deg"),
            payload.get("ndvi"),
        )
        self._audit("predict", risk)

        resources = self.resource_agent.run(
            risk["risk"], int(payload.get("affected_population", 0))
        )
        self._audit("prioritize", resources)

        route = calculate_route(
            (float(payload.get("origin_latitude") or lat),
             float(payload.get("origin_longitude") or lon)),
            (lat, lon),
        ).__dict__
        self._audit("deploy", route)

        alert = self.alert_agent.run(
            payload.get("location_name", f"{lat}, {lon}"),
            risk["risk"]["category"], risk["risk"]["score"], send=False
        )
        self._audit("alert", alert)

        return {
            "workflow": "Detect → Predict → Prioritize → Deploy → Alert → Audit",
            "weather": weather, "risk": risk, "resources": resources,
            "route": route, "alert": alert, "audit": list(self.audit_log),
        }
