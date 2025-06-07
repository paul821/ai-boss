import os
from datetime import datetime
try:
    from notion_client import Client
except ImportError:  # pragma: no cover - optional dependency
    Client = None  # type: ignore

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

_client = Client(auth=NOTION_TOKEN) if (Client and NOTION_TOKEN) else None


def log_entry(summary: str, category: str, timestamp: str) -> None:
    """Log a summary entry to a Notion database if configured."""
    if not _client or not NOTION_DATABASE_ID:
        # Skip when credentials are missing
        return

    _client.pages.create(
        parent={"database_id": NOTION_DATABASE_ID},
        properties={
            "Name": {"title": [{"text": {"content": summary[:100]}}]},
            "Category": {"select": {"name": category}},
            "Time": {"date": {"start": timestamp}},
        },
    )
