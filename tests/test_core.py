from tracemind.core import *

def test_trace():\n t=Tracer();assert t.record("x",lambda:4)==4 and len(t.spans)==1
