from dataclasses import dataclass


@dataclass
class Permissions:
    delete: bool
    discover: bool
    manage: bool
    read: bool
    revoke: bool
