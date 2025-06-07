"""Retrieve tasks from the custom to-do list site."""

import os
from typing import List

try:
    import requests
except ImportError:  # pragma: no cover - optional dependency
    requests = None  # type: ignore

TODO_URL = os.getenv("TODO_URL", "https://my-tdl.vercel.app/api/tasks")


def get_tasks() -> List[str]:
    """Return a list of task strings from the to-do list site or dummy data."""
    if requests is None:
        return ["Sample task 1", "Sample task 2"]

    try:
        resp = requests.get(TODO_URL, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            if isinstance(data, list):
                return [str(t.get("title", t)) for t in data]
    except Exception:
        pass
    # Fallback
    return ["Sample task 1", "Sample task 2"]
