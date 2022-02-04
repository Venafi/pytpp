from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Certificate:
    created_on: str
    dn: str
    guid: str
    name: str
    parent_dn: str
    schema_class: str
    x509: '_X509'
    links: 'List[Link]'


@dataclass
class Link:
    details: str
    next: str
    previous: str


@dataclass
class CSR:
    details: '_CSRDetails'
    enrollable: bool


@dataclass
class Policy:
    certificate_authority: '_LockedSingleValue'
    csr_generation: '_LockedSingleValue'
    management_type: '_LockedSingleValue'
    key_generation: '_LockedSingleValue'
    key_pair: '_LockedKeyPair'
    private_key_reuse_allowed: bool
    subj_alt_name_dns_allowed: bool
    subj_alt_name_email_allowed: bool
    subj_alt_name_ip_allowed: bool
    subj_alt_name_upn_allowed: bool
    subj_alt_name_uri_allowed: bool
    subject: '_LockedSubject'
    unique_subject_enforced: bool
    whitelisted_domains: list
    wildcards_allowed: bool


@dataclass
class CertificateDetails:
    c: str
    cn: str
    enhanced_key_usage: str
    issuer: str
    key_algorithm: str
    key_size: int
    key_usage: str
    l: str
    o: str
    ou: str
    public_key_hash: str
    s: str
    ski_key_identifier: str
    serial: str
    signature_algorithm: str
    signature_algorithm_oid: str
    store_added: str
    subject: str
    subject_alt_name_dns: str
    subject_alt_name_email: str
    subject_alt_name_ip: str
    subject_alt_name_upn: str
    subject_alt_name_uri: str
    thumbprint: str
    valid_from: 'datetime'
    valid_to: 'datetime'


@dataclass
class PreviousVersions:
    certificate_details: 'CertificateDetails'
    vault_id: int


@dataclass
class ProcessingDetails:
    in_error: bool
    stage: int
    status: str


@dataclass
class RenewalDetails:
    city: str
    country: str
    organization: str
    organizational_unit: str
    state: str
    subject: str
    subject_alt_name_dns: str
    subject_alt_name_email: str
    subject_alt_name_ip_address: str
    subject_alt_name_other_name_upn: str
    subject_alt_name_uri: str
    valid_from: 'datetime'
    valid_to: 'datetime'


@dataclass
class ValidationDetails:
    last_validation_state_update: str
    validation_state: str


@dataclass
class SslTls:
    host: str
    ip_address: str
    port: int
    result: '_SslTlsResult'
    sources: list


@dataclass
class File:
    installation: str
    performed_on: 'datetime'
    result: List[str]


@dataclass
class _SslTlsResult:
    chain: '_BitMaskValues'
    end_entity: '_BitMaskValues'
    id: int
    protocols: '_BitMaskValues'


@dataclass
class _BitMaskValues:
    bitmask: int
    values: List[str]


@dataclass
class _SANS:
    dns: str
    ip: str


@dataclass
class _X509:
    cn: str
    issuer: str
    key_algorithm: str
    key_size: str
    sans: str
    serial: str
    subject: str
    thumbprint: str
    valid_from: 'datetime'
    valid_to: 'datetime'


@dataclass
class _Compliant:
    compliant: bool


@dataclass
class _CompliantSingleValue(_Compliant):
    value: str


@dataclass
class _CompliantMultiValue(_Compliant):
    values: list


@dataclass
class _Locked:
    locked: bool


@dataclass
class _LockedSingleValue(_Locked):
    value: str


@dataclass
class _LockedMultiValue(_Locked):
    values: list


@dataclass
class _LockedKeyPair:
    key_algorithm: '_LockedSingleValue'
    key_size: '_LockedSingleValue'


@dataclass
class _LockedSubject:
    city: '_LockedSingleValue'
    country: '_LockedSingleValue'
    organization: '_LockedSingleValue'
    organizational_units: '_LockedMultiValue'
    state: '_LockedSingleValue'


@dataclass
class _CSRDetails:
    city: '_CompliantSingleValue'
    common_name: '_CompliantSingleValue'
    country: '_CompliantSingleValue'
    key_algorithm: '_CompliantSingleValue'
    key_size: '_CompliantSingleValue'
    organization: '_CompliantSingleValue'
    organizational_unit: '_CompliantMultiValue'
    private_key_reused: '_CompliantSingleValue'
    state: '_CompliantSingleValue'
    subj_alt_name_dns: '_CompliantMultiValue'
    subj_alt_name_email: '_CompliantMultiValue'
    subj_alt_name_ip: '_CompliantMultiValue'
    subj_alt_name_upn: '_CompliantMultiValue'
    subj_alt_name_uri: '_CompliantMultiValue'
