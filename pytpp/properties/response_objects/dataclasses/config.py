from dataclasses import dataclass
from typing import Optional


@dataclass
class Result:
    code: int
    config_result: str


@dataclass
class NameValues:
    name: str
    values: list


@dataclass
class Object:
    absolute_guid: str
    dn: str
    guid: str
    config_id: Optional[int]
    name: str
    parent: str
    revision: Optional[int]
    type_name: str


@dataclass
class Policy:
    attribute_name: str
    guid: str
    property: str
    type_name: str
    value_list: list
