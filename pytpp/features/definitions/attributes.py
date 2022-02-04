class _Application:
    def __init__(self):
        self._adaptable = None
        self._amazon_aws = None
        self._apache = None
        self._azure_key_vault = None
        self._basic = None
        self._blue_coat_sslva = None
        self._capi = None
        self._citrix_net_scaler = None
        self._connect_direct = None
        self._f5_authentication_bundle = None
        self._f5_ltm_advanced = None
        self._google_cloud_load_balancer = None
        self._ibm_datapower = None
        self._ibm_gsk = None
        self._imperva_mx = None
        self._jks = None
        self._juniper_sas = None
        self._oracle_iplanet = None
        self._palo_alto_network_fw = None
        self._pem = None
        self._pkcs11 = None
        self._pkcs12 = None
        self._riverbed_steel_head = None
        self._tealeaf_pca = None
        self._vamnshield = None

    @property
    def adaptable(self):
        if not self._adaptable:
            from pytpp.attributes.adaptable_app import AdaptableAppAttributes
            self._adaptable = AdaptableAppAttributes
        return self._adaptable

    @property
    def amazon_aws(self):
        if not self._amazon_aws:
            from pytpp.attributes.amazon_app import AmazonAppAttributes
            self._amazon_aws = AmazonAppAttributes
        return self._amazon_aws

    @property
    def apache(self):
        if not self._apache:
            from pytpp.attributes.apache import ApacheAttributes
            self._apache = ApacheAttributes
        return self._apache

    @property
    def azure_key_vault(self):
        if not self._azure_key_vault:
            from pytpp.attributes.azure_key_vault import AzureKeyVaultAttributes
            self._azure_key_vault = AzureKeyVaultAttributes
        return self._azure_key_vault

    @property
    def basic(self):
        if not self._basic:
            from pytpp.attributes.basic import BasicAttributes
            self._basic = BasicAttributes
        return self._basic

    @property
    def blue_coat_sslva(self):
        if not self._blue_coat_sslva:
            from pytpp.attributes.bluecoat_sslva import BlueCoatSSLVAAttributes
            self._blue_coat_sslva = BlueCoatSSLVAAttributes
        return self._blue_coat_sslva

    @property
    def capi(self):
        if not self._capi:
            from pytpp.attributes.capi import CAPIAttributes
            self._capi = CAPIAttributes
        return self._capi

    @property
    def citrix_net_scaler(self):
        if not self._citrix_net_scaler:
            from pytpp.attributes.netscaler import NetScalerAttributes
            self._citrix_net_scaler = NetScalerAttributes
        return self._citrix_net_scaler

    @property
    def connect_direct(self):
        if not self._connect_direct:
            from pytpp.attributes.connectdirect import ConnectDirectAttributes
            self._connect_direct = ConnectDirectAttributes
        return self._connect_direct

    @property
    def f5_authentication_bundle(self):
        if not self._f5_authentication_bundle:
            from pytpp.attributes.f5_authentication_bundle import F5AuthenticationBundleAttributes
            self._f5_authentication_bundle = F5AuthenticationBundleAttributes
        return self._f5_authentication_bundle

    @property
    def f5_ltm_advanced(self):
        if not self._f5_ltm_advanced:
            from pytpp.attributes.f5_ltm_advanced import F5LTMAdvancedAttributes
            self._f5_ltm_advanced = F5LTMAdvancedAttributes
        return self._f5_ltm_advanced

    @property
    def google_cloud_load_balancer(self):
        if not self._google_cloud_load_balancer:
            from pytpp.attributes.google_cloud_app import GoogleCloudAppAttributes
            self._google_cloud_load_balancer = GoogleCloudAppAttributes
        return self._google_cloud_load_balancer

    @property
    def ibm_datapower(self):
        if not self._ibm_datapower:
            from pytpp.attributes.datapower import DataPowerAttributes
            self._ibm_datapower = DataPowerAttributes
        return self._ibm_datapower

    @property
    def ibm_gsk(self) :
        if not self._ibm_gsk:
            from pytpp.attributes.gsk import GSKAttributes
            self._ibm_gsk = GSKAttributes
        return self._ibm_gsk

    @property
    def imperva_mx(self) :
        if not self._imperva_mx:
            from pytpp.attributes.imperva_mx import ImpervaMXAttributes
            self._imperva_mx = ImpervaMXAttributes
        return self._imperva_mx

    @property
    def jks(self) :
        if not self._jks:
            from pytpp.attributes.jks import JKSAttributes
            self._jks = JKSAttributes
        return self._jks

    @property
    def juniper_sas(self) :
        if not self._juniper_sas:
            from pytpp.attributes.juniper_sas import JuniperSASAttributes
            self._juniper_sas = JuniperSASAttributes
        return self._juniper_sas

    @property
    def oracle_iplanet(self) :
        if not self._oracle_iplanet:
            from pytpp.attributes.iplanet import iPlanetAttributes
            self._oracle_iplanet = iPlanetAttributes
        return self._oracle_iplanet

    @property
    def palo_alto_network_fw(self) :
        if not self._palo_alto_network_fw:
            from pytpp.attributes.palo_alto_network_fw import PaloAltoNetworkFWAttributes
            self._palo_alto_network_fw = PaloAltoNetworkFWAttributes
        return self._palo_alto_network_fw

    @property
    def pem(self) :
        if not self._pem:
            from pytpp.attributes.pem import PEMAttributes
            self._pem = PEMAttributes
        return self._pem

    @property
    def pkcs11(self) :
        if not self._pkcs11:
            from pytpp.attributes.pkcs11 import PKCS11Attributes
            self._pkcs11 = PKCS11Attributes
        return self._pkcs11

    @property
    def pkcs12(self) :
        if not self._pkcs12:
            from pytpp.attributes.pkcs_12 import PKCS12Attributes
            self._pkcs12 = PKCS12Attributes
        return self._pkcs12

    @property
    def riverbed_steel_head(self) :
        if not self._riverbed_steel_head:
            from pytpp.attributes.riverbed_steelhead import RiverbedSteelHeadAttributes
            self._riverbed_steel_head = RiverbedSteelHeadAttributes
        return self._riverbed_steel_head

    @property
    def tealeaf_pca(self) :
        if not self._tealeaf_pca:
            from pytpp.attributes.tealeaf_pca import TealeafPCAAttributes
            self._tealeaf_pca = TealeafPCAAttributes
        return self._tealeaf_pca

    @property
    def vamnshield(self) :
        if not self._vamnshield:
            from pytpp.attributes.vam_nshield import VAMnShieldAttributes
            self._vamnshield = VAMnShieldAttributes
        return self._vamnshield


class _ApplicationGroup:
    def __init__(self):
        self._apache = None
        self._pkcs11 = None

    @property
    def apache(self) :
        if not self._apache:
            from pytpp.attributes.apache_application_group import ApacheApplicationGroupAttributes
            self._apache = ApacheApplicationGroupAttributes
        return self._apache

    @property
    def pkcs11(self) :
        if not self._pkcs11:
            from pytpp.attributes.pkcs11_application_group import PKCS11ApplicationGroupAttributes
            self._pkcs11 = PKCS11ApplicationGroupAttributes
        return self._pkcs11


class _CertificateAuthority:
    def __init__(self):
        self._adaptable = None
        self._msca = None
        self._self_signed = None

    @property
    def adaptable(self) :
        if not self._adaptable:
            from pytpp.attributes.adaptable_ca import AdaptableCAAttributes
            self._adaptable = AdaptableCAAttributes
        return self._adaptable

    @property
    def msca(self) :
        if not self._msca:
            from pytpp.attributes.microsoft_ca import MicrosoftCAAttributes
            self._msca = MicrosoftCAAttributes
        return self._msca

    @property
    def self_signed(self) :
        if not self._self_signed:
            from pytpp.attributes.self_signed_ca import SelfSignedCAAttributes
            self._self_signed = SelfSignedCAAttributes
        return self._self_signed


class _ClientWork:
    def __init__(self):
        self._agent_connectivity = None
        self._agent_upgrade = None
        self._certificate_device_placement = None
        self._certificate_discovery = None
        self._certificate_enrollment_via_est_protocol = None
        self._certificate_installation = None
        self._device_certificate_creation = None
        self._dynamic_provisioning = None
        self._ssh_device_placement = None
        self._ssh_discovery = None
        self._ssh_key_usage = None
        self._ssh_remediation = None
        self._user_certificate_creation = None

    @property
    def agent_connectivity(self) :
        if not self._agent_connectivity:
            from pytpp.attributes.client_agent_configuration_work import ClientAgentConfigurationWorkAttributes
            self._agent_connectivity = ClientAgentConfigurationWorkAttributes
        return self._agent_connectivity

    @property
    def agent_upgrade(self):
        if not self._agent_upgrade:
            from pytpp.attributes.client_agent_automatic_upgrade_work import ClientAgentAutomaticUpgradeWorkAttributes
            self._agent_upgrade = ClientAgentAutomaticUpgradeWorkAttributes
        return self._agent_upgrade

    @property
    def certificate_device_placement(self) :
        if not self._certificate_device_placement:
            from pytpp.attributes.server_agent_cert_device_placement_work import ServerAgentCertDevicePlacementWorkAttributes
            self._certificate_device_placement = ServerAgentCertDevicePlacementWorkAttributes
        return self._certificate_device_placement

    @property
    def certificate_discovery(self) :
        if not self._certificate_discovery:
            from pytpp.attributes.client_certificate_discovery_work import ClientCertificateDiscoveryWorkAttributes
            self._certificate_discovery = ClientCertificateDiscoveryWorkAttributes
        return self._certificate_discovery

    @property
    def certificate_enrollment_via_est_protocol(self) :
        if not self._certificate_enrollment_via_est_protocol:
            from pytpp.attributes.network_device_certificate_work import NetworkDeviceCertificateWorkAttributes
            self._certificate_enrollment_via_est_protocol = NetworkDeviceCertificateWorkAttributes
        return self._certificate_enrollment_via_est_protocol

    @property
    def certificate_installation(self) :
        if not self._certificate_installation:
            from pytpp.attributes.certificate_provisioning_work import CertificateProvisioningWorkAttributes
            self._certificate_installation = CertificateProvisioningWorkAttributes
        return self._certificate_installation

    @property
    def dynamic_provisioning(self) :
        if not self._dynamic_provisioning:
            from pytpp.attributes.server_certificate_work import ServerCertificateWorkAttributes
            self._dynamic_provisioning = ServerCertificateWorkAttributes
        return self._dynamic_provisioning

    @property
    def ssh_device_placement(self) :
        if not self._ssh_device_placement:
            from pytpp.attributes.server_agent_ssh_device_placement_work import ServerAgentSSHDevicePlacementWorkAttributes
            self._ssh_device_placement = ServerAgentSSHDevicePlacementWorkAttributes
        return self._ssh_device_placement

    @property
    def ssh_discovery(self) :
        if not self._ssh_discovery:
            from pytpp.attributes.client_agent_ssh_discovery_work import ClientAgentSSHDiscoveryWorkAttributes
            self._ssh_discovery = ClientAgentSSHDiscoveryWorkAttributes
        return self._ssh_discovery

    @property
    def ssh_key_usage(self) :
        if not self._ssh_key_usage:
            from pytpp.attributes.client_agent_ssh_key_usage_work import ClientAgentSSHKeyUsageWorkAttributes
            self._ssh_key_usage = ClientAgentSSHKeyUsageWorkAttributes
        return self._ssh_key_usage

    @property
    def ssh_remediation(self) :
        if not self._ssh_remediation:
            from pytpp.attributes.client_agent_ssh_provisioning_work import ClientAgentSSHProvisioningWorkAttributes
            self._ssh_remediation = ClientAgentSSHProvisioningWorkAttributes
        return self._ssh_remediation

    @property
    def user_certificate_creation(self) :
        if not self._user_certificate_creation:
            from pytpp.attributes.client_user_certificate_work import ClientUserCertificateWorkAttributes
            self._user_certificate_creation = ClientUserCertificateWorkAttributes
        return self._user_certificate_creation


class _Credential:
    def __init__(self):
        self._amazon = None
        self._certificate = None
        self._generic = None
        self._password = None
        self._private_key = None
        self._upcred = None

    @property
    def amazon(self) :
        if not self._amazon:
            from pytpp.attributes.amazon_credential import AmazonCredentialAttributes
            self._amazon = AmazonCredentialAttributes
        return self._amazon

    @property
    def certificate(self) :
        if not self._certificate:
            from pytpp.attributes.certificate_credential import CertificateCredentialAttributes
            self._certificate = CertificateCredentialAttributes
        return self._certificate

    @property
    def generic(self) :
        if not self._generic:
            from pytpp.attributes.generic_credential import GenericCredentialAttributes
            self._generic = GenericCredentialAttributes
        return self._generic

    @property
    def password(self) :
        if not self._password:
            from pytpp.attributes.password_credential import PasswordCredentialAttributes
            self._password = PasswordCredentialAttributes
        return self._password

    @property
    def private_key(self) :
        if not self._private_key:
            from pytpp.attributes.private_key_credential import PrivateKeyCredentialAttributes
            self._private_key = PrivateKeyCredentialAttributes
        return self._private_key

    @property
    def username_password(self) :
        if not self._upcred:
            from pytpp.attributes.username_password_credential import UsernamePasswordCredentialAttributes
            self._upcred = UsernamePasswordCredentialAttributes
        return self._upcred


class _Discovery:
    def __init__(self):
        self._network = None

    @property
    def network(self) :
        if not self._network:
            from pytpp.attributes.discovery import DiscoveryAttributes
            self._network = DiscoveryAttributes
        return self._network


class _Identity:
    def __init__(self):
        self._group = None
        self._user = None

    @property
    def group(self) :
        if not self._group:
            from pytpp.attributes.group import GroupAttributes
            self._group = GroupAttributes
        return self._group

    @property
    def user(self) :
        if not self._user:
            from pytpp.attributes.user import UserAttributes
            self._user = UserAttributes
        return self._user


class _Platforms:
    def __init__(self):
        self._auto_layout_manager = None
        self._bulk_provisioning_manager = None
        self._ca_import_manager = None
        self._certificate_manager = None
        self._certificate_pre_enrollment = None
        self._certificate_revocation = None
        self._cloud_instance_monitor = None
        self._discovery_manager = None
        self._engines = None
        self._monitor = None
        self._onboard_discovery_manager = None
        self._reporting = None
        self._ssh_manager = None
        self._trustnet_manager = None
        self._validation_manager = None

    @property
    def auto_layout_manager(self) :
        if not self._auto_layout_manager:
            from pytpp.attributes.auto_layout_manager import AutoLayoutManagerAttributes
            self._auto_layout_manager = AutoLayoutManagerAttributes
        return self._auto_layout_manager

    @property
    def bulk_provisioning_manager(self) :
        if not self._bulk_provisioning_manager:
            from pytpp.attributes.bulk_provisioning_manager import BulkProvisioningManagerAttributes
            self._bulk_provisioning_manager = BulkProvisioningManagerAttributes
        return self._bulk_provisioning_manager

    @property
    def ca_import_manager(self) :
        if not self._ca_import_manager:
            from pytpp.attributes.ca_import_manager import CAImportManagerAttributes
            self._ca_import_manager = CAImportManagerAttributes
        return self._ca_import_manager

    @property
    def certificate_manager(self) :
        if not self._certificate_manager:
            from pytpp.attributes.certificate_manager import CertificateManagerAttributes
            self._certificate_manager = CertificateManagerAttributes
        return self._certificate_manager

    @property
    def certificate_pre_enrollment(self) :
        if not self._certificate_pre_enrollment:
            from pytpp.attributes.certificate_pre_enrollment import CertificatePreEnrollmentAttributes
            self._certificate_pre_enrollment = CertificatePreEnrollmentAttributes
        return self._certificate_pre_enrollment

    @property
    def certificate_revocation(self) :
        if not self._certificate_revocation:
            from pytpp.attributes.certificate_revocation import CertificateRevocationAttributes
            self._certificate_revocation = CertificateRevocationAttributes
        return self._certificate_revocation

    @property
    def cloud_instance_monitor(self) :
        if not self._cloud_instance_monitor:
            from pytpp.attributes.cloud_instance_monitor import CloudInstanceMonitorAttributes
            self._cloud_instance_monitor = CloudInstanceMonitorAttributes
        return self._cloud_instance_monitor

    @property
    def discovery_manager(self) :
        if not self._discovery_manager:
            from pytpp.attributes.discovery_manager import DiscoveryManagerAttributes
            self._discovery_manager = DiscoveryManagerAttributes
        return self._discovery_manager

    @property
    def engines(self):
        if not self._engines:
            from pytpp.attributes.venafi_platform import VenafiPlatformAttributes
            self._engines = VenafiPlatformAttributes
        return self._engines

    @property
    def monitor(self) :
        if not self._monitor:
            from pytpp.attributes.monitoring_module import MonitoringModuleAttributes
            self._monitor = MonitoringModuleAttributes
        return self._monitor

    @property
    def onboard_discovery_manager(self) :
        if not self._onboard_discovery_manager:
            from pytpp.attributes.onboard_discovery_manager import OnboardDiscoveryManagerAttributes
            self._onboard_discovery_manager = OnboardDiscoveryManagerAttributes
        return self._onboard_discovery_manager

    @property
    def reporting(self) :
        if not self._reporting:
            from pytpp.attributes.reporter_service_module import ReporterServiceModuleAttributes
            self._reporting = ReporterServiceModuleAttributes
        return self._reporting

    @property
    def ssh_manager(self) :
        if not self._ssh_manager:
            from pytpp.attributes.ssh_manager import SSHManagerAttributes
            self._ssh_manager = SSHManagerAttributes
        return self._ssh_manager

    @property
    def validation_manager(self) :
        if not self._validation_manager:
            from pytpp.attributes.validation_manager import ValidationManagerAttributes
            self._validation_manager = ValidationManagerAttributes
        return self._validation_manager


class _Workflow:
    def __init__(self):
        self._adaptable = None
        self._standard = None
        self._ticket = None

    @property
    def adaptable(self) :
        if not self._adaptable:
            from pytpp.attributes.adaptable_workflow import AdaptableWorkflowAttributes
            self._adaptable = AdaptableWorkflowAttributes
        return self._adaptable

    @property
    def standard(self) :
        if not self._standard:
            from pytpp.attributes.workflow import WorkflowAttributes
            self._standard = WorkflowAttributes
        return self._standard

    @property
    def ticket(self) :
        if not self._ticket:
            from pytpp.attributes.workflow_ticket import WorkflowTicketAttributes
            self._ticket = WorkflowTicketAttributes
        return self._ticket


class _Attributes:
    def __init__(self):
        self._applications = None
        self._application_group = None
        self._ca = None
        self._certificate = None
        self._client_groups = None
        self._client_work = None
        self._credentials = None
        self._custom_fields = None
        self._device = None
        self._discovery = None
        self._folder = None
        self._identity = None
        self._permissions = None
        self._placement_rules = None
        self._platforms = None
        self._workflow = None

    @property
    def application(self) -> _Application:
        self._applications = self._applications or _Application()
        return self._applications

    @property
    def application_group(self) -> _ApplicationGroup:
        self._application_group = self._application_group or _ApplicationGroup()
        return self._application_group

    @property
    def certificate(self):
        if not self._certificate:
            from pytpp.attributes.x509_certificate import X509CertificateAttributes
            self._certificate = X509CertificateAttributes
        return self._certificate

    @property
    def certificate_authority(self) -> _CertificateAuthority:
        self._ca = self._ca or _CertificateAuthority()
        return self._ca

    @property
    def client_groups(self):
        if not self._client_groups:
            from pytpp.attributes.client_group import ClientGroupAttributes
            self._client_groups = ClientGroupAttributes
        return self._client_groups

    @property
    def client_work(self) -> _ClientWork:
        self._client_work = self._client_work or _ClientWork()
        return self._client_work

    @property
    def credential(self) -> _Credential:
        self._credentials = self._credentials or _Credential()
        return self._credentials

    @property
    def custom_fields(self):
        if not self._custom_fields:
            from pytpp.attributes.metadata_list import MetadataListAttributes
            from pytpp.attributes.metadata_text import MetadataTextAttributes
            from pytpp.attributes.metadata_category import MetadataCategoryAttributes
            from pytpp.attributes.metadata_choice import MetadataChoiceAttributes
            from pytpp.attributes.metadata_datetime import MetadataDateTimeAttributes
            from pytpp.attributes.metadata_identity import MetadataIdentityAttributes
            from pytpp.attributes.metadata_base import IterableMeta

            class CustomFieldAttributes(metaclass=IterableMeta):
                list_type = MetadataListAttributes
                text_type = MetadataTextAttributes
                category_type = MetadataCategoryAttributes
                choice_type = MetadataChoiceAttributes
                datetime_type = MetadataDateTimeAttributes
                identity_type = MetadataIdentityAttributes

            self._custom_fields = CustomFieldAttributes
        return self._custom_fields

    @property
    def device(self):
        if not self._device:
            from pytpp.attributes.device import DeviceAttributes
            self._device = DeviceAttributes
        return self._device

    @property
    def discovery(self) -> _Discovery:
        self._discovery = self._discovery or _Discovery()
        return self._discovery

    @property
    def folder(self):
        if not self._folder:
            from pytpp.attributes.policy import PolicyAttributes
            self._folder = PolicyAttributes
        return self._folder

    @property
    def identity(self) -> _Identity:
        self._identity = self._identity or _Identity()
        return self._identity

    @property
    def placement_rules(self):
        if not self._placement_rules:
            from pytpp.attributes.layout_rule_base import LayoutRuleBaseAttributes
            self._placement_rules = LayoutRuleBaseAttributes
        return self._placement_rules

    @property
    def platforms(self) -> _Platforms:
        self._platforms = self._platforms or _Platforms()
        return self._platforms

    @property
    def workflow(self) -> _Workflow:
        self._workflow = self._workflow or _Workflow()
        return self._workflow


Attributes = _Attributes()
