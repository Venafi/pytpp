from __future__ import annotations
from pytpp.api.api_base import ObjectModel, ApiField


class Permissions(ObjectModel):
    delete: bool = ApiField(alias='Delete')
    discover: bool = ApiField(alias='Discover')
    manage: bool = ApiField(alias='Manage')
    read: bool = ApiField(alias='Read')
    revoke: bool = ApiField(alias='Revoke')
