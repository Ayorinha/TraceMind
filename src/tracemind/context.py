"""Trace correlation context for distributed AI workflows."""
from dataclasses import dataclass
from uuid import UUID

@dataclass(frozen=True)
class TraceContext:
    trace_id: UUID
    parent_span_id: UUID | None = None
    sampled: bool = True
