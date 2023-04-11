from typing import Optional
from dataclasses import dataclass, asdict


@dataclass
class RedisSettings:
    host: str
    port: int
    db: Optional[int]
    
    def dict(self):
        return {f'redis__{k}': str(v) for k, v in asdict(self).items()}
