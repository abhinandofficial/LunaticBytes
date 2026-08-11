from __future__ import annotations

from dataclasses import dataclass
import networkx as nx


@dataclass
class RouteResult:
    origin: tuple[float, float]
    destination: tuple[float, float]
    distance_km: float
    status: str


def calculate_route(
    origin: tuple[float, float],
    destination: tuple[float, float],
) -> RouteResult:
    """Tiny NetworkX prototype; replace with an OSMnx road graph."""
    graph = nx.Graph()
    graph.add_edge("origin", "destination", weight=1.0)
    distance = float(nx.shortest_path_length(
        graph, "origin", "destination", weight="weight"
    ))
    return RouteResult(origin, destination, distance, "prototype-route")
