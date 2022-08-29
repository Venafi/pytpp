import time
from datetime import datetime
from typing import List, Dict
from pytpp.api.websdk.models import credential, identity
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Credentials(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Credentials')
        self.Adaptable = self._Adaptable(api_obj=api_obj, url=f'{self._url}/Adaptable')
        self.Connector = self._Connector(api_obj=api_obj, url=f'{self._url}/Connector')
        self.Create = self._Create(api_obj=api_obj, url=f'{self._url}/Create')
        self.Delete = self._Delete(api_obj=api_obj, url=f'{self._url}/Delete')
        self.Enumerate = self._Enumerate(api_obj=api_obj, url=f'{self._url}/Enumerate')
        self.Rename = self._Rename(api_obj=api_obj, url=f'{self._url}/Rename')
        self.Retrieve = self._Retrieve(api_obj=api_obj, url=f'{self._url}/Retrieve')
        self.Update = self._Update(api_obj=api_obj, url=f'{self._url}/Update')
        self.CyberArk = self._CyberArk(api_obj=api_obj, url=f'{self._url}/CyberArk')

    class _Adaptable(WebSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.Create = self._Create(api_obj=self._api_obj, url=f'{self._url}/Create')
            self.Update = self._Update(api_obj=self._api_obj, url=f'{self._url}/Update')

        class _Create(WebSdkEndpoint):
            def post(self, credential_path: str, credential_type: credential.CredentialType, connector_name: str,
                     custom_fields: List[Dict[str, str]]):
                body = {
                    'CredentialPath': credential_path,
                    'CredentialType': credential_type,
                    'ConnectorName' : connector_name,
                    'CustomFields'  : custom_fields
                }

                class Output(WebSdkOutputModel):
                    result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _Update(WebSdkEndpoint):
            def post(self, credential_path: str, credential_type: str, connector_name: str,
                     custom_fields: List[Dict[str, str]]):
                body = {
                    'CredentialPath': credential_path,
                    'CredentialType': credential_type,
                    'ConnectorName' : connector_name,
                    'CustomFields'  : custom_fields
                }

                class Output(WebSdkOutputModel):
                    result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

                return generate_output(output_cls=Output, response=self._post(data=body))

    class _Connector(WebSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.Adaptable = self._Adaptable(api_obj=self._api_obj, url=f'{self._url}/Adaptable')

        class _Adaptable(WebSdkEndpoint):
            def post(self, connector_name: str, powershell_script: str, service_address: str,
                     service_credential: str, allowed_identities: List[str] = None,
                     description: str = None):
                body = {
                    'AllowedIdentities': allowed_identities,
                    'ConnectorName'    : connector_name,
                    'Description'      : description,
                    'PowershellScript' : powershell_script,
                    'ServiceAddress'   : service_address,
                    'ServiceCredential': service_credential
                }

                class Output(WebSdkOutputModel):
                    success: bool = ApiField(alias='Success')

                return generate_output(output_cls=Output, response=self._post(data=body))

            def Guid(self, guid: str):
                return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

            class _Guid(WebSdkEndpoint):
                def delete(self):
                    class Output(WebSdkOutputModel):
                        success: bool = ApiField(alias='Success')

                    return generate_output(output_cls=Output, response=self._delete())

                def get(self):
                    class Output(WebSdkOutputModel):
                        allowed_identities: List[str] = ApiField(default_factory=list, alias='AllowedIdentities')
                        powershell_script: str = ApiField(alias='PowershellScript')
                        service_address: str = ApiField(alias='ServiceAddress')
                        service_credential: str = ApiField(alias='ServiceCredential')
                        success: bool = ApiField(alias='Success')

                    return generate_output(output_cls=Output, response=self._get())

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

                    class Output(WebSdkOutputModel):
                        success: bool = ApiField(alias='Success')

                    return generate_output(output_cls=Output, response=self._put(data=body))

    class _Create(WebSdkEndpoint):
        def post(self, credential_path: str, friendly_name: str, values: List[credential.NameTypeValue], password: str = None,
                 description: str = None, encryption_key: str = None, shared: bool = False, expiration: int = None,
                 contact: List[str] = None):
            body = {
                'CredentialPath': credential_path,
                'Password'      : password,
                'FriendlyName'  : friendly_name,
                'Values'        : values,
                'Expiration'    : f'/Date({expiration})/',
                'Description'   : description,
                'EncryptionKey' : encryption_key,
                'Shared'        : shared,
                'Contact'       : contact
            }

            class Output(WebSdkOutputModel):
                result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Delete(WebSdkEndpoint):
        def post(self, credential_path: str):
            body = {
                'CredentialPath': credential_path
            }

            class Output(WebSdkOutputModel):
                result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Enumerate(WebSdkEndpoint):
        def post(self, credential_path: str, pattern: str = None, recursive: bool = False):
            body = {
                'CredentialPath': credential_path,
                'Recursive'     : recursive,
                'Pattern'       : pattern
            }

            class Output(WebSdkOutputModel):
                result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))
                credential_infos: List[credential.CredentialInfo] = ApiField(default_factory=list, alias='CredentialInfos')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Rename(WebSdkEndpoint):
        def post(self, credential_path: str, new_credential_path: str):
            body = {
                'CredentialPath'   : credential_path,
                'NewCredentialPath': new_credential_path
            }

            class Output(WebSdkOutputModel):
                result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Retrieve(WebSdkEndpoint):
        def post(self, credential_path: str):
            body = {
                'CredentialPath': credential_path
            }

            class Output(WebSdkOutputModel):
                classname: str = ApiField(alias='Classname')
                contact: List[identity.Identity] = ApiField(alias='Contact', default_factory=list)
                description: str = ApiField(alias='Description')
                expiration: datetime = ApiField(alias='Expiration')
                friendly_name: str = ApiField(alias='FriendlyName')
                result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))
                values: List[credential.NameTypeValue] = ApiField(default_factory=list, alias='Values')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Update(WebSdkEndpoint):
        def post(self, credential_path: str, friendly_name: str, values: List[credential.NameTypeValue], description: str = None,
                 encryption_key: str = None, shared: bool = False, expiration: int = None, contact: List[str] = None):
            body = {
                'CredentialPath': credential_path,
                'FriendlyName'  : friendly_name,
                'Values'        : values,
                'Description'   : description,
                'EncryptionKey' : encryption_key,
                'Shared'        : shared,
                'Contact'       : contact
            }

            if expiration:
                exp_date = expiration
            else:
                # Expire in 10 years.
                exp_date = int((time.time() + (60 * 60 * 24 * 365 * 10)) * 1000)

            body.update({
                'Expiration': r'/Date(%s)/' % exp_date
            })

            class Output(WebSdkOutputModel):
                result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _CyberArk(WebSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.Create = self._Create(api_obj=self._api_obj, url=f'{self._url}/Create')
            self.Update = self._Update(api_obj=self._api_obj, url=f'{self._url}/Update')

        class _Create(WebSdkEndpoint):
            def post(self, cyber_ark_username: str, cyber_ark_password: str, username: str, app_id: str, safe_name: str,
                     folder_name: str, account_name: str, credential_path: str):
                body = {
                    'CyberArkUsername': cyber_ark_username,
                    'CyberArkPassword': cyber_ark_password,
                    'Username'        : username,
                    'AppID'           : app_id,
                    'SafeName'        : safe_name,
                    'FolderName'      : folder_name,
                    'AccountName'     : account_name,
                    'CredentialPath'  : credential_path
                }

                class Output(WebSdkOutputModel):
                    result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

                return generate_output(output_cls=Output, response=self._post(data=body))

        class _Update(WebSdkEndpoint):
            def post(self, cyber_ark_username: str, cyber_ark_password: str, username: str, app_id: str, safe_name: str,
                     folder_name: str, account_name: str, credential_path: str):
                body = {
                    'CyberArkUsername': cyber_ark_username,
                    'CyberArkPassword': cyber_ark_password,
                    'Username'        : username,
                    'AppID'           : app_id,
                    'SafeName'        : safe_name,
                    'FolderName'      : folder_name,
                    'AccountName'     : account_name,
                    'CredentialPath'  : credential_path
                }

                class Output(WebSdkOutputModel):
                    result: credential.Result = ApiField(alias='Result', converter=lambda x: credential.Result(code=x))

                return generate_output(output_cls=Output, response=self._post(data=body))
