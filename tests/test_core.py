from tracemind.core import *
def test_span():
 with Tracer().span('llm',tokens=4) as s: pass
 assert s.attributes['tokens']==4 and s.duration_ms>=0
