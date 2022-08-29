from typing import List
from pytpp.api.websdk.models import secret_store, certificate as cert
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _X509CertificateStore(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/X509CertificateStore')
        self.Add = self._Add(api_obj=self._api_obj, url=f'{self._url}/Add')
        self.Lookup = self._Lookup(api_obj=self._api_obj, url=f'{self._url}/Lookup')
        self.LookupExpiring = self._LookupExpiring(api_obj=self._api_obj, url=f'{self._url}/LookupExpiring')
        self.Remove = self._Remove(api_obj=self._api_obj, url=f'{self._url}/Remove')
        self.Retrieve = self._Retrieve(api_obj=self._api_obj, url=f'{self._url}/Retrieve')

    class _Add(WebSdkEndpoint):
        def post(self, owner_dn: str, certificate_collection_strings: List[str] = None, certificate_string: str = None,
                 protection_key: str = None, typed_name_values: List[cert.NameTypeValue] = None):
            body = {
                'CertificateCollectionStrings': certificate_collection_strings,
                'CertificateString'           : certificate_string,
                'OwnerDN'                     : owner_dn,
                'ProtectionKey'               : protection_key,
                'TypedNameValues'             : typed_name_values
            }

            class Output(WebSdkOutputModel):
                leaf_existed: bool = ApiField(alias='LeafExisted')
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_id: int = ApiField(alias='VaultId')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Lookup(WebSdkEndpoint):
        def post(self, certificate_string: str = None, name: str = None, owner_dn: str = None, value: str = None):
            body = {
                'CertificateString': certificate_string,
                'Name'             : name,
                'OwnerDN'          : owner_dn,
                'Value'            : value
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_id: int = ApiField(alias='VaultId')
                vault_ids: List[int] = ApiField(alias='VaultIds', default_factory=list)
                certificate_collection_strings: List[str] = ApiField(alias='CertificateCollectionStrings', default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _LookupExpiring(WebSdkEndpoint):
        def post(self, days_to_expiration: int, owner_dn: str):
            body = {
                'DaysToExpiration': days_to_expiration,
                'OwnerDN'         : owner_dn
            }

            class Output(WebSdkOutputModel):
                vault_ids: List[int] = ApiField(alias='VaultIds', default_factory=list)
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Remove(WebSdkEndpoint):
        def post(self, owner_dn: str, certificate: str = None, vault_id: int = None):
            body = {
                'Certificate': certificate,
                'OwnerDN'    : owner_dn,
                'VaultId'    : vault_id
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Retrieve(WebSdkEndpoint):
        def post(self, vault_id: int):
            body = {
                'VaultId': vault_id
            }

            class Output(WebSdkOutputModel):
                certificate_string: str = ApiField(alias='CertificateString')
                typed_name_values: List[secret_store.TypedNameValues] = ApiField(alias='TypedNameValues', default_factory=list)
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))
