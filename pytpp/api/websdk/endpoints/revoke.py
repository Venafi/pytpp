from pytpp.api.api_base import API, APIResponse


class _Revoke:
    def __init__(self, api_obj):
        self.Token = self._Token(api_obj=api_obj)

    class _Token(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Revoke/Token')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def get(self):
            response = APIResponse(response=self._get())
            # Set this to None to avoid erroneous re-authentication.
            self._api_obj._token = None
            return response
