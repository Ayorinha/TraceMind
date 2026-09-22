from dataclasses import asdict
import json

def span_to_json(span) -> str:
    payload=asdict(span)
    if payload["duration_ms"] < 0: raise ValueError("duration cannot be negative")
    return json.dumps(payload, sort_keys=True, default=str)
