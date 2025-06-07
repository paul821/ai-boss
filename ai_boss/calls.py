from .logger import log_call
from .zoom_client import create_meeting
from .calendar import get_today_events
from .tasks import get_tasks
from .scheduler import get_call_times


PROMPTS = {
    "kickoff": "Morning kickoff! Any meetings or events today?",
    "content": "Progress check! What have you done so far?",
    "final": "Wrap-up time! How did your day go?",
}


def _console_call(prompt: str) -> str:
    print(prompt)
    return input("Your response: ")


def _dial(prompt: str) -> None:
    url = create_meeting(prompt)
    if url:
        print(f"Join Zoom meeting: {url}")


def kickoff_call(base_url: str = "") -> None:
    if base_url:
        _dial(PROMPTS["kickoff"])
    else:
        response = _console_call(PROMPTS["kickoff"])
        log_call("kickoff", response)
        # Display today's schedule and upcoming calls
        events = get_today_events()
        tasks = get_tasks()
        times = get_call_times()
        print("\nToday's events:")
        for e in events:
            print(f"- {e['time']} {e['summary']}")
        print("\nToday's tasks:")
        for t in tasks:
            print(f"- {t}")
        print("\nNext calls:")
        for t in times.get("content", []):
            print(f"- {t}")
        print(f"Final: {times.get('final')}")


def content_call(base_url: str = "") -> None:
    if base_url:
        _dial(PROMPTS["content"])
    else:
        response = _console_call(PROMPTS["content"])
        log_call("content", response)
        print("\nSummary:")
        print(f"- {response[:60]}")


def final_call(base_url: str = "") -> None:
    if base_url:
        _dial(PROMPTS["final"])
    else:
        response = _console_call(PROMPTS["final"])
        log_call("final", response)
        print("\nSummary:")
        print(f"- {response[:60]}")
