from dataclasses import dataclass,field
from time import perf_counter
@dataclass
class Span: name:str; attributes:dict[str,object]=field(default_factory=dict); duration_ms:float=0
class Tracer:
 def span(self,name,**attrs): return _Context(Span(name,attrs),perf_counter())
class _Context:
 def __init__(self,s,t): self.s=s; self.t=t
 def __enter__(self): return self.s
 def __exit__(self,*_): self.s.duration_ms=(perf_counter()-self.t)*1000
