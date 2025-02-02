from dataclasses import dataclass
from typing import List, Optional

@dataclass
class LPProblem:
    c: List[float]
    A: List[List[float]]
    b: List[float]
    sense: Optional[str] = None

