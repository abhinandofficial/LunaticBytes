from __future__ import annotations

import requests
import streamlit as st

st.set_page_config(page_title="ResQ-Agent", page_icon="🌧️", layout="wide")
st.title("🌧️ ResQ-Agent")
st.caption("Agentic AI Disaster Prediction and Response — prototype dashboard")
st.info("Decision-support prototype. Verify recommendations against official emergency guidance.")

api_url = st.sidebar.text_input("Backend URL", "http://127.0.0.1:8000")

c1, c2 = st.columns(2)
with c1:
    location = st.text_input("Location name", "Prototype Area")
    latitude = st.number_input("Latitude", value=10.5276, format="%.6f")
    longitude = st.number_input("Longitude", value=76.2144, format="%.6f")
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, value=85.0)

with c2:
    elevation = st.number_input("Elevation (m)", value=12.0)
    slope = st.number_input("Slope (degrees)", min_value=0.0, value=2.5)
    ndvi = st.slider("NDVI", -1.0, 1.0, 0.42)
    population = st.number_input("Affected population", min_value=0, value=100, step=10)

if st.button("Run ResQ-Agent", type="primary"):
    payload = {
        "latitude": latitude, "longitude": longitude, "rainfall_mm": rainfall,
        "elevation_m": elevation, "slope_deg": slope, "ndvi": ndvi,
        "affected_population": population, "location_name": location,
    }
    try:
        response = requests.post(
            f"{api_url.rstrip('/')}/analyze", json=payload, timeout=30
        )
        response.raise_for_status()
        result = response.json()
        risk = result["risk"]["risk"]

        st.metric("Flood Risk", risk["category"].upper(), f'{risk["score"]:.0%}')
        st.subheader("Response Recommendation")
        st.json(result["resources"])
        st.subheader("Alert")
        st.warning(result["alert"]["message"])

        with st.expander("Full agent output"):
            st.json(result)
        with st.expander("Audit trail"):
            st.json(result["audit"])
    except requests.RequestException as exc:
        st.error(f"Could not reach FastAPI: {exc}")
