from __future__ import annotations


class ResourceAgent:
    name = "resource_agent"

    def run(self, risk: dict, affected_population: int = 0) -> dict:
        category = risk["category"]
        resources = {
            "rescue_teams": 0, "medical_kits": 0, "evacuation_vehicles": 0
        }

        if category == "critical":
            resources = {
                "rescue_teams": 4,
                "medical_kits": max(20, affected_population // 25),
                "evacuation_vehicles": 4,
            }
        elif category == "high":
            resources = {
                "rescue_teams": 2,
                "medical_kits": max(10, affected_population // 40),
                "evacuation_vehicles": 2,
            }
        elif category == "moderate":
            resources = {
                "rescue_teams": 1,
                "medical_kits": max(5, affected_population // 60),
                "evacuation_vehicles": 1,
            }

        priority = {"critical": "P0", "high": "P1", "moderate": "P2", "low": "P3"}
        return {
            "agent": self.name,
            "priority": priority[category],
            "resources": resources,
        }
