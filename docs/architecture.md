# ResQ-Agent Architecture

## Principle

Separate **agentic reasoning** from **deterministic tools**. Agents decide what
information/action is needed; tools perform controlled retrieval and computation.

## Runtime Flow

```text
Input → Coordination Agent
          ├─ Weather Agent → Weather Tool → OpenWeatherMap
          ├─ Risk Agent → Terrain + Satellite → GEBCO / Sentinel-style data
          ├─ Resource Agent → Routing Tool → OSM / OSMnx / NetworkX
          ├─ Alert Agent → Alert Tool → Twilio
          └─ Audit Trail
```

## Future Groq Integration

The intended Groq layer should expose strict JSON tool schemas, validate tool
arguments, validate model outputs, limit retries, and record model/tool metadata.
High-impact actions should require human approval.

## Audit

The prototype uses an in-memory audit log. Production should use durable,
tamper-evident storage containing event IDs, timestamps, agent/model metadata,
tool calls, decisions, approvals, and external action IDs.
