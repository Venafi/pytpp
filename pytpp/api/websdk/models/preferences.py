from __future__ import annotations
from pytpp.api.api_base import ObjectModel, ApiField
from typing import Literal

ProductType = Literal[
    'CodeSign Protect',
    'Client Protect',
    'Platform',
    'SSH Protect',
    'TLS Protect',
]


class Preference(ObjectModel):
    id: int = ApiField(alias='Id')
    universal: str = ApiField(alias='Universal')
    product: str = ApiField(alias='Product')
    category: str = ApiField(alias='Category')
    name: str = ApiField(alias='Name')
    value: str = ApiField(alias='Value')
    locked: bool = ApiField(alias='Locked')
