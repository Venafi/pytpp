from pytpp.properties.response_objects.dataclasses import ssh_certificates
from pytpp.properties.resultcodes import ResultCodes


class SSHCertificate:
    @staticmethod
    def Response(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}

        error_code = response_object.get('ErrorCode')
        return ssh_certificates.Response(
            success=response_object.get('Success'),
            error_code=error_code,
            error_message=ResultCodes.SSHErrorCodes.get(error_code, 'Unknown') if error_code else None,
        )

    @staticmethod
    def ProcessingDetails(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh_certificates.ProcessingDetails(
            status=response_object.get('Status'),
            status_description=response_object.get('StatusDescription'),
        )

    @staticmethod
    def CertificateDetails(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh_certificates.CertificateDetails(
            ca_fingerprint_sha256=response_object.get('CAFingerprintSHA256'),
            certificate_fingerprint_sha256=response_object.get('CertificateFingerprintSHA256'),
            certificate_type=response_object.get('CertificateType'),
            extensions=response_object.get('Extensions'),
            key_id=response_object.get('KeyID'),
            key_type=response_object.get('KeyType'),
            principals=response_object.get('Principals'),
            public_key_fingerprint_sha256=response_object.get('PublicKeyFingerprintSHA256'),
            serial_number=response_object.get('SerialNumber'),
            valid_from=response_object.get('ValidFrom'),
            valid_to=response_object.get('ValidTo'),
        )

    @staticmethod
    def RequestDetails(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh_certificates.RequestDetails(
            originating_ip=response_object.get('OriginatingIP'),
            requested_by=response_object.get('RequestedBy'),
        )

    @staticmethod
    def APIClient(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh_certificates.APIClient(
            allowed_to_request_certificate_identifier=response_object.get('AllowedToRequestCertificateIdentifier'),
            allowed_to_request_extensions=response_object.get('AllowedToRequestExtensions'),
            allowed_to_request_force_command=response_object.get('AllowedToRequestForceCommand'),
            allowed_to_request_principals=response_object.get('AllowedToRequestPrincipals'),
            allowed_to_request_source_addresses=response_object.get('AllowedToRequestSourceAddresses'),
        )

    @staticmethod
    def Certificate(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh_certificates.Certificate(
            allowed_private_key_algorithms=response_object.get('AllowedPrivateKeyAlgorithms'),
            allowed_private_key_reuse=response_object.get('AllowedPrivateKeyReuse'),
            certificate_destination_dn=response_object.get('CertificateDestinationDn'),
            default_private_key_algorithm=response_object.get('DefaultPrivateKeyAlgorithm'),
            signature_hashing_algorithm=response_object.get('SignatureHashingAlgorithm'),
            type=response_object.get('Type'),
            validity_period=response_object.get('ValidityPeriod'),
        )

    @staticmethod
    def CAKeyPair(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return ssh_certificates.CAKeyPair(
            created_on=response_object.get('CreatedOn'),
            dn=response_object.get('DN'),
            fingerprint_sha256=response_object.get('FingerprintSHA256'),
            guid=response_object.get('Guid'),
            key_algorithm=response_object.get('KeyAlgorithm'),
            name=response_object.get('Name'),
            public_key_data=response_object.get('PublicKeyData'),
        )
