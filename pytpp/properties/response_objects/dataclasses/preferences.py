from dataclasses import dataclass


@dataclass
class Preference:
    id: int
    universal: str
    product: str
    category: str
    name: str
    value: str
    locked: bool
