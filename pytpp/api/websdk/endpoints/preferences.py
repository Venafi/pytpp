from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.preferences import Preferences


class _Preferences(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Preferences')

    def get(self, category: str = None, name: str = None, product: str = None):
        params = {
            'Category': category,
            'Name': name,
            'Product': product
        }

        class _Response(APIResponse):
            def __init__(self, response):
                super().__init__(response=response)

            @property
            @api_response_property()
            def preferences(self):
                return [Preferences.Preference(p) for p in self._from_json(key='Preferences')]

        return _Response(response=self._get(params=params))

    def post(self, preferences: dict):
        body = {
            'Preferences': preferences
        }

        return APIResponse(response=self._post(data=body))

    def delete(self, category: str = None, name: str = None, product: str = None):
        params = {
            'Category': category,
            'Name': name,
            'Product': product
        }

        return APIResponse(response=self._delete(params=params))
