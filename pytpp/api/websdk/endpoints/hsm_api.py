from typing import List, Union
from pytpp.api.websdk.models import hsm_api
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _HSMAPI(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/API')
        self._url = self._url.replace('vedsdk', 'vedhsm')
        self.Sign = self._Sign(api_obj=self._api_obj, url=f'{self._url}/Sign')
        self.SignJWT = self._SignJWT(api_obj=self._api_obj, url=f'{self._url}/SignJWT')
        self.GetGPGPublicKey = self._GetGPGPublicKey(api_obj=self._api_obj, url=f'{self._url}/GetGPGPublicKey')
        self.GetObjects = self._GetObjects(api_obj=self._api_obj, url=f'{self._url}/GetObjects')

    class _Sign(WebSdkEndpoint):
        def post(self, client_info: Union[dict, hsm_api.ClientInfo], data: str, key_context: str, key_id: int, mechanism: int,
                 process_info: Union[dict, hsm_api.ProcessInfo], client_mechanism: str = None, justification: str = None,
                 key_context_to_wrap: int = None, key_id_to_wrap: int = None, parameter: Union[dict, hsm_api.Parameter] = None,
                 password: str = None, username: str = None, verify_data: bool = None,
                 wrapping_key_id: int = None):
            body = {
                'ClientInfo'      : client_info,
                'ClientMechanism' : client_mechanism,
                'Data'            : data,
                'Justification'   : justification,
                'KeyContext'      : key_context,
                'KeyContextToWrap': key_context_to_wrap,
                'KeyId'           : key_id,
                'KeyIdToWrap'     : key_id_to_wrap,
                'Mechanism'       : mechanism,
                'Parameter'       : parameter,
                'Password'        : password,
                'ProcessInfo'     : process_info,
                'Username'        : username,
                'VerifyData'      : verify_data,
                'WrappingKeyId'   : wrapping_key_id
            }

            class Output(WebSdkOutputModel):
                result_data: str = ApiField(alias='ResultData')
                success: bool = ApiField(alias='Success')
                try_later: bool = ApiField(alias='TryLater')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _SignJWT(WebSdkEndpoint):
        def post(self, client_info: Union[dict, hsm_api.ClientInfo], process_info: Union[dict, hsm_api.ProcessInfo], key_id: str,
                 header: str, payload: str):
            body = {
                'ClientInfo' : client_info,
                'ProcessInfo': process_info,
                'KeyId'      : key_id,
                'Header'     : header,
                'Payload'    : payload
            }

            class Output(WebSdkOutputModel):
                result_data: str = ApiField(alias='ResultData')
                success: bool = ApiField(alias='Success')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetGPGPublicKey(WebSdkEndpoint):
        def post(self, key_id: str, key_context: str = None):
            body = {
                'KeyId'     : key_id,
                'KeyContext': key_context
            }

            class Output(WebSdkOutputModel):
                fingerprint: str = ApiField(alias='Fingerprint')
                location: str = ApiField(alias='Location')
                public_key: str = ApiField(alias='PublicKey')
                success: bool = ApiField(alias='Success')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _GetObjects(WebSdkEndpoint):
        def post(self, environment_filter: List[int] = None, include_chains: bool = None, include_archived: bool = None,
                 key_id: str = None, key_context: str = None, object_type_filter: List[int] = None):
            body = {
                'EnvironmentFilter': environment_filter,
                'IncludeChains'    : include_chains,
                'IncludeArchived'  : include_archived,
                'KeyId'            : key_id,
                'KeyContext'       : key_context,
                'ObjectTypeFilter' : object_type_filter,
            }

            class Output(WebSdkOutputModel):
                certificates: List[hsm_api.Certificate] = ApiField(alias='Certificates', default_factory=list)
                pending: bool = ApiField(alias='Pending')
                private_keys: List[hsm_api.PrivateKey] = ApiField(alias='PrivateKeys', default_factory=list)
                public_keys: List[hsm_api.PublicKey] = ApiField(alias='PublicKeys', default_factory=list)
                success: bool = ApiField(alias='Success')

            return generate_output(output_cls=Output, response=self._post(data=body))
