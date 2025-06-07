from datetime import datetime
import json
from pathlib import Path
from .notion_logger import log_entry

LOG_PATH = Path("logs.json")


def log_call(call_type: str, text: str):
    """Append call info to a log file."""
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "type": call_type,
        "text": text.strip(),
    }
    if LOG_PATH.exists():
        data = json.loads(LOG_PATH.read_text())
    else:
        data = []
    data.append(entry)
    LOG_PATH.write_text(json.dumps(data, indent=2))
    # Also send to Notion if configured
    log_entry(entry["text"], call_type, entry["timestamp"])
