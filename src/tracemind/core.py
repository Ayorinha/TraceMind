from __future__ import annotations
from dataclasses import dataclass, field
from time import perf_counter
from typing import Any, Callable
@dataclass(frozen=True, slots=True)
class Span: name: str; duration_ms: float; attributes: dict[str, str] = field(default_factory=dict)
class Tracer:
    def __init__(self): self.spans: list[Span] = []
    def record(self, name: str, fn: Callable[[], Any], **attributes: Any) -> Any:
        if not name.strip(): raise ValueError("span name must be non-empty")
        start = perf_counter()
        try: return fn()
        finally: self.spans.append(Span(name, (perf_counter() - start) * 1000, {str(k): str(v) for k, v in attributes.items()}))
