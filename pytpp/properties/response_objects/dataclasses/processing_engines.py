from dataclasses import dataclass


@dataclass
class Engine:
    links: 'Link'
    engine_dn: str
    engine_guid: str
    engine_name: str


@dataclass
class Folder:
    folder_dn: str
    folder_guid: str
    folder_name: str


@dataclass
class Link:
    self: 'Self'


@dataclass
class Self:
    href: str
