from pytpp.api.websdk.models import recycle_bin
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField
from typing import List, Union


class _RecycleBin(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/RecycleBin')
        self.DeletionTask = self._DeletionTask(api_obj=self._api_obj, url=f'{self._url}/DeletionTask')
        self.Empty = self._Empty(api_obj=self._api_obj, url=f'{self._url}/Empty')
        self.GetConfiguration = self._GetConfiguration(api_obj=self._api_obj, url=f'{self._url}/GetConfiguration')
        self.GetContents = self._GetContents(api_obj=self._api_obj, url=f'{self._url}/GetContents')
        self.GetItem = self._GetItem(api_obj=self._api_obj, url=f'{self._url}/GetItem')
        self.Purge = self._Purge(api_obj=self._api_obj, url=f'{self._url}/Purge')
        self.PurgeTask = self._PurgeTask(api_obj=self._api_obj, url=f'{self._url}/PurgeTask')
        self.Restore = self._Restore(api_obj=self._api_obj, url=f'{self._url}/Restore')
        self.SetConfiguration = self._SetConfiguration(api_obj=self._api_obj, url=f'{self._url}/SetConfiguration')

    class _DeletionTask(WebSdkEndpoint):
        def post(self, start: bool = None, stop: bool = None):
            body = {
                'Start': start,
                'Stop' : stop
            }

            class Output(WebSdkOutputModel):
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Empty(WebSdkEndpoint):
        def post(self):
            class Output(WebSdkOutputModel):
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data={}))

    class _GetConfiguration(WebSdkEndpoint):
        def post(self):
            class Output(WebSdkOutputModel):
                deletion: recycle_bin.Deletion = ApiField(alias='Deletion')
                purge: recycle_bin.Purge = ApiField(alias='Purge')
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data={}))

    class _GetContents(WebSdkEndpoint):
        def post(self, limit: int):
            body = {
                'Limit': limit
            }

            class Output(WebSdkOutputModel):
                items: List[recycle_bin.Item] = ApiField(alias='Items', default_factory=list)
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))
                total: int = ApiField(alias='Total')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetItem(WebSdkEndpoint):
        def post(self, guid: str):
            body = {
                'Guid': guid
            }

            class Output(WebSdkOutputModel):
                item: recycle_bin.Item = ApiField(alias='Item')
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Purge(WebSdkEndpoint):
        def post(self, guid: str):
            body = {
                'Guid': guid
            }

            class Output(WebSdkOutputModel):
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _PurgeTask(WebSdkEndpoint):
        def post(self, purge_all: bool, start: bool = None, stop: bool = None):
            body = {
                'PurgeAll': purge_all,
                'Start'   : start,
                'Stop'    : stop
            }

            class Output(WebSdkOutputModel):
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Restore(WebSdkEndpoint):
        def post(self, guid: str):
            body = {
                'Guid': guid
            }

            class Output(WebSdkOutputModel):
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _SetConfiguration(WebSdkEndpoint):
        def post(self, deletion: Union[dict, recycle_bin.Deletion], purge: Union[dict, recycle_bin.Purge] = None):
            body = {
                'Deletion': deletion,
                'Purge'   : purge
            }

            class Output(WebSdkOutputModel):
                result: recycle_bin.Result = ApiField(alias='Result', converter=lambda x: recycle_bin.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))
