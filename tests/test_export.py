import json
from tracemind.core import Span
from tracemind.export import span_to_json

def test_span_export():
    payload=json.loads(span_to_json(Span("retrieval", {"k":5}, 12.5)))
    assert payload["name"]=="retrieval"
    assert payload["duration_ms"]==12.5
