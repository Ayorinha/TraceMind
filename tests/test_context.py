from uuid import uuid4
from tracemind.context import TraceContext

def test_trace_context_supports_parenting():
    parent=uuid4(); child=TraceContext(uuid4(),parent)
    assert child.parent_span_id == parent
