from typing import List 
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.secret_store import SecretStore


class _SecretStore:
    def __init__(self, api_obj):
        self.Add = self._Add(api_obj=api_obj)
        self.Associate = self._Associate(api_obj=api_obj)
        self.Dissociate = self._Dissociate(api_obj=api_obj)
        self.EncryptionKeysInUse = self._EncryptionKeysInUse(api_obj=api_obj)
        self.Lookup = self._Lookup(api_obj=api_obj)
        self.LookupAllAssociationsbyVaultid = self._LookupAllAssociationsbyVaultid(api_obj=api_obj)
        self.LookupByAssociation = self._LookupByAssociation(api_obj=api_obj)
        self.LookupAssociationbyVaultID = self._LookupAssociationbyVaultID(api_obj=api_obj)
        self.LookupByOwner = self._LookupByOwner(api_obj=api_obj)
        self.LookupByVaultType = self._LookupByVaultType(api_obj=api_obj)
        self.Mutate = self._Mutate(api_obj=api_obj)
        self.OrphanLookup = self._OrphanLookup(api_obj=api_obj)
        self.OwnerAdd = self._OwnerAdd(api_obj=api_obj)
        self.OwnerDelete = self._OwnerDelete(api_obj=api_obj)
        self.OwnerLookup = self._OwnerLookup(api_obj=api_obj)
        self.Retrieve = self._Retrieve(api_obj=api_obj)

    class _Add(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/Add')

        def post(self, base_64_data: str, keyname: str, namespace: str, owner: str, vault_type: int):
            body = {
                'Base64Data': base_64_data,
                'Keyname': keyname,
                'Namespace': namespace,
                'Owner': owner,
                'VaultType': vault_type
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

                @property
                @api_response_property()
                def vault_id(self) -> int:
                    return self._from_json(key='VaultID')

            return _Response(response=self._post(data=body))

    class _Associate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/Associate')

        def post(self, name: str, vault_id: int, date_value: int = None, int_value: int = None, string_value: str = None):
            body = {
                'Name': name,
                'VaultID': vault_id,
                'DateValue': date_value,
                'IntValue': int_value,
                'StringValue': string_value
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _Dissociate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/Dissociate')

        def post(self, vault_id: int, int_value: int = None, name: str = None, string_value: str = None, date_value: int = None):
            body = {
                'VaultID': vault_id,
                'IntValue': int_value,
                'Name': name,
                'StringValue': string_value,
                'DateValue': date_value
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _EncryptionKeysInUse(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/EncryptionKeysInUse')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def encryption_keys(self) -> List[str]:
                    return self._from_json(key='EncryptionKeys')

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

            return _Response(response=self._get())

    class _Lookup(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/Lookup')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

                @property
                @api_response_property()
                def vault_ids(self) -> List[int]:
                    return self._from_json(key='VaultIDs')

            return _Response(response=self._get())

    class _LookupAllAssociationsbyVaultid(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/LookupAllAssociationsbyVaultid')

        def post(self, vault_id: int):
            body = {
                'VaultID': vault_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

                @property
                @api_response_property()
                def typed_name_values(self):
                    return [SecretStore.TypedNameValues(tnv) for tnv in self._from_json('TypedNameValues')]

            return _Response(response=self._post(data=body))

    class _LookupByAssociation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/LookupByAssociation')

        def post(self, name: str, int_value: int = None ,string_value: str = None, date_value: int = None):
            body = {
                'Name': name,
                'IntValue': int_value,
                'StringValue': string_value,
                'DateValue': date_value
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

                @property
                @api_response_property()
                def vault_ids(self) -> List[int]:
                    return self._from_json(key='VaultIDs')

            return _Response(response=self._post(data=body))

    class _LookupAssociationbyVaultID(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/LookupAssociationbyVaultID')

        def post(self, vault_id: int, name: str = None):
            body = {
                'VaultID': vault_id,
                'Name': name
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

                @property
                @api_response_property()
                def value(self) -> str:
                    return self._from_json(key='Value')

            return _Response(response=self._post(data=body))

    class _LookupByOwner(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/LookupByOwner')

        def post(self, namespace: str, owner: str, vault_type: str = None):
            body = {
                'Namespace': namespace,
                'Owner': owner,
                'VaultType': vault_type
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

                @property
                @api_response_property()
                def vault_ids(self) -> List[int]:
                    return self._from_json(key='VaultIDs')

            return _Response(response=self._post(data=body))

    class _LookupByVaultType(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/LookupByVaultType')

        def post(self, vault_type: int):
            body = {
                'VaultType': vault_type
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

                @property
                @api_response_property()
                def vault_ids(self) -> List[int]:
                    return self._from_json(key='VaultIDs')

            return _Response(response=self._post(data=body))

    class _Mutate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/Mutate')

        def post(self, vault_id: int, vault_type: int):
            body = {
                'VaultID': vault_id,
                'VaultType': vault_type
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _OrphanLookup(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/OrphanLookup')

        def post(self, vault_type: int):
            body = {
                'VaultType': vault_type
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

                @property
                @api_response_property()
                def vault_ids(self) -> List[int]:
                    return self._from_json(key='VaultIDs')

            return _Response(response=self._post(data=body))

    class _OwnerAdd(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/OwnerAdd')

        def post(self, namespace: str, owner: str, vault_id: int):
            body = {
                'Namespace': namespace,
                'Owner': owner,
                'VaultId': vault_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _OwnerDelete(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/OwnerDelete')

        def post(self, namespace: str, owner: str, vault_id: int = None):
            body = {
                'Namespace': namespace,
                'Owner': owner,
                'VaultId': vault_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _OwnerLookup(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/OwnerLookup')

        def post(self, namespace: str, vault_id: int):
            body = {
                'Namespace': namespace,
                'VaultID': vault_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

                @property
                @api_response_property()
                def owners(self) -> List[str]:
                    return self._from_json(key='Owners')

            return _Response(response=self._post(data=body))

    class _Retrieve(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SecretStore/Retrieve')

        def post(self, vault_id: int):
            body = {
                'VaultID': vault_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def base_64_data(self) -> str:
                    return self._from_json(key='Base64Data')

                @property
                @api_response_property()
                def result(self):
                    return SecretStore.Result(self._from_json(key='Result'))

                @property
                @api_response_property()
                def vault_type(self) -> str:
                    return self._from_json(key='VaultType')

            return _Response(response=self._post(data=body))
