# Development Guide

## Setup

```bash
python -m venv .venv
pip install -r requirements.txt
pytest -q
```

Run API:
```bash
uvicorn src.main:app --reload
```

Run dashboard:
```bash
streamlit run dashboard/app.py
```

## Guidelines

- Keep network integrations in `src/tools/`.
- Keep agent orchestration in `src/agents/`.
- Prefer typed Pydantic contracts as the project grows.
- Keep real external actions disabled by default during development.
- Add tests before replacing mock terrain/satellite/routing implementations.
- Add Groq tool/function calling as a separate orchestration layer.
