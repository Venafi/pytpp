from datetime import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class Counter:
    a_name: str
    b_name: str
    c_name: str
    description: str
    name: str
    stats_type: int


@dataclass
class Result:
    key: 'Key'
    value: 'List[Value]'


@dataclass
class Key:
    m_item1: str
    m_item2: str
    m_item3: str


@dataclass
class Value:
    count: int
    sum_value: int
    tag_a: str
    tag_b: str
    tag_c: str
    time_frame: datetime
    type: int
