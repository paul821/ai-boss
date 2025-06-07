from ai_boss.zoom_client import create_meeting


def test_create_meeting_returns_link(monkeypatch):
    monkeypatch.delenv('ZOOM_JWT', raising=False)
    monkeypatch.delenv('ZOOM_USER_ID', raising=False)
    url = create_meeting('Test')
    assert url.startswith('https://')
