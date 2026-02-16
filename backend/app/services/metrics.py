from collections import defaultdict
from datetime import datetime

_metrics = defaultdict(int)
_events = []

def record_event(event_type: str, payload: dict):
    _metrics[event_type] += 1
    _events.append({
        "event": event_type,
        "timestamp": datetime.utcnow().isoformat(),
        "payload": payload
    })

def get_metrics():
    return dict(_metrics)

def get_events(limit: int = 50):
    return _events[-limit:]
