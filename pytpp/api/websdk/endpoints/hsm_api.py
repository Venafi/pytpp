from pytpp.api.api_base import API, APIResponse, api_response_property


class _HSMAPI:
    def __init__(self, api_obj):
        self.Sign = self._Sign(api_obj=api_obj)
        self.SignJWT = self._SignJWT(api_obj=api_obj)
        self.GetGPGPublicKey = self._GetGPGPublicKey(api_obj=api_obj)

    class _Sign(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='API/Sign')
            self._url = self._url.replace('vedsdk', 'vedhsm')

        def post(self, client_info: dict, data: str, key_context: str, key_id: int, mechanism: int,
                 process_info: dict, client_mechanism: str = None, justification: str = None,
                 key_context_to_wrap: int = None, key_id_to_wrap: int = None, parameter: dict = None,
                 password: str = None, username: str = None, verify_data: bool = None,
                 wrapping_key_id: int = None):
            body = {
                'ClientInfo': client_info,
                'ClientMechanism': client_mechanism,
                'Data': data,
                'Justification': justification,
                'KeyContext': key_context,
                'KeyContextToWrap': key_context_to_wrap,
                'KeyId': key_id,
                'KeyIdToWrap': key_id_to_wrap,
                'Mechanism': mechanism,
                'Parameter': parameter,
                'Password': password,
                'ProcessInfo': process_info,
                'Username': username,
                'VerifyData': verify_data,
                'WrappingKeyId': wrapping_key_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result_data(self) -> str:
                    return self._from_json(key='ResultData')

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

                @property
                @api_response_property()
                def try_later(self) -> bool:
                    return self._from_json(key='TryLater')

            return _Response(response=self._post(data=body))

    class _SignJWT(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='API/SignJWT')
            self._url = self._url.replace('vedsdk', 'vedhsm')

        def post(self, client_info: dict, process_info: dict, key_id: str,
                 header: str, payload: str):
            body = {
                'ClientInfo': client_info,
                'ProcessInfo': process_info,
                'KeyId': key_id,
                'Header': header,
                'Payload': payload
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result_data(self) -> str:
                    return self._from_json(key='ResultData')

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(response=self._post(data=body))

    class _GetGPGPublicKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='API/GetGPGPublicKey')
            self._url = self._url.replace('vedsdk', 'vedhsm')

        def post(self, key_id: str, key_context: str = None):
            body = {
                'KeyId':key_id,
                'KeyContext': key_context
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def fingerprint(self) -> str:
                    return self._from_json(key='Fingerprint')

                @property
                @api_response_property()
                def location(self) -> str:
                    return self._from_json(key='Location')

                @property
                @api_response_property()
                def public_key(self) -> str:
                    return self._from_json(key='PublicKey')

                @property
                @api_response_property()
                def success(self) -> bool:
                    return self._from_json(key='Success')

            return _Response(response=self._post(data=body))

