from __future__ import annotations
from datetime import datetime

from pytpp.api.websdk.models.resultcodes import ResultCodes
from pytpp.api.websdk.models.identity import Identity
from pytpp.api.api_base import ObjectModel, ApiField
from typing import List


class Result(ObjectModel):
    code: int = ApiField()

    @property
    def recycle_bin_result(self) -> str:
        return ResultCodes.RecycleBin.get(self.code, 'Unknown')


class Deletion(ObjectModel):
    allotted_time: int = ApiField(alias='AllottedTime')
    query_size: int = ApiField(alias='QuerySize')
    sql_timeout: int = ApiField(alias='SqlTimeout')
    tasks: List[str] = ApiField(alias='Tasks', default_factory=list)


class Item(ObjectModel):
    child_count: int = ApiField(alias='ChildCount')
    dn: str = ApiField(alias='DN')
    deleted_by: Identity = ApiField(alias='DeletedBy')
    deleted_on: datetime = ApiField(alias='DeletedOn')
    guid: str = ApiField(alias='Guid')
    name: str = ApiField(alias='Name')
    purge_on: datetime = ApiField(alias='PurgeOn')
    restoration_dn: str = ApiField(alias='RestorationDN')
    restore_state: int = ApiField(alias='RestoreState')
    type: str = ApiField(alias='Type')
    type_detail: str = ApiField(alias='TypeDetail')


class Purge(ObjectModel):
    after: int = ApiField(alias='After')
    allotted_time: int = ApiField(alias='AllottedTime')
    engine_dn: str = ApiField(alias='EngineDN')
