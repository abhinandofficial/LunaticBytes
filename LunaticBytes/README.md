
                                                              Disaster Management System

Team Name Lunatic Bytes

Team Members
Abhinand C Varghese
Adarsh Parakkal Benoy
Adithya KB
Problem Statement

Natural disasters such as floods and extreme rainfall can develop rapidly and affect large populations. Emergency response teams need to analyze weather, terrain, geographic, and environmental data quickly to identify high-risk areas and make informed decisions.

Traditional disaster-management workflows often involve fragmented data sources and manual analysis, which can delay risk assessment, resource allocation, and emergency communication.

Solution

The Disaster Management System is an Agentic AI-based system designed to analyze disaster-related data and support emergency response.

The system combines weather, terrain, geospatial, satellite-style, and machine-learning data to detect abnormal conditions, predict disaster risk, identify affected areas, prioritize emergency resources, generate alerts, and maintain an audit trail of agent decisions.

The system follows the workflow:

Detect → Predict → Prioritize → Deploy → Alert → Audit

Features
Abnormal rainfall detection
Hyper-local flood-risk analysis
Terrain and elevation analysis
Geospatial data processing
Satellite-style data analysis
Affected-area identification
Emergency resource prioritization
Route and deployment recommendations
Emergency alert generation
Multi-agent coordination
Agent decision audit trail
Machine-learning based anomaly detection
FastAPI backend
Streamlit dashboard
Twilio SMS integration
OpenStreetMap-based geographic support
Modular and extensible architecture



Agent Workflow / Flowchart
             ┌─────────────────────┐
             │      Data Input           │
             │ Weather / Geo /           │
             │ Terrain / Satellite       │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │   Weather Agent           │
             │       DETECT              │
             │ Rainfall Anomalies        │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │     Risk Agent            │
             │      PREDICT              │
             │   Disaster Risk           │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │   Resource Agent          │
             │     PRIORITIZE            │
             │ Emergency Resources       │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Deployment / Routing      │
             │       DEPLOY              │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │     Alert Agent           │
             │       ALERT               │
             │ Emergency Messages        │
             └──────────┬──────────┘
                        │
                        ▼
             ┌─────────────────────┐
             │ Coordination Agent        │
             │       AUDIT               │
             │ Decision Audit Trail      │
             └─────────────────────┘





Agent Architecture

The system consists of five specialized agents coordinated by a central Coordination Agent.

Weather Agent

Collects weather information and analyzes rainfall conditions to detect abnormal precipitation.

Risk Agent

Combines rainfall, terrain, elevation, slope, and satellite-style environmental features to calculate and classify disaster risk.

Resource Agent

Analyzes the predicted risk and affected population to prioritize emergency resources such as rescue teams, medical supplies, and evacuation vehicles.

Alert Agent

Generates emergency alerts based on the detected risk level and provides an interface for sending notifications through services such as Twilio.

Coordination Agent

Coordinates the complete workflow between agents, manages the sequence of operations, and maintains an audit trail of agent decisions.



Architecture Overview
                    ┌───────────────────┐
                    │ Streamlit              │
                    │ Dashboard              │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ FastAPI Backend        │
                    └─────────┬─────────┘
                              │
                              ▼
                  ┌─────────────────────────┐
                  │   Coordination Agent           │
                  └──────┬──────┬──────┬────┘
                            │      │      │
              ┌──────────┘      │      └──────────┐
              ▼                 ▼                 ▼
       ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
       │Weather Agent    │   │ Risk Agent     │   │ Resource        │
       │                 │   │                │   │    Agent        │
       └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
                │                       │                           │
              ▼                 ▼                 ▼
        Weather API       ML / Terrain       Routing / OSM
                          / Satellite
                                                │
                                                ▼
                                         ┌─────────────┐
                                         │ Alert Agent     │
                                         └──────┬──────┘
                                                │
                                                ▼
                                             Twilio


Tech Stack

Frontend
Streamlit
Python
Backend
FastAPI
Uvicorn
Python 3.11+
AI / LLM
Groq API
Groq tool/function calling
scikit-learn
NumPy
Pandas
Agent Framework
Custom modular Python multi-agent architecture
Groq tool/function calling
Specialized Weather, Risk, Resource, Alert, and Coordination Agents
Tools / APIs
OpenWeatherMap API — Weather data
OpenStreetMap — Geographic and road data
GEBCO — Terrain and elevation data
Sentinel-2-compatible mock data — Satellite-style environmental features
GeoPandas — Geospatial processing
Shapely — Geometry operations
OSMnx — Road-network analysis
NetworkX — Graph and routing analysis
Twilio — Emergency SMS alerts
python-dotenv — Environment configuration
Database

The current prototype uses an in-memory audit trail and does not require a dedicated database.

A future production version can use:

PostgreSQL
PostGIS
SQLite
Setup / How to Run
1. Clone the Repository
git clone <repository-url>
cd Lunatic-Bytes
2. Create a Virtual Environment
python -m venv .venv

Windows:

.venv\Scripts\activate

Linux/macOS:

source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file based on .env.example:

GROQ_API_KEY=
OPENWEATHER_API_KEY=
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=

Do not commit real API keys to the repository.

5. Run the Backend
uvicorn src.main:app --reload

The API will be available at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs
6. Run the Streamlit Dashboard
streamlit run dashboard/app.py
7. Run Tests
pytest -q
