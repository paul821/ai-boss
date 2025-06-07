import os
import time
from typing import Optional

try:
    import requests
except ImportError:  # pragma: no cover - optional dependency
    requests = None  # type: ignore

ZOOM_JWT = os.getenv("ZOOM_JWT")
ZOOM_USER_ID = os.getenv("ZOOM_USER_ID")


def create_meeting(topic: str) -> Optional[str]:
    """Create a Zoom meeting and return the join URL, or a dummy link."""
    if not all([ZOOM_JWT, ZOOM_USER_ID, requests]):
        print("Zoom credentials not configured. Returning dummy link.")
        return f"https://zoom.us/j/{int(time.time())}"

    headers = {
        "Authorization": f"Bearer {ZOOM_JWT}",
        "Content-Type": "application/json",
    }
    payload = {"topic": topic, "type": 1}
    resp = requests.post(
        f"https://api.zoom.us/v2/users/{ZOOM_USER_ID}/meetings",
        headers=headers,
        json=payload,
        timeout=10,
    )
    if resp.status_code == 201:
        return resp.json().get("join_url")
    print("Failed to create Zoom meeting")
    return None
