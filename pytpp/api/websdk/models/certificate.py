from __future__ import annotations
from pytpp.api.api_base import ObjectModel, ApiField
from datetime import datetime
from typing import List, Literal

CertificateFormat = Literal['Base64', 'Base64 (PKCS #8)', 'DER', 'JKS', 'PKCS #7', 'PKCS #12']


class Link(ObjectModel):
    details: str = ApiField(alias='Details')
    next: str = ApiField(alias='Next')
    previous: str = ApiField(alias='Previous')


class CertificateDetails(ObjectModel):
    aia_ca_issuer_url: List[str] = ApiField(alias='AIACAIssuerURL', default_factory=list)
    aia_key_identifier: str = ApiField(alias='AIAKeyIdentifier')
    c: str = ApiField(alias='C')
    cdp_uri: str = ApiField(alias='CDPURI')
    cn: str = ApiField(alias='CN')
    elliptic_curve: str = ApiField(alias='EllipticCurve')
    enhanced_key_usage: str = ApiField(alias='EnhancedKeyUsage')
    issuer: str = ApiField(alias='Issuer')
    key_algorithm: str = ApiField(alias='KeyAlgorithm')
    key_size: int = ApiField(alias='KeySize')
    key_usage: str = ApiField(alias='KeyUsage')
    l: str = ApiField(alias='L')
    o: str = ApiField(alias='O')
    ou: List[str] = ApiField(alias='OU', default_factory=list)
    public_key_hash: str = ApiField(alias='PublicKeyHash')
    revocation_date: datetime = ApiField(alias='RevocationDate')
    revocation_status: str = ApiField(alias='RevocationStatus')
    s: str = ApiField(alias='S')
    ski_key_identifier: str = ApiField(alias='SKIKeyIdentifier')
    serial: str = ApiField(alias='Serial')
    signature_algorithm: str = ApiField(alias='SignatureAlgorithm')
    signature_algorithm_oid: str = ApiField(alias='SignatureAlgorithmOID')
    store_added: datetime = ApiField(alias='StoreAdded')
    subject: str = ApiField(alias='Subject')
    subject_alt_name_dns: List[str] = ApiField(alias='SubjectAltNameDNS', default_factory=list)
    subject_alt_name_email: List[str] = ApiField(alias='SubjectAltNameEmail', default_factory=list)
    subject_alt_name_ip_address: List[str] = ApiField(alias='SubjectAltNameIPAddress', default_factory=list)
    subject_alt_name_other_name_upn: List[str] = ApiField(alias='SubjectAltNameOtherNameUPN', default_factory=list)
    subject_alt_name_uri: List[str] = ApiField(alias='SubjectAltNameUri', default_factory=list)
    template_major_version: str = ApiField(alias='TemplateMajorVersion')
    template_minor_version: str = ApiField(alias='TemplateMajorVersion')
    template_name: str = ApiField(alias='TemplateName')
    template_oid: str = ApiField(alias='TemplateOID')
    thumbprint: str = ApiField(alias='Thumbprint')
    valid_from: datetime = ApiField(alias='ValidFrom')
    valid_to: datetime = ApiField(alias='ValidTo')


class PreviousVersions(ObjectModel):
    certificate_details: CertificateDetails = ApiField(alias='CertificateDetails')
    vault_id: int = ApiField(alias='VaultId')


class ProcessingDetails(ObjectModel):
    in_error: bool = ApiField(alias='InError')
    stage: int = ApiField(alias='Stage')
    status: str = ApiField(alias='Status')


class RenewalDetails(ObjectModel):
    city: str = ApiField(alias='City')
    country: str = ApiField(alias='Country')
    organization: str = ApiField(alias='Organization')
    organizational_unit: List[str] = ApiField(alias='OrganizationalUnit', default_factory=list)
    state: str = ApiField(alias='State')
    subject: str = ApiField(alias='Subject')
    subject_alt_name_dns: List[str] = ApiField(alias='SubjectAltNameDns', default_factory=list)
    subject_alt_name_email: List[str] = ApiField(alias='SubjectAltNameEmail', default_factory=list)
    subject_alt_name_ip_address: List[str] = ApiField(alias='SubjectAltNameIpAddress', default_factory=list)
    subject_alt_name_other_name_upn: List[str] = ApiField(alias='SubjectAltNameOtherNameUpn', default_factory=list)
    subject_alt_name_uri: List[str] = ApiField(alias='SubjectAltNameUri', default_factory=list)
    valid_from: datetime = ApiField(alias='ValidFrom')
    valid_to: datetime = ApiField(alias='ValidTo')


class ValidationDetails(ObjectModel):
    last_validation_state_update: str = ApiField(alias='LastValidationStateUpdate')
    validation_state: str = ApiField(alias='ValidationState')


class File(ObjectModel):
    installation: str = ApiField(alias='Installation')
    performed_on: datetime = ApiField(alias='PerformedOn')
    result: List[str] = ApiField(alias='Result', default_factory=list)


class BitMaskValues(ObjectModel):
    bitmask: int = ApiField(alias='Bitmask')
    values: List[str] = ApiField(alias='Values', default_factory=list)


class SANS(ObjectModel):
    dns: List[str] = ApiField(alias='Dns', default_factory=list)
    ip: List[str] = ApiField(alias='Ip', default_factory=list)


class Compliant(ObjectModel):
    compliant: bool = ApiField(alias='Compliant')


class CompliantSingleValue(Compliant):
    value: str = ApiField(alias='Value')


class CompliantMultiValue(Compliant):
    values: List[str] = ApiField(alias='Values', default_factory=list)


class Locked(ObjectModel):
    locked: bool = ApiField(alias='Locked')


class LockedSingleValue(Locked):
    value: str = ApiField(alias='Value')


class LockedMultiValue(Locked):
    values: list = ApiField(alias='Values')


class LockedKeyPair(ObjectModel):
    key_algorithm: LockedSingleValue = ApiField(alias='KeyAlgorithm')
    key_size: LockedSingleValue = ApiField(alias='KeySize')


class LockedSubject(ObjectModel):
    city: LockedSingleValue = ApiField(alias='City')
    country: LockedSingleValue = ApiField(alias='Country')
    organization: LockedSingleValue = ApiField(alias='Organization')
    organizational_units: LockedMultiValue = ApiField(alias='OrganizationalUnits')
    state: LockedSingleValue = ApiField(alias='State')


class CSRDetails(ObjectModel):
    city: CompliantSingleValue = ApiField(alias='City')
    common_name: CompliantSingleValue = ApiField(alias='CommonName')
    country: CompliantSingleValue = ApiField(alias='Country')
    key_algorithm: CompliantSingleValue = ApiField(alias='KeyAlgorithm')
    key_size: CompliantSingleValue = ApiField(alias='KeySize')
    organization: CompliantSingleValue = ApiField(alias='Organization')
    organizational_unit: CompliantMultiValue = ApiField(alias='OrganizationalUnit')
    private_key_reused: CompliantSingleValue = ApiField(alias='PrivateKeyReused')
    state: CompliantSingleValue = ApiField(alias='State')
    subj_alt_name_dns: CompliantMultiValue = ApiField(alias='SubjAltNameDns')
    subj_alt_name_email: CompliantMultiValue = ApiField(alias='SubjAltNameEmail')
    subj_alt_name_ip: CompliantMultiValue = ApiField(alias='SubjAltNameIp')
    subj_alt_name_upn: CompliantMultiValue = ApiField(alias='SubjAltNameUpn')
    subj_alt_name_uri: CompliantMultiValue = ApiField(alias='SubjAltNameUri')


class NameValue(ObjectModel):
    name: str = ApiField(alias='Name')
    value: str = ApiField(alias='Value')


class NameTypeValue(ObjectModel):
    type: str = ApiField(alias='Type')
    name: str = ApiField(alias='Name')
    value: str = ApiField(alias='Value')


class SslTlsResult(ObjectModel):
    chain: BitMaskValues = ApiField(alias='Chain')
    end_entity: BitMaskValues = ApiField(alias='EndEntity')
    id: int = ApiField(alias='Id')
    protocols: BitMaskValues = ApiField(alias='Protocols')


class SslTls(ObjectModel):
    host: str = ApiField(alias='Host')
    ip_address: str = ApiField(alias='IpAddress')
    port: int = ApiField(alias='Port')
    result: SslTlsResult = ApiField(alias='Result')
    sources: List[str] = ApiField(alias='Sources', default_factory=list)


class Policy(ObjectModel):
    certificate_authority: LockedSingleValue = ApiField(alias='CertificateAuthority')
    csr_generation: LockedSingleValue = ApiField(alias='CsrGeneration')
    management_type: LockedSingleValue = ApiField(alias='ManagementType')
    key_generation: LockedSingleValue = ApiField(alias='KeyGeneration')
    key_pair: LockedKeyPair = ApiField(alias='KeyPair')
    private_key_reuse_allowed: bool = ApiField(alias='PrivateKeyReuseAllowed')
    subj_alt_name_dns_allowed: bool = ApiField(alias='SubjAltNameDnsAllowed')
    subj_alt_name_email_allowed: bool = ApiField(alias='SubjAltNameEmailAllowed')
    subj_alt_name_ip_allowed: bool = ApiField(alias='SubjAltNameIpAllowed')
    subj_alt_name_upn_allowed: bool = ApiField(alias='SubjAltNameUpnAllowed')
    subj_alt_name_uri_allowed: bool = ApiField(alias='SubjAltNameUriAllowed')
    subject: LockedSubject = ApiField(alias='Subject')
    unique_subject_enforced: bool = ApiField(alias='UniqueSubjectEnforced')
    whitelisted_domains: List[str] = ApiField(alias='WhitelistedDomains', default_factory=list)
    wildcards_allowed: bool = ApiField(alias='WildcardsAllowed')


class CSR(ObjectModel):
    details: CSRDetails = ApiField('Details')
    enrollable: bool = ApiField('Enrollable')


class X509(ObjectModel):
    cn: str = ApiField(alias='Cn')
    issuer: str = ApiField(alias='Issuer')
    key_algorithm: str = ApiField(alias='KeyAlgorithm')
    key_size: int = ApiField(alias='KeySize')
    sans: SANS = ApiField(alias='Sans')
    serial: str = ApiField(alias='Serial')
    subject: str = ApiField(alias='Subject')
    thumbprint: str = ApiField(alias='Thumbprint')
    valid_from: datetime = ApiField(alias='ValidFrom')
    valid_to: datetime = ApiField(alias='ValidTo')


class Certificate(ObjectModel):
    created_on: datetime = ApiField(alias='CreatedOn')
    dn: str = ApiField(alias='DN')
    guid: str = ApiField(alias='Guid')
    name: str = ApiField(alias='Name')
    parent_dn: str = ApiField(alias='ParentDn')
    schema_class: str = ApiField(alias='SchemaClass')
    x509: X509 = ApiField(alias='X509')
    links: List[Link] = ApiField(alias='_links', default_factory=list)


class CertificateFilter(ObjectModel):
    certificate_type: str = ApiField(alias='CertificateType')
    chain_validation_failure: str = ApiField(alias='ChainValidationFailure')
    cn: str = ApiField(alias='CN')
    country: str = ApiField(alias='C')
    created_on: datetime = ApiField(alias='CreatedOn')
    created_on_greater: datetime = ApiField(alias='CreatedOnGreater')
    created_on_less: datetime = ApiField(alias='CreatedOnLess')
    disabled: bool = ApiField(alias='Disabled')
    in_error: bool = ApiField(alias='InError')
    is_self_signed: bool = ApiField(alias='IsSelfSigned')
    is_wildcard: bool = ApiField(alias='IsWildcard')
    issuer: str = ApiField(alias='Issuer')
    key_algorithm: str = ApiField(alias='KeyAlgorithm')
    key_size: str = ApiField(alias='KeySize')
    key_size_greater: str = ApiField(alias='KeySizeGreater')
    key_size_less: str = ApiField(alias='KeySizeLess')
    l: str = ApiField(alias='L')
    management_type: str = ApiField(alias='ManagementType')
    name: str = ApiField(alias='Name')
    network_validation_disabled: str = ApiField(alias='NetworkValidationDisabled')
    o: str = ApiField(alias='O')
    ou: str = ApiField(alias='OU')
    parent_dn: str = ApiField(alias='ParentDn')
    parent_dn_recursive: str = ApiField(alias='ParentDnRecursive')
    pending_workflow: bool = ApiField(alias='PendingWorkflow')
    s: str = ApiField(alias='S')
    san_dns: str = ApiField(alias='SAN-DNS')
    san_email: str = ApiField(alias='SAN-Email')
    san_ip: str = ApiField(alias='SAN-IP')
    san_upn: str = ApiField(alias='SAN-UPN')
    san_uri: str = ApiField(alias='SAN-URI')
    serial: str = ApiField(alias='Serial')
    signature_algorithm: str = ApiField(alias='SignatureAlgorithm')
    ssl_tls_protocol: str = ApiField(alias='SslTlsProtocol')
    stage: str = ApiField(alias='Stage')
    stage_greater: str = ApiField(alias='StageGreater')
    stage_less: str = ApiField(alias='StageLess')
    thumbprint: str = ApiField(alias='Thumbprint')
    tls_validation_failure: str = ApiField(alias='TlsValidationFailure')
    valid_from: datetime = ApiField(alias='ValidFrom')
    valid_from_greater: datetime = ApiField(alias='ValidFromGreater')
    valid_from_less: datetime = ApiField(alias='ValidFromLess')
    valid_to: datetime = ApiField(alias='ValidTo')
    valid_to_greater: datetime = ApiField(alias='ValidToGreater')
    valid_to_less: datetime = ApiField(alias='ValidToLess')
    validation_disabled: bool = ApiField(alias='ValidationDisabled')
    validation_state: str = ApiField(alias='ValidationState')
