import time
from typing import List, Dict
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.credential import Credential
from pytpp.tools.helpers.date_converter import from_date_string


class _Credentials:
    def __init__(self, api_obj):
        self.Adaptable = self._Adaptable(api_obj=api_obj)
        self.Connector = self._Connector(api_obj=api_obj)
        self.Create = self._Create(api_obj=api_obj)
        self.Delete = self._Delete(api_obj=api_obj)
        self.Enumerate = self._Enumerate(api_obj=api_obj)
        self.Rename = self._Rename(api_obj=api_obj)
        self.Retrieve = self._Retrieve(api_obj=api_obj)
        self.Update = self._Update(api_obj=api_obj)
        self.CyberArk = self._CyberArk(api_obj=api_obj)

    class _Adaptable:
        def __init__(self, api_obj):
            self.Update = self._Update(api_obj=api_obj)
        
        class _Update(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Credentials/Adaptable/Update')
            
            def post(self, credential_path: str, credential_type: str, connector_name: str,
                     custom_fields: List[Dict[str, str]]):
                body = {
                    'CredentialPath': credential_path,
                    'CredentialType': credential_type,
                    'ConnectorName': connector_name,
                    'CustomFields': custom_fields
                }
                
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def result(self):
                        return Credential.Result(self._from_json(key='Result'))
                        
                return _Response(response=self._post(data=body))

    class _Connector:
        def __init__(self, api_obj):
            self.Adaptable = self._Adaptable(api_obj=api_obj)

        class _Adaptable(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Credentials/Connector/Adaptable')

            def post(self, connector_name: str, powershell_script: str, service_address: str,
                     service_credential: str, allowed_identities: List[str] = None,
                     description: str = None):
                body = {
                    'AllowedIdentities': allowed_identities,
                    'ConnectorName': connector_name,
                    'Description': description,
                    'PowershellScript': powershell_script,
                    'ServiceAddress': service_address,
                    'ServiceCredential': service_credential
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def succcess(self) -> bool:
                        return self._from_json(key='Succcess')

                return _Response(response=self._post(data=body))

            def Guid(self, guid: str):
                return self._Guid(api_obj=self._api_obj, guid=guid)

            class _Guid(API):
                def __init__(self, api_obj, guid: str):
                    super().__init__(api_obj=api_obj, url=f'/Credentials/Connector/Adaptable/{guid}')

                def delete(self):
                    class _Response(APIResponse):
                        def __init__(self, response):
                            super().__init__(response=response)

                        @property
                        @api_response_property()
                        def success(self) -> bool:
                            return self._from_json(key='Success')

                    return _Response(response=self._delete())

                def get(self):
                    class _Response(APIResponse):
                        def __init__(self, response):
                            super().__init__(response=response)

                        @property
                        @api_response_property()
                        def allowed_identities(self) -> List[str]:
                            return self._from_json(key='AllowedIdentities')

                        @property
                        @api_response_property()
                        def powershell_script(self) -> str:
                            return self._from_json(key='PowershellScript')

                        @property
                        @api_response_property()
                        def service_address(self) -> str:
                            return self._from_json(key='ServiceAddress')

                        @property
                        @api_response_property()
                        def service_credential(self) -> str:
                            return self._from_json(key='ServiceCredential')

                        @property
                        @api_response_property()
                        def success(self) -> bool:
                            return self._from_json(key='Success')

                    return _Response(response=self._get())

                def put(self, connector_name: str = None, powershell_script: str = None,
                        service_address: str = None, service_credential: str = None,
                        allowed_identities: List[str] = None, description: str = None):
                    body = {
                        'AllowedIdentities': allowed_identities,
                        'ConnectorName'    : connector_name,
                        'Description'      : description,
                        'PowershellScript' : powershell_script,
                        'ServiceAddress'   : service_address,
                        'ServiceCredential': service_credential
                    }

                    class _Response(APIResponse):
                        def __init__(self, response):
                            super().__init__(response=response)

                        @property
                        @api_response_property()
                        def succcess(self) -> bool:
                            return self._from_json(key='Succcess')

                    return _Response(response=self._put(data=body))

    class _Create(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Credentials/Create')

        def post(self, credential_path: str, friendly_name: str, values: list, password: str = None, description: str = None,
                 encryption_key: str = None, shared: bool = False, expiration: int = None, contact: list = None):
            body = {
                'CredentialPath': credential_path,
                'Password': password,
                'FriendlyName': friendly_name,
                'Values': values,
                'Expiration': f'/Date({expiration})/',
                'Description': description,
                'EncryptionKey': encryption_key,
                'Shared': shared,
                'Contact': contact
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Credential.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _Delete(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Credentials/Delete')

        def post(self, credential_path: str):
            body = {
                'CredentialPath': credential_path
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Credential.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _Enumerate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Credentials/Enumerate')

        def post(self, credential_path: str, pattern: str = None, recursive: bool = False):
            body = {
                'CredentialPath': credential_path,
                'Recursive': recursive,
                'Pattern': pattern
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Credential.Result(self._from_json(key='Result'))

                @property
                @api_response_property()
                def credential_infos(self):
                    return [Credential.CredentialInfo(cred_info) for cred_info in self._from_json(key='CredentialInfos')]

            return _Response(response=self._post(data=body))

    class _Rename(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Credentials/Rename')

        def post(self, credential_path: str, new_credential_path: str):
            body = {
                'CredentialPath': credential_path,
                'NewCredentialPath': new_credential_path
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Credential.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _Retrieve(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Credentials/Retrieve')

        def post(self, credential_path: str):
            body = {
                'CredentialPath': credential_path
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def classname(self) -> str:
                    return self._from_json(key='Classname')

                @property
                @api_response_property()
                def description(self) -> str:
                    return self._from_json(key='Description')

                @property
                @api_response_property()
                def expiration(self):
                    return from_date_string(self._from_json(key='Expiration'))

                @property
                @api_response_property()
                def friendly_name(self) -> str:
                    return self._from_json(key='FriendlyName')

                @property
                @api_response_property()
                def result(self):
                    return Credential.Result(self._from_json(key='Result'))

                @property
                @api_response_property()
                def values(self):
                    return [Credential.NameTypeValue(ntv) for ntv in self._from_json(key='Values')]

            return _Response(response=self._post(data=body))

    class _Update(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Credentials/Update')

        def post(self, credential_path: str, friendly_name: str, values: list, description: str = None,
                 encryption_key: str = None, shared: bool = False, expiration: int = None, contact: list = None):
            body = {
                'CredentialPath': credential_path,
                'FriendlyName': friendly_name,
                'Values': values,
                'Description': description,
                'EncryptionKey': encryption_key,
                'Shared': shared,
                'Contact': contact
            }

            if expiration:
                exp_date = expiration
            else:
                # Expire in 10 years.
                exp_date = int((time.time() + (60 * 60 * 24 * 365 * 10)) * 1000)

            body.update({'Expiration': r'/Date(%s)/' % exp_date})
            
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def result(self):
                    return Credential.Result(self._from_json(key='Result'))

            return _Response(response=self._post(data=body))

    class _CyberArk:
        def __init__(self, api_obj):
            self.Create = self._Create(api_obj=api_obj)
            self.Update = self._Update(api_obj=api_obj)

        class _Create(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Credentials/CyberArk/Create')

            def post(self, cyber_ark_username: str, cyber_ark_password: str, username: str, app_id: str, safe_name: str,
                     folder_name: str, account_name: str, credentials_path: str):
                body = {
                    'CyberArkUsername': cyber_ark_username,
                    'CyberArkPassword': cyber_ark_password,
                    'Username': username,
                    'AppID': app_id,
                    'SafeName': safe_name,
                    'FolderName': folder_name,
                    'AccountName': account_name,
                    'CredentialsPath': credentials_path
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def result(self):
                        return Credential.Result(self._from_json(key='Result'))

                return _Response(response=self._post(data=body))

        class _Update(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/Credentials/CyberArk/Update')

            def post(self, cyber_ark_username: str, cyber_ark_password: str, username: str, app_id: str, safe_name: str,
                     folder_name: str, account_name: str, credentials_path: str):
                body = {
                    'CyberArkUsername': cyber_ark_username,
                    'CyberArkPassword': cyber_ark_password,
                    'Username': username,
                    'AppID': app_id,
                    'SafeName': safe_name,
                    'FolderName': folder_name,
                    'AccountName': account_name,
                    'CredentialsPath': credentials_path
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def result(self):
                        return Credential.Result(self._from_json(key='Result'))

                return _Response(response=self._post(data=body))
