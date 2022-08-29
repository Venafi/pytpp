from typing import List
from pytpp.api.websdk.models import preferences as prefs
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Preferences(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Preferences')

    def get(self, category: str = None, name: str = None, product: prefs.ProductType = None):
        params = {
            'Category': category,
            'Name'    : name,
            'Product' : product
        }

        class Output(WebSdkOutputModel):
            preferences: List[prefs.Preference] = ApiField(alias='Preferences', default_factory=list)

        return generate_output(output_cls=Output, response=self._get(params=params))

    def post(self, preferences: List[prefs.Preference]):
        body = {
            'Preferences': preferences
        }

        return generate_output(output_cls=WebSdkOutputModel, response=self._post(data=body))

    def delete(self, category: str = None, name: str = None, product: prefs.ProductType = None):
        params = {
            'Category': category,
            'Name'    : name,
            'Product' : product
        }

        return generate_output(output_cls=WebSdkOutputModel, response=self._delete(params=params))
