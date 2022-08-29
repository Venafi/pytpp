from typing import List, Union
from pytpp.api.websdk.models import config, metadata
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Metadata(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Metadata')
        self.DefineItem = self._DefineItem(api_obj=self._api_obj, url=f'{self._url}/DefineItem')
        self.Find = self._Find(api_obj=self._api_obj, url=f'{self._url}/Find')
        self.FindItem = self._FindItem(api_obj=self._api_obj, url=f'{self._url}/FindItem')
        self.Get = self._Get(api_obj=self._api_obj, url=f'{self._url}/Get')
        self.GetItemGuids = self._GetItemGuids(api_obj=self._api_obj, url=f'{self._url}/GetItemGuids')
        self.GetItems = self._GetItems(api_obj=self._api_obj, url=f'{self._url}/GetItems')
        self.GetItemsForClass = self._GetItemsForClass(api_obj=self._api_obj, url=f'{self._url}/GetItemsForClass')
        self.GetPolicyItems = self._GetPolicyItems(api_obj=self._api_obj, url=f'{self._url}/GetPolicyItems')
        self.Items = self._Items(api_obj=self._api_obj, url=f'{self._url}/Items')
        self.LoadItem = self._LoadItem(api_obj=self._api_obj, url=f'{self._url}/LoadItem')
        self.LoadItemGuid = self._LoadItemGuid(api_obj=self._api_obj, url=f'{self._url}/LoadItemGuid')
        self.ReadEffectiveValues = self._ReadEffectiveValues(api_obj=self._api_obj, url=f'{self._url}/ReadEffectiveValues')
        self.ReadPolicy = self._ReadPolicy(api_obj=self._api_obj, url=f'{self._url}/ReadPolicy')
        self.Set = self._Set(api_obj=self._api_obj, url=f'{self._url}/Set')
        self.SetPolicy = self._SetPolicy(api_obj=self._api_obj, url=f'{self._url}/SetPolicy')
        self.UndefineItem = self._UndefineItem(api_obj=self._api_obj, url=f'{self._url}/UndefineItem')
        self.UpdateItem = self._UpdateItem(api_obj=self._api_obj, url=f'{self._url}/UpdateItem')

    class _DefineItem(WebSdkEndpoint):
        def post(self, item: Union[dict, metadata.Item]):
            body = {
                'Item': item
            }

            class Output(WebSdkOutputModel):
                dn: str = ApiField(alias='DN')
                item: metadata.Item = ApiField(alias='Item')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Find(WebSdkEndpoint):
        def post(self, item: str = None, item_guid: str = None, value: str = None):
            body = {
                'Item'    : item,
                'ItemGuid': item_guid,
                'Value'   : value
            }

            class Output(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                objects: List[config.Object] = ApiField(default_factory=list, alias='Objects')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _FindItem(WebSdkEndpoint):
        def post(self, name: str):
            body = {
                'Name': name
            }

            class Output(WebSdkOutputModel):
                item_guid: str = ApiField(alias='ItemGuid')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Get(WebSdkEndpoint):
        def post(self, dn: str, all_included: bool = None):
            body = {
                'DN' : dn,
                'All': all_included
            }

            class Output(WebSdkOutputModel):
                data: metadata.Data = ApiField(alias='Data')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetItemGuids(WebSdkEndpoint):
        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Output(WebSdkOutputModel):
                item_guids: List[str] = ApiField(default_factory=list, alias='ItemGuids')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetItems(WebSdkEndpoint):
        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Output(WebSdkOutputModel):
                items: List[metadata.Item] = ApiField(default_factory=list, alias='Items')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetItemsForClass(WebSdkEndpoint):
        def post(self, config_class: str):
            body = {
                'ConfigClass': config_class
            }

            class Output(WebSdkOutputModel):
                items: List[metadata.Item] = ApiField(default_factory=list, alias='Items')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetPolicyItems(WebSdkEndpoint):
        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Output(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                policy_items: List[metadata.PolicyItem] = ApiField(default_factory=list, alias='PolicyItems')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Items(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                items: List[metadata.Item] = ApiField(default_factory=list, alias='Items')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._get())

    class _LoadItem(WebSdkEndpoint):
        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Output(WebSdkOutputModel):
                item: metadata.Item = ApiField(alias='Item')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _LoadItemGuid(WebSdkEndpoint):
        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class Output(WebSdkOutputModel):
                item_guid: str = ApiField(alias='ItemGuid')
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _ReadEffectiveValues(WebSdkEndpoint):
        def post(self, dn: str, item_guid: str):
            body = {
                'DN'      : dn,
                'ItemGuid': item_guid
            }

            class Output(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                policy_dn: str = ApiField(alias='PolicyDn')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))
                values: List[str] = ApiField(default_factory=list, alias='Values')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _ReadPolicy(WebSdkEndpoint):
        def post(self, dn: str, item_guid: str, obj_type: str):
            body = {
                'DN'      : dn,
                'ItemGuid': item_guid,
                'Type'    : obj_type
            }

            class Output(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))
                values: List[str] = ApiField(default_factory=list, alias='Values')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Set(WebSdkEndpoint):
        def post(self, dn: str, guid_data: List[metadata.GuidData], keep_existing: bool = False):
            body = {
                'DN'          : dn,
                'GuidData'    : guid_data,
                'KeepExisting': keep_existing
            }

            class Output(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _SetPolicy(WebSdkEndpoint):
        def post(self, dn: str, config_class: str, guid_data: List[metadata.GuidData], locked: bool = False):
            body = {
                'DN'         : dn,
                'ConfigClass': config_class,
                'GuidData'   : guid_data,
                'Locked'     : locked
            }

            class Output(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _UndefineItem(WebSdkEndpoint):
        def post(self, item_guid: str, remove_data: bool = True):
            body = {
                'ItemGuid'  : item_guid,
                'RemoveData': remove_data
            }

            class Output(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _UpdateItem(WebSdkEndpoint):
        def post(self, item: Union[dict, metadata.Item] = None, update: Union[dict, metadata.Update] = None):
            body = {
                'ItemGuid': item,
                'Update'  : update
            }

            class Output(WebSdkOutputModel):
                locked: bool = ApiField(alias='Locked')
                result: metadata.Result = ApiField(alias='Result', converter=lambda x: metadata.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))
