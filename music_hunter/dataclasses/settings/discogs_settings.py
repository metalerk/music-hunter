from typing import Optional
from dataclasses import dataclass, asdict


@dataclass
class DiscogsSettings:
    token: str
    user_agent: str
    
    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}
