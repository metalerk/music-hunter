from dataclasses import dataclass


@dataclass
class Artist:
    """ Artist dataclass """
    id: str
    name: str
    real_name: str
    images: str
    profile: str
