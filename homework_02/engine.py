"""
create dataclass `Engine`
"""
from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class Engine:
    volume: int
    pistons: int


