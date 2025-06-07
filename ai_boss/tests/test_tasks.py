from ai_boss.tasks import get_tasks


def test_get_tasks_returns_list(monkeypatch):
    monkeypatch.setattr('ai_boss.tasks.requests', None)
    tasks = get_tasks()
    assert isinstance(tasks, list)
    assert tasks
