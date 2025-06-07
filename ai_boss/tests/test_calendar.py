from ai_boss.calendar import get_today_events


def test_get_today_events():
    events = get_today_events()
    assert isinstance(events, list)
    assert events
