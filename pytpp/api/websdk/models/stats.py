from __future__ import annotations
from pytpp.api.api_base import ObjectModel, ApiField
from datetime import datetime
from typing import List


class Counter(ObjectModel):
    a_name: str = ApiField(alias='AName')
    b_name: str = ApiField(alias='BName')
    c_name: str = ApiField(alias='CName')
    description: str = ApiField(alias='Description')
    name: str = ApiField(alias='Name')
    stats_type: int = ApiField(alias='StatsType')
    value_description: str = ApiField(alias='ValueDescription')


class Key(ObjectModel):
    m_item1: str = ApiField(alias='MItem1')
    m_item2: str = ApiField(alias='MItem2')
    m_item3: str = ApiField(alias='MItem3')


class Value(ObjectModel):
    count: int = ApiField(alias='Count')
    sum_value: int = ApiField(alias='SumValue')
    tag_a: str = ApiField(alias='TagA')
    tag_b: str = ApiField(alias='TagB')
    tag_c: str = ApiField(alias='TagC')
    time_frame: datetime = ApiField(alias='TimeFrame')
    type: int = ApiField(alias='Type')


class Result(ObjectModel):
    key: Key = ApiField(alias='Key')
    value: List[Value] = ApiField(alias='Value', default_factory=list)
