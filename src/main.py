from __future__ import annotations

from typing import Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.agents.coordination_agent import CoordinationAgent

app = FastAPI(
    title="ResQ-Agent API",
    description="Prototype agentic AI disaster prediction and response API.",
    version="0.1.0",
)

coordinator = CoordinationAgent()


class AnalysisRequest(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    rainfall_mm: float = Field(..., ge=0)
    elevation_m: float | None = Field(default=None, ge=-11000)
    slope_deg: float | None = Field(default=None, ge=0)
    ndvi: float | None = Field(default=None, ge=-1, le=1)
    affected_population: int = Field(default=0, ge=0)
    location_name: str = "Unknown location"
    origin_latitude: float | None = None
    origin_longitude: float | None = None
    rainfall_anomaly_threshold_mm: float = Field(default=50, ge=0)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "resq-agent"}


@app.post("/analyze")
def analyze(request: AnalysisRequest) -> dict[str, Any]:
    payload = request.model_dump()
    payload["origin_latitude"] = payload["origin_latitude"] or payload["latitude"]
    payload["origin_longitude"] = payload["origin_longitude"] or payload["longitude"]

    try:
        return coordinator.run(payload)
    except (KeyError, ValueError, RuntimeError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
