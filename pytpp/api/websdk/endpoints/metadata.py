from typing import List 
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.metadata import Metadata
from pytpp.properties.response_objects.config import Config


class _Metadata(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Log')
        self.DefineItem = self._DefineItem(api_obj=api_obj)
        self.Find = self._Find(api_obj=api_obj)
        self.FindItem = self._FindItem(api_obj=api_obj)
        self.Get = self._Get(api_obj=api_obj)
        self.GetItemGuids = self._GetItemGuids(api_obj=api_obj)
        self.GetItems = self._GetItems(api_obj=api_obj)
        self.GetItemsForClass = self._GetItemsForClass(api_obj=api_obj)
        self.GetPolicyItems = self._GetPolicyItems(api_obj=api_obj)
        self.Items = self._Items(api_obj=api_obj)
        self.LoadItem = self._LoadItem(api_obj=api_obj)
        self.LoadItemGuid = self._LoadItemGuid(api_obj=api_obj)
        self.ReadEffectiveValues = self._ReadEffectiveValues(api_obj=api_obj)
        self.ReadPolicy = self._ReadPolicy(api_obj=api_obj)
        self.Set = self._Set(api_obj=api_obj)
        self.SetPolicy = self._SetPolicy(api_obj=api_obj)
        self.UndefineItem = self._UndefineItem(api_obj=api_obj)
        self.UpdateItem = self._UpdateItem(api_obj=api_obj)

    class _DefineItem(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/DefineItem')

        def post(self, item: dict):
            body = {
                'Item': item
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def dn(self) -> str:
                    return self._from_json('DN')

                @property
                @api_response_property()
                def item(self):
                    return Metadata.Item(self._from_json('Item'))

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _Find(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/Find')

        def post(self, item: str = None, item_guid: str = None, value: str = None):
            body = {
                'Item': item,
                'ItemGuid': item_guid,
                'Value': value
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def objects(self):
                    return [Config.Object(obj) for obj in self._from_json('Objects')]

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _FindItem(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/FindItem')

        def post(self, name: str):
            body = {
                'Name': name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def item_guid(self) -> str:
                    return self._from_json('ItemGuid')

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _Get(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/Get')

        def post(self, dn: str, all_included: bool = None):
            body = {
                'DN': dn,
                'All': all_included
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def data(self):
                    return [Metadata.Data(self._from_json('Data'))]

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _GetItemGuids(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/GetItemGuids')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def item_guids(self) -> List[str]:
                    return self._from_json('ItemGuids')

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _GetItems(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/GetItems')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def items(self):
                    return [Metadata.Item(item) for item in self._from_json('Items')]

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _GetItemsForClass(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/GetItemsForClass')

        def post(self, config_class: str):
            body = {
                'ConfigClass': config_class
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def items(self):
                    return [Metadata.Item(item) for item in self._from_json('Items')]

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _GetPolicyItems(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/GetPolicyItems')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def policy_items(self):
                    return [Metadata.PolicyItem(item) for item in self._from_json('PolicyItems')]

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _Items(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/Items')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def items(self):
                    return [Metadata.Item(item) for item in self._from_json('Items')]

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._get())

    class _LoadItem(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/LoadItem')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def item(self):
                    return Metadata.Item(self._from_json('Item'))

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _LoadItemGuid(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/LoadItemGuid')

        def post(self, dn: str):
            body = {
                'DN': dn
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def item_guid(self) -> str:
                    return self._from_json('ItemGuid')

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _ReadEffectiveValues(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/ReadEffectiveValues')

        def post(self, dn: str, item_guid: str):
            body = {
                'DN': dn,
                'ItemGuid': item_guid
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def policy_dn(self) -> str:
                    return self._from_json('PolicyDn')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

                @property
                @api_response_property()
                def values(self) -> List[str]:
                    return self._from_json('Values')

            return _Response(response=self._post(data=body))

    class _ReadPolicy(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/ReadPolicy')

        def post(self, dn: str, item_guid: str, obj_type: str):
            body = {
                'DN': dn,
                'ItemGuid': item_guid,
                'Type': obj_type
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

                @property
                @api_response_property()
                def values(self) -> List[str]:
                    return self._from_json('Values')

            return _Response(response=self._post(data=body))

    class _Set(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/Set')

        def post(self, dn: str, guid_data: list, keep_existing: bool = False):
            body = {
                'DN': dn,
                'GuidData': guid_data,
                'KeepExisting': keep_existing
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _SetPolicy(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/SetPolicy')

        def post(self, dn: str, config_class: str, guid_data: list, locked: bool = False):
            body = {
                'DN': dn,
                'ConfigClass': config_class,
                'GuidData': guid_data,
                'Locked': locked
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _UndefineItem(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/UndefineItem')

        def post(self, item_guid: str, remove_data: bool = True):
            body = {
                'ItemGuid': item_guid,
                'RemoveData': remove_data
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))

    class _UpdateItem(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Metadata/UpdateItem')

        def post(self, item: dict = None, update: dict = None):
            body = {
                'ItemGuid': item,
                'Update': update
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def locked(self) -> bool:
                    return self._from_json('Locked')

                @property
                @api_response_property()
                def result(self):
                    return Metadata.Result(self._from_json('Result'))

            return _Response(response=self._post(data=body))
