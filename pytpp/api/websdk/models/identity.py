from __future__ import annotations
from pytpp.api.api_base import ObjectModel, ApiField


class Identity(ObjectModel):
    full_name: str = ApiField(alias='FullName')
    is_container: bool = ApiField(alias='IsContainer')
    is_group: bool = ApiField(alias='IsGroup')
    name: str = ApiField(alias='Name')
    prefix: str = ApiField(alias='Prefix')
    prefixed_name: str = ApiField(alias='PrefixedName')
    prefixed_universal: str = ApiField(alias='PrefixedUniversal')
    type: int = ApiField(alias='Type')
    universal: str = ApiField(alias='Universal')

    @property
    def is_user(self):
        return self.type & 1 == 1

    @property
    def is_security_group(self):
        return self.type & 2 == 2

    @property
    def is_distribution_group(self):
        return self.type & 8 == 8


class InvalidIdentity(ObjectModel):
    prefix: str = ApiField(alias='Prefix')
    prefixed_name: str = ApiField(alias='PrefixedName')
    prefixed_universal: str = ApiField(alias='PrefixedUniversal')
    universal: str = ApiField(alias='Universal')
