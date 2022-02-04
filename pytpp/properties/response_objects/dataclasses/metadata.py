from dataclasses import dataclass
from typing import List


@dataclass
class Result:
    code: int
    metadata_result: str


@dataclass
class Item:
    allowed_characters: str
    allowed_values: str
    category: str
    classes: list
    config_attribute: str
    date_only: bool
    default_values: str
    display_after: str
    dn: str
    error_message: str
    guid: str
    help: str
    label: str
    localization_table: str
    localized_help: str
    localized_label: str
    localized_set: str
    mandatory: bool
    name: str
    mask: str
    maximum_length: int
    minimum_length: int
    policyable: bool
    regular_expression: str
    render_hidden: bool
    render_read_only: bool
    single: bool
    time_only: bool
    type: int


@dataclass
class Data:
    key: 'Item'
    value: list


@dataclass
class PolicyItem:
    key: str
    value: 'List[Item]'
