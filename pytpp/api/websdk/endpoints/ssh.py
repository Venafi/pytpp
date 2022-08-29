from typing import Any, Dict, List, Union
from pytpp.api.websdk.models import ssh
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _SSH(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/SSH')
        self.AddAuthorizedKey = self._AddAuthorizedKey(api_obj=self._api_obj, url=f'{self._url}/AddAuthorizedKey')
        self.AddHostPrivateKey = self._AddHostPrivateKey(api_obj=self._api_obj, url=f'{self._url}/AddHostPrivateKey')
        self.AddKnownHostKey = self._AddKnownHostKey(api_obj=self._api_obj, url=f'{self._url}/AddKnownHostKey')
        self.AddSelfServiceAuthorizedKey = self._AddSelfServiceAuthorizedKey(api_obj=self._api_obj, url=f'{self._url}/AddSelfServiceAuthorizedKey')
        self.AddSelfServicePrivateKey = self._AddSelfServicePrivateKey(api_obj=self._api_obj, url=f'{self._url}/AddSelfServicePrivateKey')
        self.AddUserPrivateKey = self._AddUserPrivateKey(api_obj=self._api_obj, url=f'{self._url}/AddUserPrivateKey')
        self.ApproveKeyOperation = self._ApproveKeyOperation(api_obj=self._api_obj, url=f'{self._url}/ApproveKeyOperation')
        self.CancelKeyOperation = self._CancelKeyOperation(api_obj=self._api_obj, url=f'{self._url}/CancelKeyOperation')
        self.CancelRotation = self._CancelRotation(api_obj=self._api_obj, url=f'{self._url}/CancelRotation')
        self.ChangePrivateKeyPassphrase = self._ChangePrivateKeyPassphrase(api_obj=self._api_obj, url=f'{self._url}/ChangePrivateKeyPassphrase')
        self.ConfirmSelfServiceKeyInstallation = self._ConfirmSelfServiceKeyInstallation(api_obj=self._api_obj, url=f'{self._url}/ConfirmSelfServiceKeyInstallation')
        self.DeleteUnmatchedKeyset = self._DeleteUnmatchedKeyset(api_obj=self._api_obj, url=f'{self._url}/DeleteUnmatchedKeyset')
        self.Devices = self._Devices(api_obj=self._api_obj, url=f'{self._url}/Devices')
        self.EditKeyOptions = self._EditKeyOptions(api_obj=self._api_obj, url=f'{self._url}/EditKeyOptions')
        self.EditSelfServiceAuthorizedKey = self._EditSelfServiceAuthorizedKey(api_obj=self._api_obj, url=f'{self._url}/EditSelfServiceAuthorizedKey')
        self.ExportSelfServiceAuthorizedKey = self._ExportSelfServiceAuthorizedKey(api_obj=self._api_obj, url=f'{self._url}/ExportSelfServiceAuthorizedKey')
        self.ExportSelfServicePrivateKey = self._ExportSelfServicePrivateKey(api_obj=self._api_obj, url=f'{self._url}/ExportSelfServicePrivateKey')
        self.ImportAuthorizedKey = self._ImportAuthorizedKey(api_obj=self._api_obj, url=f'{self._url}/ImportAuthorizedKey')
        self.ImportKeyUsageData = self._ImportKeyUsageData(api_obj=self._api_obj, url=f'{self._url}/ImportKeyUsageData')
        self.ImportPrivateKey = self._ImportPrivateKey(api_obj=self._api_obj, url=f'{self._url}/ImportPrivateKey')
        self.KeyDetails = self._KeyDetails(api_obj=self._api_obj, url=f'{self._url}/KeyDetails')
        self.KeysetDetails = self._KeysetDetails(api_obj=self._api_obj, url=f'{self._url}/KeysetDetails')
        self.KeyUsage = self._KeyUsage(api_obj=self._api_obj, url=f'{self._url}/KeyUsage')
        self.MoveKeysetsToPolicy = self._MoveKeysetsToPolicy(api_obj=self._api_obj, url=f'{self._url}/MoveKeysetsToPolicy')
        self.RejectKeyOperation = self._RejectKeyOperation(api_obj=self._api_obj, url=f'{self._url}/RejectKeyOperation')
        self.RemoveKey = self._RemoveKey(api_obj=self._api_obj, url=f'{self._url}/RemoveKey')
        self.RetryKeyOperation = self._RetryKeyOperation(api_obj=self._api_obj, url=f'{self._url}/RetryKeyOperation')
        self.RetryRotation = self._RetryRotation(api_obj=self._api_obj, url=f'{self._url}/RetryRotation')
        self.Rotate = self._Rotate(api_obj=self._api_obj, url=f'{self._url}/Rotate')
        self.SetUnmatchedKeysetPassPhrase = self._SetUnmatchedKeysetPassPhrase(api_obj=self._api_obj, url=f'{self._url}/SetUnmatchedKeysetPassPhrase')
        self.SkipKeyRotation = self._SkipKeyRotation(api_obj=self._api_obj, url=f'{self._url}/SkipKeyRotation')
        self.TestDeviceConnection = self._TestDeviceConnection(api_obj=self._api_obj, url=f'{self._url}/TestDeviceConnection')
        self.Widget = self._Widget(api_obj=self._api_obj, url=f'{self._url}/Widget')

    class _AddAuthorizedKey(WebSdkEndpoint):
        # noinspection ALL
        def post(self, device_guid: str, filepath: str, keyset_id: str, username: str, allowed_source_restriction: List[str] = None,
                 denied_source_restriction: List[str] = None, forced_command: str = None, format: str = None, 
                 options: List[str] = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'DeniedSourceRestriction' : denied_source_restriction,
                'DeviceGuid'              : device_guid,
                'Filepath'                : filepath,
                'ForcedCommand'           : forced_command,
                'Format'                  : format,
                'KeysetId'                : keyset_id,
                'Options'                 : options,
                'Username'                : username
            }

            class Output(WebSdkOutputModel):
                key_id: int = ApiField(alias='KeyId')
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _AddHostPrivateKey(WebSdkEndpoint):
        # noinspection ALL
        def post(self, device_guid: str, filepath: str, username: str, format: str = None, policy_dn: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath'  : filepath,
                'Format'    : format,
                'Username'  : username,
                'PolicyDN'  : policy_dn
            }

            class Output(WebSdkOutputModel):
                key_id: int = ApiField(alias='KeyId')
                keyset_id: str = ApiField(alias='KeysetId')
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _AddKnownHostKey(WebSdkEndpoint):
        # noinspection ALL
        def post(self, device_guid: str, filepath: str, keyset_id: str, username: str, format: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath'  : filepath,
                'Format'    : format,
                'KeysetId'  : keyset_id,
                'Username'  : username
            }

            class Output(WebSdkOutputModel):
                key_id: int = ApiField(alias='KeyId')
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _AddSelfServiceAuthorizedKey(WebSdkEndpoint):
        def post(self, allowed_source_restriction: List[str], denied_source_restriction: List[str], folder_id: str, location: str, 
                 notes: str, options: List[str], owner: str, contact_email: str = None, forced_command: str = None, 
                 keyset_id: str = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'ContactEmail'            : contact_email,
                'DeniedSourceRestriction' : denied_source_restriction,
                'FolderId'                : folder_id,
                'ForcedCommand'           : forced_command,
                'KeysetId'                : keyset_id,
                'Location'                : location,
                'Notes'                   : notes,
                'Options'                 : options,
                'Owner'                   : owner
            }

            class Output(WebSdkOutputModel):
                key_id: int = ApiField(alias='KeyId')
                keyset_id: str = ApiField(alias='KeysetId')
                notes: str = ApiField(alias='Notes')
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _AddSelfServicePrivateKey(WebSdkEndpoint):
        def post(self, folder_id: str, location: str, notes: str, owner: str, contact_email: str = None, keyset_id: str = None):
            body = {
                'ContactEmail': contact_email,
                'FolderId'    : folder_id,
                'KeysetId'    : keyset_id,
                'Location'    : location,
                'Notes'       : notes,
                'Owner'       : owner
            }

            class Output(WebSdkOutputModel):
                key_id: int = ApiField(alias='KeyId')
                keyset_id: str = ApiField(alias='KeysetId')
                notes: str = ApiField(alias='Notes')
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _AddUserPrivateKey(WebSdkEndpoint):
        # noinspection ALL
        def post(self, device_guid: str, filepath: str, username: str, format: str = None, keyset_id: str = None,
                 passphrase: str = None, policy_dn: str = None):
            body = {
                'DeviceGuid': device_guid,
                'Filepath'  : filepath,
                'Format'    : format,
                'KeysetId'  : keyset_id,
                'Passphrase': passphrase,
                'Username'  : username,
                'PolicyDN'  : policy_dn
            }

            class Output(WebSdkOutputModel):
                key_id: int = ApiField(alias='KeyId')
                keyset_id: str = ApiField(alias='KeysetId')
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _ApproveKeyOperation(WebSdkEndpoint):
        def post(self, key_id: int, comment: str):
            body = {
                'KeyId'  : key_id,
                'Comment': comment
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _CancelKeyOperation(WebSdkEndpoint):
        def post(self, key_id: int):
            body = {
                'KeyId': key_id
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _CancelRotation(WebSdkEndpoint):
        def post(self, keyset_id: str):
            body = {
                'KeysetId': keyset_id
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _ChangePrivateKeyPassphrase(WebSdkEndpoint):
        def post(self, key_id: int, passphrase: str):
            body = {
                'KeysetId'  : key_id,
                'Passphrase': passphrase
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _ConfirmSelfServiceKeyInstallation(WebSdkEndpoint):
        def post(self, keyset_id: str):
            body = {
                'KeysetId': keyset_id
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _DeleteUnmatchedKeyset(WebSdkEndpoint):
        def post(self, unmatched_trust_id: str):
            body = {
                'UnmatchedTrustId': unmatched_trust_id
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Devices(WebSdkEndpoint):
        def post(self, page_size: int, offset: int = None, ssh_device_filter: Union[dict, ssh.SshDeviceFilter] = None):
            body = {
                'PageSize'       : page_size,
                'Offset'         : offset,
                'SshDeviceFilter': ssh_device_filter
            }

            class Output(WebSdkOutputModel):
                data: List[ssh.DeviceData] = ApiField(default_factory=list, alias='Data')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _EditKeyOptions(WebSdkEndpoint):
        def post(self, key_id: int, allowed_source_restriction: List[str] = None, denied_source_restriction: List[str] = None,
                 forced_command: str = None, options: List[str] = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'DeniedSourceRestriction' : denied_source_restriction,
                'ForcedCommand'           : forced_command,
                'KeyId'                   : key_id,
                'Options'                 : options
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _EditSelfServiceAuthorizedKey(WebSdkEndpoint):
        def post(self, key_id: int, allowed_source_restriction: List[str] = None,
                 denied_source_restriction: List[str] = None, forced_command: str = None,
                 location: str = None, notes: str = None, options: List[str] = None):
            body = {
                'AllowedSourceRestriction': allowed_source_restriction,
                'DeniedSourceRestriction' : denied_source_restriction,
                'ForcedCommand'           : forced_command,
                'KeyId'                   : key_id,
                'Location'                : location,
                'Notes'                   : notes,
                'Options'                 : options
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _ExportSelfServiceAuthorizedKey(WebSdkEndpoint):
        # noinspection ALL
        def post(self, key_id: int, format: str = None):
            body = {
                'KeyId' : key_id,
                'Format': format
            }

            class Output(WebSdkOutputModel):
                key_material: str = ApiField(alias='KeyMaterial')
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _ExportSelfServicePrivateKey(WebSdkEndpoint):
        # noinspection ALL
        def post(self, key_id: int, format: str = None, passphrase: str = None):
            body = {
                'KeyId'     : key_id,
                'Format'    : format,
                'Passphrase': passphrase
            }

            class Output(WebSdkOutputModel):
                key_material: str = ApiField(alias='KeyMaterial')
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _ImportAuthorizedKey(WebSdkEndpoint):
        # noinspection ALL
        def post(self, device_guid: str, filepath: str, format: str, key_content_base_64: str, username: str):
            body = {
                'DeviceGuid'      : device_guid,
                'Filepath'        : filepath,
                'Format'          : format,
                'KeyContentBase64': key_content_base_64,
                'Username'        : username
            }

            class Output(WebSdkOutputModel):
                key_id: int = ApiField(alias='KeyId')
                response: ssh.SshWebResponse = ApiField(alias='SshWebResponse')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _ImportKeyUsageData(WebSdkEndpoint):
        def post(self, log_data: List[ssh.LogData]):
            body = {
                'LogData': log_data
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='SshWebResponse')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _ImportPrivateKey(WebSdkEndpoint):
        # noinspection ALL
        def post(self, device_guid: str, filepath: str, format: str, key_content_base_64: str, username: str,
                 passphrase: str = None):
            body = {
                'DeviceGuid'      : device_guid,
                'Filepath'        : filepath,
                'Format'          : format,
                'KeyContentBase64': key_content_base_64,
                'Passphrase'      : passphrase,
                'Username'        : username
            }

            class Output(WebSdkOutputModel):
                key_id: int = ApiField(alias='KeyId')
                response: ssh.SshWebResponse = ApiField(alias='SshWebResponse')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _KeyDetails(WebSdkEndpoint):
        def post(self, key_id: int):
            body = {
                'KeyId': key_id
            }

            class Output(WebSdkOutputModel):
                key_data: List[ssh.KeyData] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data=body), root_field='key_data')

    class _KeysetDetails(WebSdkEndpoint):
        def get(self, keyset_id: str, load_key_data: bool = None):
            params = {
                'KeysetId'   : keyset_id,
                'LoadKeyData': load_key_data
            }

            class Output(WebSdkOutputModel):
                pass

            # This cannot be inherited as that method is broken. Instead, manually update the fields.
            Output.__fields__.update(ssh.KeySetData.__fields__)

            return generate_output(output_cls=Output, response=self._get(params=params))

        def post(self, page_size: int, keyset_filter: List[ssh.KeySetFilter] = None, load_key_data: bool = None,
                 offset: int = None):
            body = {
                'KeysetFilter': keyset_filter,
                'LoadKeyData' : load_key_data,
                'Offset'      : offset,
                'PageSize'    : page_size
            }

            class Output(WebSdkOutputModel):
                data: List[ssh.KeySetData] = ApiField(default_factory=list, alias='Data')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _KeyUsage(WebSdkEndpoint):
        def post(self, ssh_key_usage_filter: List[ssh.KeyUsageFilter], page_size: int = None, offset: int = None):
            body = {
                'SshKeyUsageFilter': ssh_key_usage_filter,
                'PageSize'         : page_size,
                'Offset'           : offset
            }

            class Output(WebSdkOutputModel):
                data: List[ssh.KeyUsageData] = ApiField(default_factory=list, alias='Data')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _MoveKeysetsToPolicy(WebSdkEndpoint):
        def post(self, keyset_ids: List[str], policy_dn: str = None, policy_path: str = None):
            body = {
                'KeysetIds' : keyset_ids,
                'PolicyDN'  : policy_dn,
                'PolicyPath': policy_path
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _RejectKeyOperation(WebSdkEndpoint):
        def post(self, key_id: int, comment: str):
            body = {
                'KeyId'  : key_id,
                'Comment': comment
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _RemoveKey(WebSdkEndpoint):
        def post(self, key_id: int):
            body = {
                'KeyId': key_id
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _RetryKeyOperation(WebSdkEndpoint):
        def post(self, key_id: int):
            body = {
                'KeyId': key_id
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _RetryRotation(WebSdkEndpoint):
        def post(self, keyset_id: str):
            body = {
                'KeysetId': keyset_id
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _Rotate(WebSdkEndpoint):
        def post(self, keyset_id: str, options: int = None, allow_skip_on_rotation: bool = None):
            body = {
                'KeysetId'           : keyset_id,
                'AllowSkipOnRotation': allow_skip_on_rotation,
                'Options'            : options
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _SetUnmatchedKeysetPassPhrase(WebSdkEndpoint):
        def post(self, passphrase: str, unmatched_trust_id: str):
            body = {
                'Passphrase'      : passphrase,
                'UnmatchedTrustId': unmatched_trust_id
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _SkipKeyRotation(WebSdkEndpoint):
        def post(self, key_id: int):
            body = {
                'KeyId': key_id
            }

            class Output(WebSdkOutputModel):
                response: ssh.SshWebResponse = ApiField(alias='Response')

            return generate_output(output_cls=Output, response=self._post(data=body))

    class _TestDeviceConnection(WebSdkEndpoint):
        def post(self, device_guids: List[str]):
            body = {
                'deviceGuids': device_guids
            }

            class Output(WebSdkOutputModel):
                connection_results: List[ssh.ConnectionResult] = ApiField(default_factory=list)

            return generate_output(output_cls=Output, response=self._post(data=body), root_field='connection_results')

    class _Widget(WebSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.CriticalAlerts = self._CriticalAlerts(api_obj=self._api_obj, url=f'{self._url}/CriticalAlerts')
            self.PolicyViolations = self._PolicyViolations(api_obj=self._api_obj, url=f'{self._url}/PolicyViolations')
            self.Stats = self._Stats(api_obj=self._api_obj, url=f'{self._url}/Stats')

        class _CriticalAlerts(WebSdkEndpoint):
            def get(self, min_allowed_key_length: int):
                params = {
                    'minAllowedKeyLength': min_allowed_key_length
                }

                class Output(WebSdkOutputModel):
                    accessible_root_accounts: int = ApiField(alias='AccessibleRootAccounts')
                    non_compliant_duplicate_private_keys: int = ApiField(alias='NonCompliantDuplicatePrivateKeys')
                    non_root_orphans: int = ApiField(alias='NonRootOrphans')
                    root_orphans: int = ApiField(alias='RootOrphans')
                    shared_private_keys: int = ApiField(alias='SharedPrivateKeys')
                    very_small_key: int = ApiField(alias='VerySmallKey')

                return generate_output(output_cls=Output, response=self._get(params=params))

        class _PolicyViolations(WebSdkEndpoint):
            def get(self):
                class Output(WebSdkOutputModel):
                    duplicate_private_keys: List[str] = ApiField(alias='DuplicatePrivateKeys', default_factory=list)
                    key_older_than_policy: str = ApiField(alias='KeyOlderThanPolicy')
                    key_smaller_than_policy: str = ApiField(alias='KeySmallerThanPolicy')
                    missing_options: List[str] = ApiField(alias='MissingOptions', default_factory=list)
                    non_compliant_algorithm: str = ApiField(alias='NonCompliantAlgorithm')
                    non_compliant_force_command: str = ApiField(alias='NonCompliantForceCommand')
                    non_compliant_source_restriction: str = ApiField(alias='NonCompliantSourceRestriction')
                    non_compliant_vendor_format: str = ApiField(alias='NonCompliantVendorFormat')
                    root_access: str = ApiField(alias='RootAccess')
                    shared_server_account: str = ApiField(alias='SharedServerAccount')
                    vulnerable_protocol: str = ApiField(alias='VulnerableProtocol')

                return generate_output(output_cls=Output, response=self._get())

        class _Stats(WebSdkEndpoint):
            def get(self, group_by: str):
                params = {
                    'GroupBy': group_by
                }

                class Output(WebSdkOutputModel):
                    stats: Dict[str, Any] = ApiField()

                return generate_output(output_cls=Output, response=self._get(params=params),
                                       root_field='stats')
