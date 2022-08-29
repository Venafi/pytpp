from __future__ import annotations
from typing import List

from pytpp.api.websdk.models.resultcodes import ResultCodes
from pytpp.api.api_base import ObjectModel, ApiField


# region Models
class Result(ObjectModel):
    code: int = ApiField()

    @property
    def config_result(self) -> str:
        return ResultCodes.Config.get(self.code, 'Unknown')


class AttributeDefinition(ObjectModel):
    name: str = ApiField(alias='Name')
    property: int = ApiField(alias='Property')
    syntax: str = ApiField(alias='Syntax')


class ClassDefinition(ObjectModel):
    containment_names: List[str] = ApiField(alias='ContainmentNames', default_factory=list)
    containment_sub_names: List[str] = ApiField(alias='ContainmentSubNames', default_factory=list)
    mandatory_names: List[str] = ApiField(alias='MandatoryNames', default_factory=list)
    name: str = ApiField(alias='Name')
    naming_names: List[str] = ApiField(alias='NamingNames', default_factory=list)
    optional_names: List[str] = ApiField(alias='OptionalNames', default_factory=list)
    super_class_names: List[str] = ApiField(alias='SuperClassNames', default_factory=list)
