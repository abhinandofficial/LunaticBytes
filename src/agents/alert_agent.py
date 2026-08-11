from __future__ import annotations

from src.tools.alerts import build_alert


class AlertAgent:
    name = "alert_agent"

    def run(self, location: str, risk_category: str, risk_score: float,
            send: bool = False, recipient: str | None = None) -> dict:
        message = build_alert(location, risk_category, risk_score)
        result = {
            "agent": self.name, "message": message,
            "sent": False, "status": "dry-run"
        }

        if send:
            if not recipient:
                raise ValueError("recipient is required when send=True")
            from src.tools.alerts import send_sms
            result["message_id"] = send_sms(recipient, message)
            result["sent"] = True
            result["status"] = "sent"

        return result
