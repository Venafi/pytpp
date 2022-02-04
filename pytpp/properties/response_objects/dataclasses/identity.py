from dataclasses import dataclass


@dataclass
class Identity:
    full_name: str
    is_container: bool
    is_group: bool
    name: str
    prefix: str
    prefixed_name: str
    prefixed_universal: str
    type: str
    universal: str


@dataclass
class InvalidIdentity:
    prefix: str
    prefixed_name: str
    prefixed_universal: str
    universal: str
