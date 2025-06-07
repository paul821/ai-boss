from apscheduler.schedulers.background import BackgroundScheduler
from .calls import kickoff_call, content_call, final_call

scheduler = BackgroundScheduler()

# Stored times for display during the kickoff call
CALL_TIMES = {
    "kickoff": "09:00",
    "content": [],
    "final": "21:00",
}


def schedule_calls(base_url: str = "",
                   kickoff_time: str = "09:00",
                   content_times=None,
                   final_time: str = "21:00") -> None:
    if content_times is None:
        content_times = ["11:00", "13:00", "16:00", "19:00"]

    CALL_TIMES["kickoff"] = kickoff_time
    CALL_TIMES["content"] = content_times
    CALL_TIMES["final"] = final_time

    h, m = map(int, kickoff_time.split(":"))
    scheduler.add_job(kickoff_call, "cron", day_of_week="mon-fri", hour=h, minute=m, args=[base_url])

    for t in content_times:
        h, m = map(int, t.split(":"))
        scheduler.add_job(content_call, "cron", day_of_week="mon-fri", hour=h, minute=m, args=[base_url])

    h, m = map(int, final_time.split(":"))
    scheduler.add_job(final_call, "cron", day_of_week="mon-fri", hour=h, minute=m, args=[base_url])


def start() -> None:
    scheduler.start()


def get_call_times() -> dict:
    """Return the currently scheduled call times."""
    return CALL_TIMES
