from __future__ import annotations
from pytpp.api.api_base import ObjectModel, ApiField


class Self(ObjectModel):
    href: str = ApiField(alias='Href')


class Link(ObjectModel):
    self: Self = ApiField(alias='Self')


class Engine(ObjectModel):
    links: Link = ApiField(alias='_links')
    engine_dn: str = ApiField(alias='EngineDn')
    engine_guid: str = ApiField(alias='EngineGuid')
    engine_name: str = ApiField(alias='EngineName')


class Folder(ObjectModel):
    folder_dn: str = ApiField(alias='FolderDN')
    folder_guid: str = ApiField(alias='FolderGuid')
    folder_name: str = ApiField(alias='FolderName')
