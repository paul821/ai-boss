"""Google Calendar integration with a simple fallback."""

import os
from datetime import datetime, timedelta
from typing import List, Dict

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
except ImportError:  # pragma: no cover - optional dependency
    service_account = None
    build = None

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def _real_events() -> List[Dict[str, str]]:
    creds_file = os.getenv("GOOGLE_CREDENTIALS")
    calendar_id = os.getenv("GOOGLE_CALENDAR_ID")
    if not creds_file or not calendar_id or not service_account or not build:
        return []

    creds = service_account.Credentials.from_service_account_file(
        creds_file, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=creds)
    now = datetime.utcnow().isoformat() + "Z"
    tomorrow = (datetime.utcnow() + timedelta(days=1)).isoformat() + "Z"
    events_result = (
        service.events()
        .list(
            calendarId=calendar_id,
            timeMin=now,
            timeMax=tomorrow,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])
    return [
        {
            "time": e["start"].get("dateTime", e["start"].get("date", "")),
            "summary": e.get("summary", ""),
        }
        for e in events
    ]


def get_today_events() -> List[Dict[str, str]]:
    """Return today's events from Google Calendar or dummy data."""
    events = _real_events()
    if events:
        return events
    return [
        {"time": "10:00", "summary": "Example meeting"},
        {"time": "15:00", "summary": "Doctor appointment"},
    ]
