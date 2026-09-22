from dataclasses import dataclass,field
from time import perf_counter
@dataclass(frozen=True)
class Span:name:str;duration_ms:float;attributes:dict[str,str]=field(default_factory=dict)
class Tracer:
 def __init__(self):self.spans=[]
 def record(self,name,fn,**attributes):
  start=perf_counter()
  try:return fn()
  finally:self.spans.append(Span(name,(perf_counter()-start)*1000,{str(k):str(v) for k,v in attributes.items()}))
