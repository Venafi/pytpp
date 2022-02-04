from dataclasses import dataclass


@dataclass
class Rights:
    checksum: str
    is_container: bool
    is_group: bool
    object: str
    principal: str
    rights: str
    sub_system: str
