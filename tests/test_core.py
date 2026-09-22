from tracemind.core import Tracer

def test_trace():
    tracer = Tracer()
    assert tracer.record("x", lambda: 4) == 4
    assert len(tracer.spans) == 1
