from typing import List
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.ssh import SSH


class _SSH:
    def __init__(self, api_obj):
        self.AddAuthorizedKey = self._AddAuthorizedKey(api_obj=api_obj)
        self.AddHostPrivateKey = self._AddHostPrivateKey(api_obj=api_obj)
        self.AddKnownHostKey = self._AddKnownHostKey(api_obj=api_obj)
        self.AddSelfServiceKey = self._AddSelfServiceKey(api_obj=api_obj)
        self.AddSelfServiceAuthorizedKey = self._AddSelfServiceAuthorizedKey(api_obj=api_obj)
        self.AddSelfServicePrivateKey = self._AddSelfServicePrivateKey(api_obj=api_obj)
        self.AddUserPrivateKey = self._AddUserPrivateKey(api_obj=api_obj)
        self.ApproveKeyOperation = self._ApproveKeyOperation(api_obj=api_obj)
        self.CancelKeyOperation = self._CancelKeyOperation(api_obj=api_obj)
        self.CancelRotation = self._CancelRotation(api_obj=api_obj)
        self.ChangePrivateKeyPassphrase = self._ChangePrivateKeyPassphrase(api_obj=api_obj)
        self.ConfirmSelfServiceKeyInstallation = self._ConfirmSelfServiceKeyInstallation(api_obj=api_obj)
        self.DeleteUnmatchedKeyset = self._DeleteUnmatchedKeyset(api_obj=api_obj)
        self.Devices = self._Devices(api_obj=api_obj)
        self.EditKeyOptions = self._EditKeyOptions(api_obj=api_obj)
        self.EditSelfServiceAuthorizedKey = self._EditSelfServiceAuthorizedKey(api_obj=api_obj)
        self.ExportSelfServiceKey = self._ExportSelfServiceKey(api_obj=api_obj)
        self.ExportSelfServicePrivateKey = self._ExportSelfServicePrivateKey(api_obj=api_obj)
        self.ImportAuthorizedKey = self._ImportAuthorizedKey(api_obj=api_obj)
        self.ImportKeyUsageData = self._ImportKeyUsageData(api_obj=api_obj)
        self.ImportPrivateKey = self._ImportPrivateKey(api_obj=api_obj)
        self.KeyDetails = self._KeyDetails(api_obj=api_obj)
        self.KeysetDetails = self._KeysetDetails(api_obj=api_obj)
        self.KeyUsage = self._KeyUsage(api_obj=api_obj)
        self.MoveKeysetsToPolicy = self._MoveKeysetsToPolicy(api_obj=api_obj)
        self.RejectKeyOperation = self._RejectKeyOperation(api_obj=api_obj)
        self.RemoveKey = self._RemoveKey(api_obj=api_obj)
        self.RetryKeyOperation = self._RetryKeyOperation(api_obj=api_obj)
        self.RetryRotation = self._RetryRotation(api_obj=api_obj)
        self.Rotate = self._Rotate(api_obj=api_obj)
        self.SetUnmatchedKeysetPassPhrase = self._SetUnmatchedKeysetPassPhrase(api_obj=api_obj)
        self.SkipKeyRotation = self._SkipKeyRotation(api_obj=api_obj)
        self.TestDeviceConnection = self._TestDeviceConnection(api_obj=api_obj)
        self.Widget = self._Widget(api_obj=api_obj)

    class _AddAuthorizedKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddAuthorizedKey')

        def post(self, device_guid: str, filepath: str, keyset_id: str, username: str, allowed_source_restriction: list = None,
                 denied_source_restriction: list = None, forced_command: str = None, format: str = None, options: list = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'DeniedSourceRestriction': denied_source_restriction,
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'ForcedCommand': forced_command,
                'Format': format,
                'KeysetId': keyset_id,
                'Options': options,
                'Username': username
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def key_id(self) -> str:
                    return self._from_json('KeyId')

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('Response'))

            return _Response(response=self._post(data=body))

    class _AddHostPrivateKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddHostPrivateKey')

        def post(self, device_guid: str, filepath: str, username: str, format: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'Username': username
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def key_id(self) -> str:
                    return self._from_json('KeyId')

                @property
                @api_response_property()
                def keyset_id(self) -> str:
                    return self._from_json('KeysetId')

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('Response'))

            return _Response(response=self._post(data=body))

    class _AddKnownHostKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddKnownHostKey')

        def post(self, device_guid: str, filepath: str, keyset_id: str, username: str, format: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'KeysetId': keyset_id,
                'Username': username
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def key_id(self) -> str:
                    return self._from_json('KeyId')

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('Response'))

            return _Response(response=self._post(data=body))

    class _AddSelfServiceKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddSelfServiceKey')

        def post(self, folder_id: str, location: str, notes: str, owner: str, contact_email: str = None, keyset_id: str = None):
            body = {
                'ContactEmail': contact_email,
                'FolderId': folder_id,
                'KeysetId': keyset_id,
                'Location': location,
                'Notes': notes,
                'Owner': owner
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def key_id(self) -> str:
                    return self._from_json('KeyId')

                @property
                @api_response_property()
                def keyset_id(self) -> str:
                    return self._from_json('KeysetId')

                @property
                @api_response_property()
                def notes(self) -> str:
                    return self._from_json('Notes')

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('Response'))

            return _Response(response=self._post(data=body))

    class _AddSelfServiceAuthorizedKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddSelfServiceAuthorizedKey')

        def post(self, allowed_source_restriction: list, denied_source_restriction: list, folder_id: str, location: str, notes: str,
                 options: list, owner: str, contact_email: str = None, forced_command: str = None, keyset_id: str = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'ContactEmail': contact_email,
                'DeniedSourceRestriction': denied_source_restriction,
                'FolderId': folder_id,
                'ForcedCommand': forced_command,
                'KeysetId': keyset_id,
                'Location': location,
                'Notes': notes,
                'Options': options,
                'Owner': owner
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def key_id(self) -> str:
                    return self._from_json('KeyId')

                @property
                @api_response_property()
                def keyset_id(self) -> str:
                    return self._from_json('KeysetId')

                @property
                @api_response_property()
                def notes(self) -> str:
                    return self._from_json('Notes')

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('Response'))

            return _Response(response=self._post(data=body))

    class _AddSelfServicePrivateKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddSelfServicePrivateKey')

        def post(self, folder_id: str, location: str, notes: str, owner: str, contact_email: str = None, keyset_id: str = None):
            body = {
                'ContactEmail': contact_email,
                'FolderId': folder_id,
                'KeysetId': keyset_id,
                'Location': location,
                'Notes': notes,
                'Owner': owner
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def owner(self) -> str:
                    return self._from_json('Owner')

                @property
                @api_response_property()
                def location(self) -> str:
                    return self._from_json('Location')

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('Response'))

            return _Response(response=self._post(data=body))

    class _AddUserPrivateKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/AddUserPrivateKey')

        def post(self, device_guid: str, filepath: str, username: str, format: str = None, keyset_id: str = None, passphrase: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'KeysetId': keyset_id,
                'Passphrase': passphrase,
                'Username': username
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def key_id(self) -> str:
                    return self._from_json('KeyId')

                @property
                @api_response_property()
                def keyset_id(self) -> str:
                    return self._from_json('KeysetId')

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('Response'))

            return _Response(response=self._post(data=body))

    class _ApproveKeyOperation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ApproveKeyOperation')

        def post(self, key_id: str, comment: str):
            body = {
                'KeyId': key_id,
                'Comment': comment
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _CancelKeyOperation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/CancelKeyOperation')

        def post(self, key_id: str):
            body = {
                'KeyId': key_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _CancelRotation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/CancelRotation')

        def post(self, keyset_id: str):
            body = {
                'KeysetId': keyset_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _ChangePrivateKeyPassphrase(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ChangePrivateKeyPassphrase')

        def post(self, key_id: str, passphrase: str):
            body = {
                'KeysetId': key_id,
                'Passphrase': passphrase
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _ConfirmSelfServiceKeyInstallation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ConfirmSelfServiceKeyInstallation')

        def post(self, keyset_id: str):
            body = {
                'KeysetId': keyset_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _DeleteUnmatchedKeyset(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/DeleteUnmatchedKeyset')

        def post(self, unmatched_trust_id: str):
            body = {
                'UnmatchedTrustId': unmatched_trust_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _Devices(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/Devices')

        def post(self, page_size: int, offset: int = None, ssh_device_filter: dict = None):
            body = {
                'PageSize': page_size,
                'Offset': offset,
                'SshDeviceFilter': ssh_device_filter
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def data(self):
                    return [SSH.DeviceData(d) for d in self._from_json('Data')]

            return _Response(response=self._post(data=body))

    class _EditSelfServiceAuthorizedKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/EditSelfServiceAuthorizedKey')

        def post(self, key_id: str, allowed_source_restriction: list = None, comments: str = None, denied_source_restriction: list = None,
                 forced_command: str = None, location: str = None, notes: str = None, options: list = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'Comments': comments,
                'DeniedSourceRestriction': denied_source_restriction,
                'ForcedCommand': forced_command,
                'KeyId': key_id,
                'Location': location,
                'Notes': notes,
                'Options': options
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('Response'))

            return _Response(response=self._post(data=body))

    class _ExportSelfServiceKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ExportSelfServiceKey')

        def post(self, key_id: str, format: str = None, passphrase: str = None):
            body = {
                'KeyId': key_id,
                'Format': format,
                'Passphrase': passphrase
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def key_material(self) -> str:
                    return self._from_json('KeyMaterial')

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('Response'))

            return _Response(response=self._post(data=body))

    class _ExportSelfServicePrivateKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ExportSelfServicePrivateKey')

        def post(self, key_id: str, format: str = None, passphrase: str = None):
            body = {
                'KeyId': key_id,
                'Format': format,
                'Passphrase': passphrase
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def key_id(self) -> str:
                    return self._from_json('KeyId')

                @property
                @api_response_property()
                def keyset_id(self) -> str:
                    return self._from_json('KeysetId')

                @property
                @api_response_property()
                def notes(self) -> str:
                    return self._from_json('Notes')

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('Response'))

            return _Response(response=self._post(data=body))

    class _ImportAuthorizedKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ImportAuthorizedKey')

        def post(self, device_guid: str, filepath: str, format: str, key_content_base_64: str, username: str):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'KeyContentBase64': key_content_base_64,
                'Username': username
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def key_id(self) -> str:
                    return self._from_json('KeyId')

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('SshWebResponse'))

            return _Response(response=self._post(data=body))

    class _ImportKeyUsageData(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ImportKeyUsageData')

        def post(self, log_data: list):
            body = {
                'LogData': log_data
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('SshWebResponse'))

            return _Response(response=self._post(data=body))

    class _ImportPrivateKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/ImportPrivateKey')

        def post(self, device_guid: str, filepath: str, format: str, key_content_base_64: str, username: str, passphrase: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath': filepath,
                'Format': format,
                'KeyContentBase64': key_content_base_64,
                'Passphrase': passphrase,
                'Username': username
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def key_id(self) -> str:
                    return self._from_json('KeyId')

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json('SshWebResponse'))

            return _Response(response=self._post(data=body))

    class _EditKeyOptions(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/EditKeyOptions')

        def post(self, key_id: str, allowed_source_restriction: list = None, denied_source_restriction: list = None,
                 forced_command: str = None, options: list = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'DeniedSourceRestriction': denied_source_restriction,
                'ForcedCommand': forced_command,
                'KeyId': key_id,
                'Options': options
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _KeyDetails(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/KeyDetails')

        def post(self, key_id: list):
            body = {
                'KeyId': key_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def key_data(self):
                    return [SSH.KeyData(d) for d in self._from_json('KeyData')]

            return _Response(response=self._post(data=body))

    class _KeysetDetails(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/KeysetDetails')

        def get(self, keyset_id: list, load_key_data: bool = None):
            params = {
                'KeysetId': keyset_id,
                'LoadKeyData': load_key_data
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def access(self):
                    return self._from_json('Access')

                @property
                @api_response_property()
                def algorithm(self):
                    return self._from_json('Algorithm')

                @property
                @api_response_property()
                def fingerprint_md5(self):
                    return self._from_json('FingerprintMD5')

                @property
                @api_response_property()
                def fingerprint_sha256(self):
                    return self._from_json('FingerprintSHA256')

                @property
                @api_response_property()
                def keyset_id(self):
                    return self._from_json('KeysetId')

                @property
                @api_response_property()
                def last_rotation_date(self):
                    return self._from_json('LastRotationDate')

                @property
                @api_response_property()
                def last_used(self):
                    return self._from_json('LastUsed')

                @property
                @api_response_property()
                def length(self):
                    return self._from_json('Length')

                @property
                @api_response_property()
                def private_keys(self):
                    return [SSH.KeyData(key) for key in self._from_json('PrivateKeys')] if 'PrivateKeys' in self.api_response.json() else []

                @property
                @api_response_property()
                def process_status(self):
                    return self._from_json('ProcessStatus')

                @property
                @api_response_property()
                def public_keys(self):
                    return [SSH.KeyData(key) for key in self._from_json('PublicKeys')] if 'PublicKeys' in self.api_response.json() else []

                @property
                @api_response_property()
                def rotation_stage(self):
                    return self._from_json('RotationStage')

                @property
                @api_response_property()
                def type(self):
                    return self._from_json('Type')

                @property
                @api_response_property()
                def violation_status(self):
                    return self._from_json('ViolationStatus')

            return _Response(response=self._get(params=params))

        def post(self, page_size: int, keyset_filter: list = None, load_key_data: bool = None, offset: int = None):
            body = {
                'KeysetFilter': keyset_filter,
                'LoadKeyData': load_key_data,
                'Offset': offset,
                'PageSize': page_size
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def data(self):
                    return [SSH.KeySetData(key) for key in self._from_json('Data')]

            return _Response(response=self._post(data=body))

    class _KeyUsage(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/KeyUsage')

        def post(self, ssh_key_usage_filter: list, load_key_data: bool = None, page_size: int = None, offset: int = None):
            body = {
                'SshKeyUsageFilter': ssh_key_usage_filter,
                'LoadKeyData': load_key_data,
                'PageSize': page_size,
                'Offset': offset
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def data(self):
                    return [SSH.KeyUsageData(key) for key in self._from_json('Data')]

            return _Response(response=self._post(data=body))

    class _MoveKeysetsToPolicy(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/MoveKeysetsToPolicy')

        def post(self, keyset_ids: list, policy_path: str):
            body = {
                'KeysetIds': keyset_ids,
                'PolicyPath': policy_path
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _RejectKeyOperation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/RejectKeyOperation')

        def post(self, key_id: str, comment: str):
            body = {
                'KeyId': key_id,
                'Comment': comment
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _RemoveKey(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/RemoveKey')

        def post(self, key_id: str):
            body = {
                'KeyId': key_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _RetryKeyOperation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/RetryKeyOperation')

        def post(self, key_id: str):
            body = {
                'KeyId': key_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _RetryRotation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/RetryRotation')

        def post(self, keyset_id: str):
            body = {
                'KeysetId': keyset_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _Rotate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/Rotate')

        def post(self, allow_skip_on_rotation: bool, keyset_id: str):
            body = {
                'AllowSkipOnRotation': allow_skip_on_rotation,
                'KeysetId': keyset_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _SetUnmatchedKeysetPassPhrase(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/SetUnmatchedKeysetPassPhrase')

        def post(self, passphrase: str, unmatched_trust_id: str):
            body = {
                'Passphrase': passphrase,
                'UnmatchedTrustId': unmatched_trust_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _SkipKeyRotation(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSH/SkipKeyRotation')

        def post(self, key_id: str):
            body = {
                'KeyId': key_id
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def response(self):
                    return SSH.Response(self._from_json())

            return _Response(response=self._post(data=body))

    class _TestDeviceConnection(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='SSH/TestDeviceConnection')

        def post(self, device_guids: List[str]):
            body = {
                'deviceGuids': device_guids
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def connection_results(self):
                    return [SSH.ConnectionResult(result) for result in self._from_json()]

            return _Response(response=self._post(data=body))

    class _Widget:
        def __init__(self, api_obj):
            self.CriticalAlerts = self._CriticalAlerts(api_obj=api_obj)
            self.PolicyViolations = self._PolicyViolations(api_obj=api_obj)
            self.Stats = self._Stats(api_obj=api_obj)

        class _CriticalAlerts(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SSH/Widget/CriticalAlerts')

            def get(self, min_allowed_key_length: int):
                params = {
                    'minAllowedKeyLength': min_allowed_key_length
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def root_orphans(self) -> int:
                        return self._from_json('RootOrphans')

                    @property
                    @api_response_property()
                    def non_root_orphans(self) -> int:
                        return self._from_json('NonRootOrphans')

                    @property
                    @api_response_property()
                    def accessible_root_accounts(self) -> int:
                        return self._from_json('AccessibleRootAccounts')

                    @property
                    @api_response_property()
                    def shared_private_keys(self) -> int:
                        return self._from_json('SharedPrivateKeys')

                    @property
                    @api_response_property()
                    def non_compliant_duplicate_private_keys(self) -> int:
                        return self._from_json('NonCompliantDuplicatePrivateKeys')

                    @property
                    @api_response_property()
                    def very_small_key(self) -> int:
                        return self._from_json('VerySmallKey')

                return _Response(response=self._get(params=params))

        class _PolicyViolations(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SSH/Widget/PolicyViolations')

            def get(self):
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def non_compliant_force_command(self):
                        return self._from_json('NonCompliantForceCommand')

                    @property
                    @api_response_property()
                    def non_compliant_source_restriction(self):
                        return self._from_json('NonCompliantSourceRestriction')

                    @property
                    @api_response_property()
                    def missing_options(self):
                        return self._from_json('MissingOptions')

                    @property
                    @api_response_property()
                    def non_compliant_algorithm(self):
                        return self._from_json('NonCompliantAlgorithm')

                    @property
                    @api_response_property()
                    def vulnerable_protocol(self):
                        return self._from_json('VulnerableProtocol')

                    @property
                    @api_response_property()
                    def non_compliant_vendor_format(self):
                        return self._from_json('NonCompliantVendorFormat')

                    @property
                    @api_response_property()
                    def key_older_than_policy(self):
                        return self._from_json('KeyOlderThanPolicy')

                    @property
                    @api_response_property()
                    def shared_server_account(self):
                        return self._from_json('SharedServerAccount')

                    @property
                    @api_response_property()
                    def key_smaller_than_policy(self):
                        return self._from_json('KeySmallerThanPolicy')

                    @property
                    @api_response_property()
                    def duplicate_private_keys(self):
                        return self._from_json('DuplicatePrivateKeys')

                    @property
                    @api_response_property()
                    def root_access(self):
                        return self._from_json('RootAccess')

                return _Response(response=self._get())

        class _Stats(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SSH/Widget/Stats')

            def get(self, group_by: str):
                params = {
                    'GroupBy': group_by
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def name_value_pairs(self) -> dict:
                        return self._from_json()

                return _Response(response=self._get(params=params))
