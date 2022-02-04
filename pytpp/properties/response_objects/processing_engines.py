from pytpp.properties.response_objects.dataclasses import processing_engines


class ProcessingEngines:
    @staticmethod
    def Engine(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return processing_engines.Engine(
            links=ProcessingEngines.Link(response_object.get('_links')),
            engine_dn=response_object.get('EngineDN'),
            engine_guid=response_object.get('EngineGuid'),
            engine_name=response_object.get('EngineName'),
        )

    @staticmethod
    def Folder(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return processing_engines.Folder(
            folder_dn=response_object.get('FolderDN'),
            folder_guid=response_object.get('FolderGuid'),
            folder_name=response_object.get('FolderName'),
        )

    @staticmethod
    def Link(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return processing_engines.Link(
            self=ProcessingEngines.Self(response_object.get('self')),
        )

    @staticmethod
    def Self(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return processing_engines.Self(
            href=response_object.get('href'),
        )
