from __future__ import annotations
from pytpp.api.websdk.models.resultcodes import ResultCodes
from pytpp.api.api_base import ObjectModel, ApiField


class Result(ObjectModel):
    code: int = ApiField()

    @property
    def secret_store_result(self) -> str:
        return ResultCodes.SecretStore.get(self.code, 'Unknown')


class TypedNameValues(ObjectModel):
    name: str = ApiField(alias='Name')
    type: str = ApiField(alias='Type')
    value: str = ApiField(alias='Value')
