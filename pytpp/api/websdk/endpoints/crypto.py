from typing import List
from pytpp.api.api_base import API, APIResponse, api_response_property


class _Crypto:
    def __init__(self, api_obj):
        self.AvailableKeys = self._AvailableKeys(api_obj=api_obj)
        self.DefaultKey = self._DefaultKey(api_obj=api_obj)

    class _AvailableKeys(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Crypto/AvailableKeys')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def keynames(self) -> List[str]:
                    return self._from_json('Keynames')

            return _Response(response=self._get())

    class _DefaultKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Crypto/DefaultKey')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def default_key(self) -> str:
                    return self._from_json('DefaultKey')

            return _Response(response=self._get())
