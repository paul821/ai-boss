from ai_boss.logger import log_call, LOG_PATH
import json


def test_log_call(tmp_path, monkeypatch):
    monkeypatch.setattr('ai_boss.logger.LOG_PATH', tmp_path / 'log.json')
    log_call('kickoff', 'hello')
    data = json.loads((tmp_path / 'log.json').read_text())
    assert data[0]['type'] == 'kickoff'
