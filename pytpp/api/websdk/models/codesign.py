from __future__ import annotations
from pytpp.api.websdk.models.resultcodes import ResultCodes
from pytpp.api.api_base import ObjectModel, ApiField
from datetime import datetime
from typing import List, Literal, TypeVar, Generic

T = TypeVar('T')

EnvironmentType = Literal[
    'Code Signing Apple Environment',
    'Code Signing Certificate Environment',
    'Code Signing CSP Environment',
    'Code Signing DotNet Environment',
    'Code Signing Key Pair Environment',
    'Code Signing GPG Environment'
]

TemplateType = Literal[
    'Code Signing Apple Environment Template',
    'Code Signing Certificate Environment Template',
    'Code Signing CSP Environment Template',
    'Code Signing DotNet Environment Template',
    'Code Signing Key Pair Environment Template',
    'Code Signing GPG Environment Template',
]


# region Models
class ResultCode(ObjectModel):
    code: int = ApiField()

    @property
    def codesign_result(self):
        return ResultCodes.CodeSign.get(self.code, 'Unknown')


class Items(ObjectModel, Generic[T]):
    dirty: bool = ApiField(alias='Dirty')
    items: List[T] = ApiField(alias='Items', default_factory=list)


class InfoValue(ObjectModel, Generic[T]):
    info: int = ApiField(alias='Info')
    value: Items[T] = ApiField(alias='Value')


class CustomFieldAttributes(ObjectModel):
    field_name: str = ApiField(alias='FieldName')
    values: List[str] = ApiField(alias='Values', default_factory=list)


class EnvironmentTemplateDetails(InfoValue[str]):
    template_values: InfoValue[str] = ApiField(alias='TemplateValues')


class RightsKeyValue(ObjectModel):
    key: str = ApiField(alias='Key')
    value: int = ApiField(alias='Value')


class SignApplicationCollection(ObjectModel):
    description: str = ApiField(alias='Description')
    dn: str = ApiField(alias='Dn')
    guid: str = ApiField(alias='Guid')
    hash: str = ApiField(alias='Hash')
    id: int = ApiField(alias='Id')
    location: str = ApiField(alias='Location')
    permitted_argument_pattern: str = ApiField(alias='PermittedArgumentPattern')
    signatory_issuer: str = ApiField(alias='SignatoryIssuer')
    signatory_subject: str = ApiField(alias='SignatorySubject')
    size: int = ApiField(alias='Size')
    version: str = ApiField(alias='Version')


class AppleTemplate(ObjectModel):
    allow_user_key_import: bool = ApiField(alias='AllowUserKeyImport')
    certificate_authority_dn: InfoValue[str] = ApiField(alias='CertificateAuthorityDN')
    certificate_subject: InfoValue[str] = ApiField(alias='CertificateSubject')
    city: InfoValue[str] = ApiField(alias='City')
    country: InfoValue[str] = ApiField(alias='Country')
    cn_pattern: InfoValue[str] = ApiField(alias='CNPattern')
    description: str = ApiField(alias='Description')
    dn: str = ApiField(alias='Dn')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    key_algorithm: InfoValue[str] = ApiField(alias='KeyAlgorithm')
    key_storage_location: InfoValue[str] = ApiField(alias='KeyStorageLocation')
    key_time_constraints: Items[str] = ApiField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = ApiField(alias='KeyUseFlowDN')
    object_naming_pattern: str = ApiField(alias='ObjectNamingPattern')
    organization: InfoValue[str] = ApiField(alias='Organization')
    organizational_unit: InfoValue[str] = ApiField(alias='OrganizationalUnit')
    per_user: bool = ApiField(alias='PerUser')
    read_only: bool = ApiField(alias='ReadOnly')
    state: InfoValue[str] = ApiField(alias='State')
    target_policy_dn: str = ApiField(alias='TargetPolicyDn')
    type: TemplateType = ApiField(alias='Type')
    visible_to: Items[str] = ApiField(alias='VisibleTo')


class AppleEnvironment(ObjectModel):
    allow_user_key_import: bool = ApiField(alias='AllowUserKeyImport')
    apple_template: AppleTemplate = ApiField(alias='AppleTemplate')
    custom_field_attributes: Items[CustomFieldAttributes] = ApiField(alias='CustomFieldAttributes')
    dirty: bool = ApiField(alias='Dirty')
    disabled: bool = ApiField(alias='Disabled')
    dn: str = ApiField(alias='Dn')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    ip_address_restriction: Items[str] = ApiField(alias='IpAddressRestriction')
    key_time_constraints: Items[str] = ApiField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = ApiField(alias='KeyUseFlowDn')
    per_user: bool = ApiField(alias='PerUser')
    template_dn: str = ApiField(alias='TemplateDn')
    type: EnvironmentType = ApiField(alias='Type')


class CertificateTemplate(ObjectModel):
    allow_user_key_import: bool = ApiField(alias='AllowUserKeyImport')
    certificate_authority_dn: InfoValue[str] = ApiField(alias='CertificateAuthorityDn')
    certificate_subject: str = ApiField(alias='CertificateSubject')
    certificate_stage: str = ApiField(alias='CertificateStage')
    certificate_status_text: str = ApiField(alias='CertificateStatusText')
    city: InfoValue[str] = ApiField(alias='City')
    country: InfoValue[str] = ApiField(alias='Country')
    custom_field_attributes: Items[CustomFieldAttributes] = ApiField(alias='CustomFieldAttributes')
    description: str = ApiField(alias='Description')
    dn: str = ApiField(alias='Dn')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    key_algorithm: InfoValue[str] = ApiField(alias='KeyAlgorithm')
    key_storage_location: InfoValue[str] = ApiField(alias='KeyStorageLocation')
    key_use_flow_dn: str = ApiField(alias='KeyUseFlowDn')
    object_naming_pattern: str = ApiField(alias='ObjectNamingPattern')
    organization: InfoValue[str] = ApiField(alias='Organization')
    organization_unit: InfoValue[str] = ApiField(alias='OrganizationUnit')
    per_user: bool = ApiField(alias='PerUser')
    read_only: bool = ApiField(alias='ReadOnly')
    san_email: InfoValue[str] = ApiField(alias='SanEmail')
    state: InfoValue[str] = ApiField(alias='State')
    target_policy_dn: str = ApiField(alias='TargetPolicyDn')
    type: TemplateType = ApiField(alias='Type')
    visible_to: Items[str] = ApiField(alias='VisibleTo')


class CertificateEnvironment(ObjectModel):
    allow_user_key_import: bool = ApiField(alias='AllowUserKeyImport')
    ca_specific_attributes: Items[str] = ApiField(alias='CaSpecificAttributes')
    certificate_authority_dn: InfoValue[str] = ApiField(alias='CertificateAuthorityDn')
    certificate_subject: str = ApiField(alias='CertificateSubject')
    certificate_template: CertificateTemplate = ApiField(alias='CertificateTemplate')
    city: InfoValue[str] = ApiField(alias='City')
    country: InfoValue[str] = ApiField(alias='Country')
    custom_field_attributes: CustomFieldAttributes = ApiField(alias='CustomFieldAttributes')
    dn: str = ApiField(alias='Dn')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    ip_address_restriction: Items[str] = ApiField(alias='IpAddressRestriction')
    key_algorithm: InfoValue[str] = ApiField(alias='KeyAlgorithm')
    key_storage_location: InfoValue[str] = ApiField(alias='KeyStorageLocation')
    key_time_constraints: Items[str] = ApiField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = ApiField(alias='KeyUseFlowDn')
    organization: InfoValue[str] = ApiField(alias='Organization')
    organization_unit: InfoValue[str] = ApiField(alias='OrganizationUnit')
    per_user: bool = ApiField(alias='PerUser')
    san_email: InfoValue[str] = ApiField(alias='SanEmail')
    state: InfoValue[str] = ApiField(alias='State')
    status: int = ApiField(alias='Status')
    target_store: str = ApiField(alias='TargetStore')
    template_dn: str = ApiField(alias='TemplateDn')
    type: EnvironmentType = ApiField(alias='Type')


class CSPTemplate(ObjectModel):
    allow_user_key_import: bool = ApiField(alias='AllowUserKeyImport')
    description: str = ApiField(alias='Description')
    dirty: bool = ApiField(alias='Dirty')
    dn: str = ApiField(alias='Dn')
    encryption_key_algorithm: InfoValue[str] = ApiField(alias='EncryptionKeyAlgorithm')
    expiration: InfoValue[str] = ApiField(alias='Expiration')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    key_container_dn: str = ApiField(alias='KeyContainerDn')
    key_storage_location: InfoValue[str] = ApiField(alias='KeyStorageLocation')
    max_uses: InfoValue[str] = ApiField(alias='MaxUses')
    object_naming_pattern: str = ApiField(alias='ObjectNamingPattern')
    per_user: bool = ApiField(alias='PerUser')
    signing_key_algorithm: InfoValue[str] = ApiField(alias='SigningKeyAlgorithm')
    type: TemplateType = ApiField(alias='Type')
    visible_to: Items[str] = ApiField(alias='VisibleTo')


class CSPEnvironment(ObjectModel):
    allow_user_key_import: bool = ApiField(alias='AllowUserKeyImport')
    csp_template: CSPTemplate = ApiField(alias='CspTemplate')
    disabled: bool = ApiField(alias='Disabled')
    dn: str = ApiField(alias='Dn')
    encryption_key_algorithm: EnvironmentTemplateDetails = ApiField(alias='EncryptionKeyAlgorithm')
    encryption_key_dn: str = ApiField(alias='EncryptionKeyDn')
    expiration: int = ApiField(alias='Expiration')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    ip_address_restriction: Items[str] = ApiField(alias='IpAddressRestriction')
    key_storage_location: EnvironmentTemplateDetails = ApiField(alias='KeyStorageLocation')
    key_time_constraints: Items[str] = ApiField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = ApiField(alias='KeyUseFlowDn')
    max_uses: int = ApiField(alias='MaxUses')
    per_user: bool = ApiField(alias='PerUser')
    signing_key_algorithm: EnvironmentTemplateDetails = ApiField(alias='SigningKeyAlgorithm')
    signing_key_dn: str = ApiField(alias='SigningKeyDn')
    template_dn: str = ApiField(alias='TemplateDn')


class DotNetTemplate(ObjectModel):
    allow_user_key_import: bool = ApiField(alias='AllowUserKeyImport')
    description: str = ApiField(alias='Description')
    disabled: bool = ApiField(alias='Disabled')
    dn: str = ApiField(alias='Dn')
    expiration: InfoValue[str] = ApiField(alias='Expiration')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    key_algorithm: InfoValue[str] = ApiField(alias='KeyAlgorithm')
    key_container_dn: InfoValue[str] = ApiField(alias='KeyContainerDn')
    key_storage_location: InfoValue[str] = ApiField(alias='KeyStorageLocation')
    key_use_flow_dn: str = ApiField(alias='KeyUseFlowDn')
    max_uses: InfoValue[str] = ApiField(alias='MaxUses')
    object_naming_pattern: str = ApiField(alias='ObjectNamingPattern')
    per_user: bool = ApiField(alias='PerUser')
    type: TemplateType = ApiField(alias='Type')
    visible_to: Items[str] = ApiField(alias='VisibleTo')


class DotNetEnvironment(ObjectModel):
    allow_user_key_import: bool = ApiField(alias='AllowUserKeyImport')
    dot_net_template: DotNetTemplate = ApiField(alias='DotNetTemplate')
    disabled: bool = ApiField(alias='Disabled')
    dn: str = ApiField(alias='Dn')
    expiration: int = ApiField(alias='Expiration')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    ip_address_restriction: Items[str] = ApiField(alias='IpAddressRestriction')
    key_algorithm: EnvironmentTemplateDetails = ApiField(alias='KeyAlgorithm')
    key_dn: str = ApiField(alias='KeyDn')
    key_storage_location: EnvironmentTemplateDetails = ApiField(alias='KeyStorageLocation')
    key_time_constraints: Items[str] = ApiField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = ApiField(alias='KeyUseFlowDn')
    max_uses: int = ApiField(alias='MaxUses')
    per_user: bool = ApiField(alias='PerUser')
    template_dn: str = ApiField(alias='TemplateDn')
    type: TemplateType = ApiField(alias='Type')


class GPGTemplate(ObjectModel):
    allow_user_key_import: bool = ApiField(alias='AllowUserKeyImport')
    authentication_key_algorithm: InfoValue[str] = ApiField(alias='AuthenticationKeyAlgorithm')
    description: str = ApiField(alias='Description')
    dn: str = ApiField(alias='Dn')
    email: InfoValue[str] = ApiField(alias='Email')
    encryption_key_algorithm: InfoValue[str] = ApiField(alias='EncryptionKeyAlgorithm')
    expiration: InfoValue[str] = ApiField(alias='Expiration')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    key_container_dn: str = ApiField(alias='KeyContainerDN')
    key_storage_location: InfoValue[str] = ApiField(alias='KeyStorageLocation')
    key_use_flow_dn: str = ApiField(alias='KeyUseFlowDn')
    max_uses: InfoValue[str] = ApiField(alias='MaxUses')
    object_naming_pattern: str = ApiField(alias='ObjectNamingPattern')
    per_user: bool = ApiField(alias='PerUser')
    read_only: bool = ApiField(alias='ReadOnly')
    real_name: InfoValue[str] = ApiField(alias='RealName')
    signing_key_algorithm: InfoValue[str] = ApiField(alias='SigningKeyAlgorithm')
    type: TemplateType = ApiField(alias='Type')
    visible_to: Items[str] = ApiField(alias='VisibleTo')


class GPGEnvironment(ObjectModel):
    allow_user_key_import: bool = ApiField(alias='AllowUserKeyImport')
    authentication_key_algorithm: EnvironmentTemplateDetails = ApiField(alias='AuthenticationKeyAlgorithm')
    custom_field_attributes: Items[CustomFieldAttributes] = ApiField(alias='CustomFieldsAttributes')
    dirty: bool = ApiField(alias='Dirty')
    dn: str = ApiField(alias='Dn')
    email: List[str] = ApiField(alias='Email', default_factory=list)
    encryption_key_algorithm: EnvironmentTemplateDetails = ApiField(alias='EncryptionKeyAlgorithm')
    expiration: int = ApiField(alias='Expiration')
    guid: str = ApiField(alias='Guid')
    gpg_template: GPGTemplate = ApiField(alias='GpgTemplate')
    id: int = ApiField(alias='Id')
    ip_address_restriction: Items[str] = ApiField(alias='IpAddressRestriction')
    key_storage_location: EnvironmentTemplateDetails = ApiField(alias='KeyStorageLocation')
    key_time_constraints: Items[str] = ApiField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = ApiField(alias='KeyUseFlowDn')
    max_uses: int = ApiField(alias='MaxUses')
    per_user: bool = ApiField(alias='PerUser')
    real_name: EnvironmentTemplateDetails = ApiField(alias='RealName')
    read_only: bool = ApiField(alias='ReadOnly')
    signing_key_algorithm: EnvironmentTemplateDetails = ApiField(alias='SigningKeyAlgorithm')
    status: int = ApiField(alias='Status')
    template_dn: str = ApiField(alias='TemplateDn')
    type: EnvironmentType = ApiField(alias='Type')


class KeyPairTemplate(ObjectModel):
    allow_user_key_import: bool = ApiField(alias='AllowUserKeyImport')
    description: str = ApiField(alias='Description')
    dirty: bool = ApiField(alias='Dirty')
    dn: str = ApiField(alias='Dn')
    expiration: InfoValue[str] = ApiField(alias='Expiration')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    key_algorithm: InfoValue[str] = ApiField(alias='KeyAlgorithm')
    key_container_dn: str = ApiField(alias='KeyContainerDn')
    key_storage_location: InfoValue[str] = ApiField(alias='KeyStorageLocation')
    max_uses: int = ApiField(alias='MaxUses')
    object_naming_pattern: str = ApiField(alias='ObjectNamingPattern')
    per_user: bool = ApiField(alias='PerUser')
    type: TemplateType = ApiField(alias='Type')
    validity_period: int = ApiField(alias='ValidityPeriod')
    visible_to: Items[str] = ApiField(alias='VisibleTo')


class KeyPairEnvironment(ObjectModel):
    allow_user_key_import: bool = ApiField(alias='AllowUserKeyImport')
    custom_field_attributes: Items[CustomFieldAttributes] = ApiField(alias='CustomFieldsAttributes')
    dn: str = ApiField(alias='Dn')
    expiration: int = ApiField(alias='Expiration')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    ip_address_restriction: Items[str] = ApiField(alias='IpAddressRestriction')
    key_algorithm: InfoValue[str] = ApiField(alias='KeyAlgorithm')
    key_dn: str = ApiField(alias='KeyDn')
    key_pair_template: KeyPairTemplate = ApiField(alias='KeyPairTemplate')
    key_storage_location: EnvironmentTemplateDetails = ApiField(alias='KeyStorageLocation')
    key_time_constraints: Items[str] = ApiField(alias='KeyTimeConstraints')
    key_use_flow_dn: str = ApiField(alias='KeyUseFlowDn')
    status: int = ApiField(alias='Status')
    template_dn: str = ApiField(alias='TemplateDn')
    type: EnvironmentType = ApiField(alias='Type')


class Application(ObjectModel):
    description: str = ApiField(alias='Description')
    dn: str = ApiField(alias='Dn')
    guid: str = ApiField(alias='Guid')
    hash: str = ApiField(alias='Hash')
    id: int = ApiField(alias='Id')
    location: str = ApiField(alias='Location')
    permitted_argument_pattern: str = ApiField(alias='PermittedArgumentPattern')
    signatory_issuer: str = ApiField(alias='SignatoryIssuer')
    signatory_subject: str = ApiField(alias='SignatorySubject')
    size: int = ApiField(alias='Size')
    version: str = ApiField(alias='Version')


class ApplicationCollection(ObjectModel):
    application_dns: Items[str] = ApiField(alias='ApplicationDns')
    dn: str = ApiField(alias='Dn')
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')


class GlobalConfiguration(ObjectModel):
    approved_key_storage_locations: Items[str] = ApiField(alias='ApprovedKeyStorageLocations')
    available_key_storage_locations: Items[str] = ApiField(alias='AvailableKeyStorageLocations')
    default_ca_container: str = ApiField(alias='DefaultCaContainer')
    default_certificate_container: str = ApiField(alias='DefaultCertificateContainer')
    default_credential_container: str = ApiField(alias='DefaultCredentialContainer')
    key_use_timeout: int = ApiField(alias='KeyUseTimeout')
    project_description_tooltip: str = ApiField(alias='ProjectDescriptionTooltip')
    request_in_progress_message: str = ApiField(alias='RequestInProgressMessage')


class Project(ObjectModel):
    application_dns: Items[str] = ApiField(alias='ApplicationDns')
    applications: List[Application] = ApiField(alias='Applications', default_factory=list)
    auditors: Items[str] = ApiField(alias='Auditors')
    certificate_environments: List[CertificateEnvironment] = ApiField(alias='CertificateEnvironments', default_factory=list)
    collections: List[SignApplicationCollection] = ApiField(alias='Collections', default_factory=list)
    created_on: datetime = ApiField(alias='CreatedOn')
    csp_environments: List[CSPEnvironment] = ApiField(alias='CSPEnvironments', default_factory=list)
    custom_field_attributes: Items[CustomFieldAttributes] = ApiField(alias='CustomFieldAttributes', default_factory=list)
    description: str = ApiField(alias='Description')
    dn: str = ApiField(alias='Dn')
    dot_net_environments: List[DotNetEnvironment] = ApiField(alias='DotNetEnvironments', default_factory=list)
    gpg_environments: List[GPGEnvironment] = ApiField(alias='GPGEnvironments', default_factory=list)
    guid: str = ApiField(alias='Guid')
    id: int = ApiField(alias='Id')
    key_use_approvers: Items[str] = ApiField(alias='KeyUseApprovers')
    key_users: Items[str] = ApiField(alias='KeyUsers')
    owners: Items[str] = ApiField(alias='Owners')
    status: int = ApiField(alias='Status')


class Rights(ObjectModel):
    value: int = ApiField()

    @property
    def none(self) -> int:
        return self.value == 0

    @property
    def admin(self) -> int:
        return self.value & 1 == 1

    @property
    def use(self) -> int:
        return self.value & 2 == 2

    @property
    def audit(self) -> int:
        return self.value & 4 == 4

    @property
    def owner(self) -> int:
        return self.value & 8 == 8

    @property
    def project_approval(self) -> int:
        return self.value & 16 == 16

    @property
    def application_admin(self) -> int:
        return self.value & 32 == 32

    @property
    def approve_use(self) -> int:
        return self.value & 64 == 64
