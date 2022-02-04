from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class ResultCode:
    code: int
    codesign_result: str


@dataclass
class Items:
    items: List[str]


@dataclass
class InfoValue:
    info: int
    value: 'Items'


@dataclass
class CustomFieldAttributes:
    field_name: str
    values: List[str]


@dataclass
class EnvironmentTemplateDetails(InfoValue):
    template_values: 'InfoValue'


@dataclass
class RightsKeyValue:
    key: str
    value: int


@dataclass
class AppleTemplate:
    allow_user_key_import: bool
    cn_pattern: str
    dn: str
    guid: str
    id: int
    key_storage_location: 'InfoValue'
    key_time_constraints: 'Items'
    key_use_flow_dn: str
    read_only: bool
    target_policy_dn: str
    type: str
    visible_to: 'Items'


@dataclass
class AppleEnvironment:
    allow_user_key_import: bool
    apple_template: 'AppleTemplate'
    custom_field_attributes: 'List[CustomFieldAttributes]'
    dirty: bool
    dn: str
    guid: str
    id: int
    ip_address_restriction: 'Items'
    key_time_constraints: 'Items'
    key_use_flow_dn: str
    per_user: bool
    template_dn: str


@dataclass
class CertificateTemplate:
    allow_user_key_import: bool
    certificate_authority_dn: 'InfoValue'
    certificate_subject: str
    city: 'InfoValue'
    country: 'InfoValue'
    dn: str
    guid: str
    id: int
    key_algorithm: 'InfoValue'
    key_storage_location: 'InfoValue'
    key_use_flow_dn: str
    object_naming_pattern: str
    organization: 'InfoValue'
    organization_unit: 'InfoValue'
    per_user: bool
    read_only: bool
    san_email: 'InfoValue'
    state: 'InfoValue'
    target_policy_dn: str
    type: str
    visible_to: 'Items'


@dataclass
class CertificateEnvironment:
    allow_user_key_import: bool
    ca_specific_attributes: 'Items'
    certificate_authority_dn: 'InfoValue'
    certificate_subject: str
    certificate_template: 'CertificateTemplate'
    city: 'InfoValue'
    country: 'InfoValue'
    custom_field_attributes: 'List[CustomFieldAttributes]'
    dn: str
    guid: str
    id: int
    ip_address_restriction: 'Items'
    key_algorithm: 'InfoValue'
    key_storage_location: 'InfoValue'
    key_time_constraints: 'Items'
    key_use_flow_dn: str
    organization: 'InfoValue'
    organization_unit: 'InfoValue'
    per_user: bool
    san_email: 'InfoValue'
    state: 'InfoValue'
    status: int
    target_store: str
    template_dn: str
    type: str


@dataclass
class CSPTemplate:
    allow_user_key_import: bool
    dirty: bool
    dn: str
    encryption_key_algorithm: 'InfoValue'
    expiration: 'InfoValue'
    guid: str
    id: int
    key_container_dn: str
    key_storage_location: 'InfoValue'
    max_uses: 'InfoValue'
    object_naming_pattern: str
    per_user: bool
    signing_key_algorithm: 'InfoValue'
    type: str
    visible_to: 'Items'


@dataclass
class CSPEnvironment:
    allow_user_key_import: bool
    csp_template: 'CSPTemplate'
    disabled: bool
    dn: str
    encryption_key_algorithm:'EnvironmentTemplateDetails'
    encryption_key_dn: str
    expiration: int
    guid: str
    id: int
    ip_address_restriction: 'Items'
    key_storage_location: 'EnvironmentTemplateDetails'
    key_time_constraints: 'Items'
    key_use_flow_dn: str
    max_uses: int
    per_user: bool
    signing_key_algorithm: 'EnvironmentTemplateDetails'
    signing_key_dn: str
    template_dn: str


@dataclass
class DotNetTemplate:
    allow_user_key_import: bool
    disabled: bool
    dn: str
    expiration: 'InfoValue'
    guid: str
    id: int
    key_algorithm: 'InfoValue'
    key_container_dn: 'InfoValue'
    key_storage_location: 'InfoValue'
    key_use_flow_dn: str
    max_uses: 'InfoValue'
    object_naming_pattern: str
    per_user: bool
    type: str
    visible_to: 'Items'


@dataclass
class DotNetEnvironment:
    allow_user_key_import: bool
    dot_net_template: 'DotNetTemplate'
    disabled: bool
    dn: str
    expiration: int
    guid: str
    id: int
    ip_address_restriction: 'Items'
    key_algorithm: 'EnvironmentTemplateDetails'
    key_dn: str
    key_storage_location: 'EnvironmentTemplateDetails'
    key_time_constraints: 'Items'
    key_use_flow_dn: str
    max_uses: int
    per_user: bool
    template_dn: str


@dataclass
class GPGTemplate:
    allow_user_key_import: bool
    authentication_key_algorithm: 'InfoValue'
    dn: str
    email: 'InfoValue'
    encryption_key_algorithm: 'InfoValue'
    expiration: 'InfoValue'
    guid: str
    id: int
    key_storage_location: 'InfoValue'
    key_use_flow_dn: str
    max_uses: 'InfoValue'
    object_naming_pattern: str
    per_user: bool
    read_only: bool
    real_name: 'InfoValue'
    signing_key_algorithm: 'InfoValue'
    type: str
    visible_to: 'Items'


@dataclass
class GPGEnvironment:
    allow_user_key_import: bool
    authentication_key_algorithm: 'EnvironmentTemplateDetails'
    custom_fields_attributes: 'List[CustomFieldAttributes]'
    dirty: bool
    dn: str
    email: List[str]
    encryption_key_algorithm: 'EnvironmentTemplateDetails'
    expiration: int
    guid: str
    gpg_template: 'GPGTemplate'
    id: int
    ip_address_restriction: 'Items'
    key_storage_location: 'EnvironmentTemplateDetails'
    key_time_constraints: 'Items'
    key_use_flow_dn: str
    max_uses: int
    per_user: bool
    real_name: 'EnvironmentTemplateDetails'
    read_only: bool
    signing_key_algorithm: 'EnvironmentTemplateDetails'
    status: int
    template_dn: str
    type: str


@dataclass
class KeyPairTemplate:
    allow_user_key_import: bool
    description: str
    dirty: bool
    dn: str
    expiration: 'InfoValue'
    guid: str
    id: int
    key_algorithm:'InfoValue'
    key_container_dn: str
    key_storage_location: 'InfoValue'
    max_uses: int
    type: str
    validity_period: int
    visible_to: 'Items'


@dataclass
class KeyPairEnvironment:
    allow_user_key_import: bool
    custom_fields_attributes: 'List[CustomFieldAttributes]'
    dn: str
    expiration: int
    guid: str
    id: int
    ip_address_restriction: 'Items'
    key_algorithm: 'InfoValue'
    key_dn: str
    key_pair_template: 'KeyPairTemplate'
    key_storage_location: 'EnvironmentTemplateDetails'
    key_time_constraints: 'Items'
    key_use_flow_dn: str
    status: int
    template_dn: str
    type: str


@dataclass
class KeyStorageLocations:
    items: List[str]


@dataclass
class Application:
    dn: str
    guid: str
    id: int


@dataclass
class ApplicationCollection:
    application_dns: 'Items'
    dn: str
    guid: str
    id: int


@dataclass
class GlobalConfiguration:
    approved_key_storage_locations: 'KeyStorageLocations'
    available_key_storage_locations: 'KeyStorageLocations'
    default_ca_container: str
    default_certificate_container: str
    default_credential_container: str
    key_use_timeout: int
    project_description_tooltip: str
    request_in_progress_message: str


@dataclass
class Project:
    application_dns: 'Items'
    applications: 'List[Application]'
    auditors: 'Items'
    certificate_environments: 'List[CertificateEnvironment]'
    collections: 'List[SignApplicationCollection]'
    created_on: datetime
    description: str
    dn: str
    guid: str
    id: int
    key_use_approvers: 'Items'
    key_users: 'Items'
    owners: 'Items'
    status: int


@dataclass
class Rights:
    none: int
    admin: int
    use: int
    audit: int
    owner: int
    project_approval: int
    application_admin: int
    approve_use: int


@dataclass
class SignApplicationCollection:
    description: str
    dn: str
    guid: str
    hash: str
    id: int
    location: str
    permitted_argument_pattern: str
    signatory_issuer: str
    signatory_subject: str
    size: int
    version: str
