from pytpp.properties.response_objects.dataclasses import ssh
from pytpp.properties.resultcodes import ResultCodes
from pytpp.tools.helpers.date_converter import from_date_string


class SSH:
    @staticmethod
    def Response(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        error_code = response_object.get('ErrorCode')
        return ssh.Response(
            success=response_object.get('Success'),
            error_code=error_code,
            error_message=ResultCodes.SSHErrorCodes.get(error_code, 'Unknown') if error_code else None,
        )

    @staticmethod
    def ConnectionResult(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh.ConnectionResult(
            device_guid=response_object.get('DeviceGuid'),
            error=response_object.get('Error'),
            success=response_object.get('Success'),
        )

    @staticmethod
    def DeviceData(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh.DeviceData(
            dn=response_object.get('DN'),
            device_guid=response_object.get('DeviceGuid'),
            host_name=response_object.get('HostName'),
            is_compliant=response_object.get('IsCompliant'),
            type=response_object.get('Type'),
        )

    @staticmethod
    def KeyData(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh.KeyData(
            active_from=from_date_string(response_object.get('ActiveFrom')),
            algorithm=response_object.get('Algorithm'),
            allowed_source_restriction=response_object.get('AllowedSourceRestriction'),
            approver=response_object.get('Approver'),
            comment=response_object.get('Comment'),
            denied_source_restriction=response_object.get('DeniedSourceRestriction'),
            device_guid=response_object.get('DeviceGuid'),
            filepath=response_object.get('Filepath'),
            forced_command=response_object.get('ForcedCommand'),
            format=response_object.get('Format'),
            is_encrypted=response_object.get('IsEncrypted'),
            key_id=response_object.get('KeyId'),
            keysetid=response_object.get('KeysetId'),
            last_used=from_date_string(response_object.get('LastUsed')),
            length=response_object.get('Length'),
            notes=response_object.get('Notes'),
            options=response_object.get('Options'),
            process_error=response_object.get('ProcessError'),
            process_status=response_object.get('ProcessStatus'),
            reason=response_object.get('Reason'),
            rotation_stage=response_object.get('RotationStage'),
            type=response_object.get('Type'),
            username=response_object.get('Username'),
            violation_status=response_object.get('ViolationStatus'),
        )

    @staticmethod
    def KeySetData(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh.KeySetData(
            access=response_object.get('Access'),
            algorithm=response_object.get('Algorithm'),
            fingerprint_md5=response_object.get('FingerprintMD5'),
            fingerprint_sha256=response_object.get('FingerprintSHA256'),
            keysetid=response_object.get('KeysetId'),
            last_rotation_date=from_date_string(response_object.get('LastRotationDate')),
            last_used=from_date_string(response_object.get('LastUsed')),
            length=response_object.get('Length'),
            private_keys=[SSH.KeyData(data) for data in
                          response_object.get('PrivateKeys')] if 'PrivateKeys' in response_object.keys() else [],
            process_error=response_object.get('ProcessError'),
            process_status=response_object.get('ProcessStatus'),
            public_keys=[SSH.KeyData(data) for data in
                         response_object.get('PublicKeys')] if 'PublicKeys' in response_object.keys() else [],
            rotation_stage=response_object.get('RotationStage'),
            type=response_object.get('Type'),
            violation_status=response_object.get('ViolationStatus'),
        )

    @staticmethod
    def KeyUsageData(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh.KeyUsageData(
            alert=response_object.get('Alert'),
            authorized_key_id=response_object.get('AuthorizedKeyId'),
            client_name=response_object.get('ClientName'),
            fingerprint=response_object.get('Fingerprint'),
            key_usage_id=response_object.get('KeyUsageId'),
            keyset_id=response_object.get('KeysetId'),
            last_used=response_object.get('LastUsed'),
            private_key_id=response_object.get('PrivateKeyId'),
            server_account=response_object.get('ServerAccount'),
            server_name=response_object.get('ServerName'),
        )
