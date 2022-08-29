from typing import List
from pytpp.api.websdk.models import processing_engines
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _ProcessingEngines(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/ProcessingEngines')
        self.Engine = self._Engine(api_obj=api_obj, url=f'{self._url}/Engine')
        self.Folder = self._Folder(api_obj=api_obj, url=f'{self._url}/Folder')

    def get(self):
        class Output(WebSdkOutputModel):
            engines: List[processing_engines.Engine] = ApiField(alias='Engines', default_factory=list)

        return generate_output(output_cls=Output, response=self._get())

    class _Engine(WebSdkEndpoint):
        def Guid(self, guid: str):
            return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

        class _Guid(WebSdkEndpoint):
            def get(self):
                class Output(WebSdkOutputModel):
                    links: processing_engines.Link = ApiField(alias='_links')
                    folders: List[processing_engines.Folder] = ApiField(alias='Folders', default_factory=list)

                return generate_output(output_cls=Output, response=self._get())

            def post(self, folder_guids: List[str]):
                body = {
                    'FolderGuids': folder_guids
                }

                class Output(WebSdkOutputModel):
                    added_count: int = ApiField(alias='AddedCount')
                    errors: List[str] = ApiField(alias='Errors', default_factory=list)

                return generate_output(output_cls=Output, response=self._post(data=body))

    class _Folder(WebSdkEndpoint):
        def Guid(self, guid: str):
            return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

        class _Guid(WebSdkEndpoint):
            def delete(self):
                return generate_output(output_cls=WebSdkOutputModel, response=self._delete())

            def get(self):
                class Output(WebSdkOutputModel):
                    links: processing_engines.Link = ApiField(alias='_links')
                    engines: List[processing_engines.Engine] = ApiField(alias='Engines', default_factory=list)

                return generate_output(output_cls=Output, response=self._get())

            def put(self, engine_guids: List[str]):
                body = {
                    'EngineGuids': engine_guids
                }

                return generate_output(output_cls=WebSdkOutputModel, response=self._put(data=body))

            def EngineGuid(self, guid):
                return self._EngineGuid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

            class _EngineGuid(WebSdkEndpoint):
                def delete(self):
                    return generate_output(output_cls=WebSdkOutputModel, response=self._delete())
