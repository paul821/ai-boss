# AI Boss

AI Boss is a personal productivity assistant that meets you like a manager
throughout the day. It now creates Zoom meetings instead of phone calls,
while still reading Google Calendar events and logging summaries to Notion.
The morning call prints tasks from your to-do list and shows the next
scheduled check-in times.

## High-Level Features

- **Morning kickoff call**: At 9 AM every weekday the system asks about
your plans and meetings.
- **Content-based followups**: Scheduled check-ins keep you accountable
and record progress.
- **Daily wrap-up call**: An evening call reviews the day and captures a
brief reflection.
- **Notion logging**: Each call summary can be stored in a Notion
database for later review.

## Project Layout

```
ai_boss/
    scheduler.py      # APScheduler jobs that trigger calls
    zoom_client.py    # helper for creating Zoom meetings
    calendar.py       # Google Calendar integration
    tasks.py          # fetch tasks from the todo site
    notion_logger.py  # send call summaries to Notion
    logger.py         # writes call summaries locally
    main.py           # starts the scheduler loop
    tests/            # basic unit tests
run.py                # convenience script to start the app
requirements.txt      # Python dependencies
```

## Getting Started

1. Install Python 3 and create a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set the required environment variables for Zoom, Notion and Google
Calendar. See comments in the source code for names.
4. Start the application locally:

```bash
python run.py
```

When Zoom credentials are configured, meetings will be created
automatically. Without credentials, a dummy join link is printed to the
console for testing.
