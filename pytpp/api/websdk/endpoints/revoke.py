from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output


class _Revoke(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Revoke')
        self._url = self._url.replace('vedsdk', 'vedauth')
        self.Token = self._Token(api_obj=self._api_obj, url=f'{self._url}/Token')

    class _Token(WebSdkEndpoint):
        def get(self):
            response = generate_output(output_cls=WebSdkOutputModel, response=self._get())
            # Set this to None to avoid erroneous re-authentication.
            self._api_obj._token = None
            return response
