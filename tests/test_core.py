from tracemind.core import Tracer

def test_trace():
    t = Tracer(); assert t.record("x", lambda: 4, model="local") == 4
    assert len(t.spans) == 1 and t.spans[0].attributes["model"] == "local"
