import os
import time
from .scheduler import schedule_calls, start as start_scheduler


def main() -> None:
    base_url = os.getenv("BASE_URL", "")
    schedule_calls(base_url)
    start_scheduler()
    print("AI Boss running. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
