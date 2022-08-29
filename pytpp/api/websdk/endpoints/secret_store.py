from typing import List
from pytpp.api.websdk.models import secret_store
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _SecretStore(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/SecretStore')
        self.Add = self._Add(api_obj=self._api_obj, url=f'{self._url}/Add')
        self.Associate = self._Associate(api_obj=self._api_obj, url=f'{self._url}/Associate')
        self.Dissociate = self._Dissociate(api_obj=self._api_obj, url=f'{self._url}/Dissociate')
        self.EncryptionKeysInUse = self._EncryptionKeysInUse(api_obj=self._api_obj, url=f'{self._url}/EncryptionKeysInUse')
        self.Lookup = self._Lookup(api_obj=self._api_obj, url=f'{self._url}/Lookup')
        self.LookupAllAssociationsbyVaultid = self._LookupAllAssociationsbyVaultid(api_obj=self._api_obj, url=f'{self._url}/LookupAllAssociationsbyVaultid')
        self.LookupByAssociation = self._LookupByAssociation(api_obj=self._api_obj, url=f'{self._url}/LookupByAssociation')
        self.LookupAssociationbyVaultID = self._LookupAssociationbyVaultID(api_obj=self._api_obj, url=f'{self._url}/LookupAssociationbyVaultID')
        self.LookupByOwner = self._LookupByOwner(api_obj=self._api_obj, url=f'{self._url}/LookupByOwner')
        self.LookupByVaultType = self._LookupByVaultType(api_obj=self._api_obj, url=f'{self._url}/LookupByVaultType')
        self.Mutate = self._Mutate(api_obj=self._api_obj, url=f'{self._url}/Mutate')
        self.OrphanLookup = self._OrphanLookup(api_obj=self._api_obj, url=f'{self._url}/OrphanLookup')
        self.OwnerAdd = self._OwnerAdd(api_obj=self._api_obj, url=f'{self._url}/OwnerAdd')
        self.OwnerDelete = self._OwnerDelete(api_obj=self._api_obj, url=f'{self._url}/OwnerDelete')
        self.OwnerLookup = self._OwnerLookup(api_obj=self._api_obj, url=f'{self._url}/OwnerLookup')
        self.Retrieve = self._Retrieve(api_obj=self._api_obj, url=f'{self._url}/Retrieve')

    class _Add(WebSdkEndpoint):
        def post(self, base_64_data: str, keyname: str, namespace: str, owner: str, vault_type: int):
            body = {
                'Base64Data': base_64_data,
                'Keyname'   : keyname,
                'Namespace' : namespace,
                'Owner'     : owner,
                'VaultType' : vault_type
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_id: int = ApiField(alias='VaultID')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Associate(WebSdkEndpoint):
        def post(self, name: str, vault_id: int, date_value: str = None, int_value: int = None, string_value: str = None):
            body = {
                'Name'       : name,
                'VaultID'    : vault_id,
                'DateValue'  : date_value,
                'IntValue'   : int_value,
                'StringValue': string_value
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Dissociate(WebSdkEndpoint):
        def post(self, vault_id: int, int_value: int = None, name: str = None, string_value: str = None, date_value: int = None):
            body = {
                'VaultID'    : vault_id,
                'IntValue'   : int_value,
                'Name'       : name,
                'StringValue': string_value,
                'DateValue'  : date_value
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _EncryptionKeysInUse(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                encryption_keys: List[str] = ApiField(default_factory=list, alias='EncryptionKeys')
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return generate_output(output_cls=Output, response=self._get())

    class _Lookup(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_ids: List[int] = ApiField(default_factory=list, alias='VaultIDs')

            return generate_output(output_cls=Output, response=self._get())

    class _LookupAllAssociationsbyVaultid(WebSdkEndpoint):
        def post(self, vault_id: int):
            body = {
                'VaultID': vault_id
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                typed_name_values: List[secret_store.TypedNameValues] = ApiField(default_factory=list, alias='TypedNameValues')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _LookupByAssociation(WebSdkEndpoint):
        def post(self, name: str, int_value: int = None, string_value: str = None, date_value: int = None):
            body = {
                'Name'       : name,
                'IntValue'   : int_value,
                'StringValue': string_value,
                'DateValue'  : date_value
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_ids: List[int] = ApiField(default_factory=list, alias='VaultIDs')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _LookupAssociationbyVaultID(WebSdkEndpoint):
        def post(self, vault_id: int, name: str = None):
            body = {
                'VaultID': vault_id,
                'Name'   : name
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                value: str = ApiField(alias='Value')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _LookupByOwner(WebSdkEndpoint):
        def post(self, namespace: str, owner: str, vault_type: str = None):
            body = {
                'Namespace': namespace,
                'Owner'    : owner,
                'VaultType': vault_type
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_ids: List[int] = ApiField(default_factory=list, alias='VaultIDs')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _LookupByVaultType(WebSdkEndpoint):
        def post(self, vault_type: int):
            body = {
                'VaultType': vault_type
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_ids: List[int] = ApiField(default_factory=list, alias='VaultIDs')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Mutate(WebSdkEndpoint):
        def post(self, vault_id: int, vault_type: int):
            body = {
                'VaultID'  : vault_id,
                'VaultType': vault_type
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _OrphanLookup(WebSdkEndpoint):
        def post(self, vault_type: int):
            body = {
                'VaultType': vault_type
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_ids: List[int] = ApiField(default_factory=list, alias='VaultIDs')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _OwnerAdd(WebSdkEndpoint):
        def post(self, namespace: str, owner: str, vault_id: int):
            body = {
                'Namespace': namespace,
                'Owner'    : owner,
                'VaultId'  : vault_id
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _OwnerDelete(WebSdkEndpoint):
        def post(self, namespace: str, owner: str, vault_id: int = None):
            body = {
                'Namespace': namespace,
                'Owner'    : owner,
                'VaultId'  : vault_id
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _OwnerLookup(WebSdkEndpoint):
        def post(self, namespace: str, vault_id: int):
            body = {
                'Namespace': namespace,
                'VaultID'  : vault_id
            }

            class Output(WebSdkOutputModel):
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                owners: List[str] = ApiField(default_factory=list, alias='Owners')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Retrieve(WebSdkEndpoint):
        def post(self, vault_id: int):
            body = {
                'VaultID': vault_id
            }

            class Output(WebSdkOutputModel):
                base_64_data: str = ApiField(alias='Base64Data')
                result: secret_store.Result = ApiField(alias='Result', converter=lambda x: secret_store.Result(code=x))
                vault_type: str = ApiField(alias='VaultType')

            return generate_output(output_cls=Output, response=self._post(data=body))
