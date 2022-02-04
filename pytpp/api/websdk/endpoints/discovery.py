from typing import List 
from pytpp.api.api_base import API, APIResponse, api_response_property


class _Discovery:
    def __init__(self, api_obj):
        self._api_obj = api_obj
        self.Import = self._Import(api_obj=api_obj)

    def Guid(self, guid: str):
        return self._Guid(guid=guid, api_obj=self._api_obj)

    class _Guid(API):
        def __init__(self, guid: str, api_obj):
            super().__init__(api_obj=api_obj, url=f'/Discovery/{guid}')

        def delete(self):
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json('Success')

            return _Response(response=self._delete())

    class _Import(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Discovery/Import')

        def post(self, endpoints: list, zone_name: str):
            body = {
                'zoneName': zone_name,
                'endpoints': endpoints
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def created_certificates(self) -> int:
                    return self._from_json('createdCertificates')

                @property
                @api_response_property()
                def created_instances(self) -> int:
                    return self._from_json('createdInstances')

                @property
                @api_response_property()
                def updated_certificates(self) -> int:
                    return self._from_json('updatedCertificates')

                @property
                @api_response_property()
                def updated_instances(self) -> int:
                    return self._from_json('updatedInstances')

                @property
                @api_response_property()
                def warnings(self) -> List[str]:
                    return self._from_json('warnings')

                @property
                @api_response_property()
                def zone_name(self) -> str:
                    return self._from_json('zoneName')

            return _Response(response=self._post(data=body))

