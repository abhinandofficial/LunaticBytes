from __future__ import annotations

import os
from dotenv import load_dotenv

load_dotenv()


def build_alert(location: str, risk_category: str, risk_score: float) -> str:
    return (
        f"RESQ-AGENT ALERT: Flood risk is {risk_category.upper()} "
        f"({risk_score:.0%}) near {location}. "
        "Follow official local emergency guidance and avoid unsafe routes."
    )


def send_sms(to_number: str, message: str) -> str:
    """Real Twilio action. Keep behind explicit authorization."""
    from twilio.rest import Client

    sid = os.getenv("TWILIO_ACCOUNT_SID")
    token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")
    if not all((sid, token, from_number)):
        raise RuntimeError("Twilio credentials are not fully configured.")

    result = Client(sid, token).messages.create(
        body=message, from_=from_number, to=to_number
    )
    return result.sid
