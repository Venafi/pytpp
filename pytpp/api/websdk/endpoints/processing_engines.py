from typing import List
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.processing_engines import ProcessingEngines


class _ProcessingEngines(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/ProcessingEngines')

        self.Engine = self._Engine(api_obj=api_obj)
        self.Folder = self._Folder(api_obj=api_obj)

    def get(self):
        class _Response(APIResponse):
            def __init__(self, response):
                super().__init__(response=response)

            @property
            @api_response_property()
            def engines(self):
                return [ProcessingEngines.Engine(engine) for engine in self._from_json('Engines')]

        return _Response(response=self._get())

    class _Engine:
        def __init__(self, api_obj):
            self._api_obj = api_obj

        def Guid(self, guid: str):
            return self._Guid(guid=guid, api_obj=self._api_obj)

        class _Guid(API):
            def __init__(self, guid: str, api_obj):
                super().__init__(api_obj=api_obj, url=f'/ProcessingEngines/Engine/{guid}')

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property(return_on_204=list)
                    def folders(self):
                        return [ProcessingEngines.Folder(folder) for folder in self._from_json('Folders')][0]

                return _Response(response=self._get())

            def post(self, folder_guids: list):
                body = {
                    'FolderGuids': folder_guids
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response) \

                    @property
                    @api_response_property(return_on_204=str)
                    def added_count(self) -> int:
                        return self._from_json('AddedCount')

                    @property
                    @api_response_property(return_on_204=list)
                    def errors(self) -> List[str]:
                        return self._from_json('Errors')

                return _Response(response=self._post(data=body))

    class _Folder:
        def __init__(self, api_obj):
            self._api_obj = api_obj

        def Guid(self, guid: str):
            return self._Guid(guid=guid, api_obj=self._api_obj)

        class _Guid(API):
            def __init__(self, guid: str, api_obj):
                super().__init__(api_obj=api_obj, url=f'/ProcessingEngines/Folder/{guid}')
                self._folder_guid = guid

            def delete(self):
                return APIResponse(response=self._delete())

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property(return_on_204=list)
                    def engines(self):
                        return [ProcessingEngines.Engine(engine) for engine in self._from_json('Engines')]

                return _Response(response=self._get())

            def put(self, engine_guids: list):
                body = {
                    'EngineGuids': engine_guids
                }

                return APIResponse(response=self._put(data=body))

            def EngineGuid(self, guid):
                return self._EngineGuid(guid=self._folder_guid, engine_guid=guid, api_obj=self._api_obj)

            class _EngineGuid(API):
                def __init__(self, guid: str, engine_guid: str, api_obj):
                    super().__init__(api_obj=api_obj, url=f'/ProcessingEngines/Folder/{guid}/{engine_guid}')

                def delete(self):
                    return APIResponse(response=self._delete())
