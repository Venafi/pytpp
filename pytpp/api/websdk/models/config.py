from __future__ import annotations
from pytpp.api.api_base import ObjectModel, ApiField
from pytpp.api.websdk.models.resultcodes import ResultCodes
from typing import List, Optional, TypeVar, Generic

T = TypeVar('T')


# region Models
# region Outputs
class Result(ObjectModel):
    code: int = ApiField()

    @property
    def config_result(self):
        return ResultCodes.Config.get(self.code, 'Unknown')


class NameValues(ObjectModel, Generic[T]):
    name: str = ApiField(alias='Name')
    values: List[T] = ApiField(alias='Values', default_factory=list)


class Object(ObjectModel):
    absolute_guid: str = ApiField(alias='AbsoluteGUID')
    dn: str = ApiField(alias='DN')
    guid: str = ApiField(alias='GUID')
    config_id: Optional[int] = ApiField(alias='Id')
    name: str = ApiField(alias='Name')
    parent: str = ApiField(alias='Parent')
    revision: Optional[int] = ApiField(alias='Revision')
    type_name: str = ApiField(alias='TypeName')

    def __str__(self):
        return self.dn


class Policy(ObjectModel):
    attribute_name: str = ApiField(alias='AttributeName')
    guid: str = ApiField(alias='GUID')
    property: str = ApiField(alias='Property')
    type_name: str = ApiField(alias='TypeName')
    value_list: List[str] = ApiField(alias='ValueList', default_factory=list)


# endregion Outputs


# region Inputs
class NameAttribute(ObjectModel, Generic[T]):
    name: str = ApiField(alias='Name')
    value: T = ApiField(alias='Value')
# endregion Inputs
# endregion Models
