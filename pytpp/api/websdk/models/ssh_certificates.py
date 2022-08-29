from __future__ import annotations
from typing import List
from pytpp.api.api_base import ObjectModel, ApiField


class Output(ObjectModel):
    success: bool = ApiField(alias='Success')
    error_code: int = ApiField(alias='ErrorCode')
    error_message: str = ApiField(alias='ErrorMessage')


class ProcessingDetails(ObjectModel):
    status: str = ApiField(alias='Status')
    status_description: str = ApiField(alias='StatusDescription')


class CertificateDetails(ObjectModel):
    ca_fingerprint_sha256: str = ApiField(alias='CaFingerprintSha256')
    certificate_fingerprint_sha256: str = ApiField(alias='CertificateFingerprintSha256')
    certificate_type: str = ApiField(alias='CertificateType')
    extensions: dict = ApiField(alias='Extensions')
    key_id: str = ApiField(alias='KeyId')
    key_type: str = ApiField(alias='KeyType')
    principals: List[str] = ApiField(alias='Principals', default_factory=list)
    public_key_fingerprint_sha256: str = ApiField(alias='PublicKeyFingerprintSha256')
    serial_number: str = ApiField(alias='SerialNumber')
    source_addresses: List[str] = ApiField(alias='SourceAddresses', default_factory=list)
    valid_from: int = ApiField(alias='ValidFrom')
    valid_to: int = ApiField(alias='ValidTo')


class RequestDetails(ObjectModel):
    originating_ip: str = ApiField(alias='OriginatingIp')
    requested_by: str = ApiField(alias='RequestedBy')


class AccessControl(ObjectModel):
    allowed_certificate_identifier_patterns: List[str] = ApiField(alias='AllowedCertificateIdentifierPatterns', default_factory=list)
    allowed_extensions: List[str] = ApiField(alias='AllowedExtensions', default_factory=list)
    allowed_force_command_patterns: List[str] = ApiField(alias='AllowedForceCommandPatterns', default_factory=list)
    allowed_principals_patterns: List[str] = ApiField(alias='AllowedPrincipalsPatterns', default_factory=list)
    allowed_source_addresses: List[str] = ApiField(alias='AllowedSourceAddresses', default_factory=list)
    default_certificate_identifier: str = ApiField(alias='DefaultCertificateIdentifier')
    default_extensions: List[str] = ApiField(alias='DefaultExtensions', default_factory=list)
    default_force_command: str = ApiField(alias='DefaultForceCommand')
    default_principals: List[str] = ApiField(alias='DefaultPrincipals', default_factory=list)
    default_source_addresses: List[str] = ApiField(alias='DefaultSourceAddresses', default_factory=list)


class APIClient(ObjectModel):
    allowed_to_request_certificate_identifier: bool = ApiField(alias='AllowedToRequestCertificateIdentifier')
    allowed_to_request_extensions: bool = ApiField(alias='AllowedToRequestExtensions')
    allowed_to_request_force_command: bool = ApiField(alias='AllowedToRequestForceCommand')
    allowed_to_request_principals: bool = ApiField(alias='AllowedToRequestPrincipals')
    allowed_to_request_source_addresses: bool = ApiField(alias='AllowedToRequestSourceAddresses')


class Certificate(ObjectModel):
    allowed_private_key_algorithms: List[str] = ApiField(alias='AllowedPrivateKeyAlgorithms', default_factory=list)
    allowed_private_key_reuse: bool = ApiField(alias='AllowedPrivateKeyReuse')
    certificate_destination_dn: str = ApiField(alias='CertificateDestinationDn')
    default_private_key_algorithm: str = ApiField(alias='DefaultPrivateKeyAlgorithm')
    signature_hashing_algorithm: str = ApiField(alias='SignatureHashingAlgorithm')
    type: str = ApiField(alias='Type')
    validity_period: str = ApiField(alias='ValidityPeriod')


class CAKeyPair(ObjectModel):
    created_on: str = ApiField(alias='CreatedOn')
    dn: str = ApiField(alias='Dn')
    fingerprint_sha256: str = ApiField(alias='FingerprintSha256')
    guid: str = ApiField(alias='Guid')
    key_algorithm: str = ApiField(alias='KeyAlgorithm')
    name: str = ApiField(alias='Name')
    public_key_data: str = ApiField(alias='PublicKeyData')
