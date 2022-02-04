from pytpp.features.objects import Objects
from pytpp.features.folder import Folder
from pytpp.features.client_groups import (
    Agentless, EstCertificateEnrollment, VenafiAgent
)
from pytpp.features.client_work import (
    AgentConnectivity, AgentUpgrade, CertificateDevicePlacement, CertificateDiscovery,
    CertificateEnrollmentViaESTProtocol, CertificateInstallation, DynamicProvisioning,
    SSHDevicePlacement, SSHDiscovery, SSHKeyUsage, SSHRemediation, UserCertificateCreation
)
from pytpp.features.certificate import Certificate
from pytpp.features.device import Device, JumpServer
from pytpp.features.application import (
    Adaptable as AdapatbleApplication, AmazonAWS, Apache, AzureKeyVault, Basic, BlueCoatSSLVA, CAPI, CitrixNetScaler,
    ConnectDirect, F5AuthenticationBundle, F5LTMAdvanced, GoogleCloudLoadBalancer, IBMDataPower, IBMGSK, ImpervaMX, JKS,
    OracleIPlanet, PaloAltoNetworkFW, PEM, PKCS11, PKCS12, RiverbedSteelHead, TealeafPCA, VAMnShield,
    PKCS11ApplicationGroup, ApacheApplicationGroup
)
from pytpp.features.discovery import NetworkDiscovery
from pytpp.features.credentials import (
    AmazonCredential, CertificateCredential, GenericCredential, PasswordCredential, PrivateKeyCredential,
    UsernamePasswordCredential, GoogleCredential
)
from pytpp.features.certificate_authorities import (MSCA, SelfSignedCA)
from pytpp.features.identity import User, Group
from pytpp.features.permissions import Permissions
from pytpp.features.platforms import Platforms
from pytpp.features.placement_rules import PlacementRules, PlacementRuleCondition
from pytpp.features.workflow import ReasonCode, AdaptableWorkflow, StandardWorkflow, Ticket
from pytpp.features.custom_fields import CustomField


# region Features
class _Application:
    def __init__(self, api):
        self._api = api

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
        self._oracle_iplanet = None
        self._palo_alto_network_fw = None
        self._pem = None
        self._pkcs11 = None
        self._pkcs12 = None
        self._riverbed_steel_head = None
        self._tealeaf_pca = None
        self._vamnshield = None

    @property
    def adaptable(self) -> AdapatbleApplication:
        self._adaptable = self._adaptable or AdapatbleApplication(self._api)
        return self._adaptable

    @property
    def amazon_aws(self) -> AmazonAWS:
        self._amazon_aws = self._amazon_aws or AmazonAWS(self._api)
        return self._amazon_aws

    @property
    def apache(self) -> Apache:
        self._apache = self._apache or Apache(self._api)
        return self._apache

    @property
    def azure_key_vault(self) -> AzureKeyVault:
        self._azure_key_vault = self._azure_key_vault or AzureKeyVault(self._api)
        return self._azure_key_vault

    @property
    def basic(self) -> Basic:
        self._basic = self._basic or Basic(self._api)
        return self._basic

    @property
    def blue_coat_sslva(self) -> BlueCoatSSLVA:
        self._blue_coat_sslva = self._blue_coat_sslva or BlueCoatSSLVA(self._api)
        return self._blue_coat_sslva

    @property
    def capi(self) -> CAPI:
        self._capi = self._capi or CAPI(self._api)
        return self._capi

    @property
    def citrix_net_scaler(self) -> CitrixNetScaler:
        self._citrix_net_scaler = self._citrix_net_scaler or CitrixNetScaler(self._api)
        return self._citrix_net_scaler

    @property
    def connect_direct(self) -> ConnectDirect:
        self._connect_direct = self._connect_direct or ConnectDirect(self._api)
        return self._connect_direct

    @property
    def f5_authentication_bundle(self) -> F5AuthenticationBundle:
        self._f5_authentication_bundle = self._f5_authentication_bundle or F5AuthenticationBundle(self._api)
        return self._f5_authentication_bundle

    @property
    def f5_ltm_advanced(self) -> F5LTMAdvanced:
        self._f5_ltm_advanced = self._f5_ltm_advanced or F5LTMAdvanced(self._api)
        return self._f5_ltm_advanced

    @property
    def google_cloud_load_balancer(self) -> GoogleCloudLoadBalancer:
        self._google_cloud_load_balancer = self._google_cloud_load_balancer or GoogleCloudLoadBalancer(self._api)
        return self._google_cloud_load_balancer

    @property
    def ibm_datapower(self) -> IBMDataPower:
        self._ibm_datapower = self._ibm_datapower or IBMDataPower(self._api)
        return self._ibm_datapower

    @property
    def ibm_gsk(self) -> IBMGSK:
        self._ibm_gsk = self._ibm_gsk or IBMGSK(self._api)
        return self._ibm_gsk

    @property
    def imperva_mx(self) -> ImpervaMX:
        self._imperva_mx = self._imperva_mx or ImpervaMX(self._api)
        return self._imperva_mx

    @property
    def jks(self) -> JKS:
        self._jks = self._jks or JKS(self._api)
        return self._jks

    @property
    def oracle_iplanet(self) -> OracleIPlanet:
        self._oracle_iplanet = self._oracle_iplanet or OracleIPlanet(self._api)
        return self._oracle_iplanet

    @property
    def palo_alto_network_fw(self) -> PaloAltoNetworkFW:
        self._palo_alto_network_fw = self._palo_alto_network_fw or PaloAltoNetworkFW(self._api)
        return self._palo_alto_network_fw

    @property
    def pem(self) -> PEM:
        self._pem = self._pem or PEM(self._api)
        return self._pem

    @property
    def pkcs11(self) -> PKCS11:
        self._pkcs11 = self._pkcs11 or PKCS11(self._api)
        return self._pkcs11

    @property
    def pkcs12(self) -> PKCS12:
        self._pkcs12 = self._pkcs12 or PKCS12(self._api)
        return self._pkcs12

    @property
    def riverbed_steel_head(self) -> RiverbedSteelHead:
        self._riverbed_steel_head = self._riverbed_steel_head or RiverbedSteelHead(self._api)
        return self._riverbed_steel_head

    @property
    def tealeaf_pca(self) -> TealeafPCA:
        self._tealeaf_pca = self._tealeaf_pca or TealeafPCA(self._api)
        return self._tealeaf_pca

    @property
    def vamnshield(self) -> VAMnShield:
        self._vamnshield = self._vamnshield or VAMnShield(self._api)
        return self._vamnshield


class _ApplicationGroup:
    def __init__(self, api):
        self._api = api

        self._apache = None
        self._pkcs11 = None

    @property
    def apache(self) -> ApacheApplicationGroup:
        self._apache = self._apache or ApacheApplicationGroup(self._api)
        return self._apache

    @property
    def pkcs11(self) -> PKCS11ApplicationGroup:
        self._pkcs11 = self._pkcs11 or PKCS11ApplicationGroup(self._api)
        return self._pkcs11


class _CertificateAuthority:
    def __init__(self, api):
        self._api = api

        self._msca = None
        self._self_signed = None

    @property
    def msca(self) -> MSCA:
        self._msca = self._msca or MSCA(self._api)
        return self._msca

    @property
    def self_signed(self) -> SelfSignedCA:
        self._self_signed = self._self_signed or SelfSignedCA(self._api)
        return self._self_signed


class _ClientGroup:
    def __init__(self, api):
        self._api = api

        self._agentless = None
        self._est_certificate_enrollment = None
        self._venafi_agent = None

    @property
    def agentless(self) -> Agentless:
        self._agentless = self._agentless or Agentless(self._api)
        return self._agentless

    @property
    def est_certificate_enrollment(self) -> EstCertificateEnrollment:
        self._est_certificate_enrollment = self._est_certificate_enrollment or PKCS11ApplicationGroup(self._api)
        return self._est_certificate_enrollment

    @property
    def venafi_agent(self) -> VenafiAgent:
        self._venafi_agent = self._venafi_agent or VenafiAgent(self._api)
        return self._venafi_agent


class _ClientWork:
    def __init__(self, api):
        self._api = api
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
    def agent_connectivity(self) -> AgentConnectivity:
        self._agent_connectivity = self._agent_connectivity or AgentConnectivity(self._api)
        return self._agent_connectivity

    @property
    def agent_upgrade(self) -> AgentUpgrade:
        self._agent_upgrade = self._agent_upgrade or AgentUpgrade(self._api)
        return self._agent_upgrade

    @property
    def certificate_device_placement(self) -> CertificateDevicePlacement:
        self._certificate_device_placement = self._certificate_device_placement or CertificateDevicePlacement(self._api)
        return self._certificate_device_placement

    @property
    def certificate_discovery(self) -> CertificateDiscovery:
        self._certificate_discovery = self._certificate_discovery or CertificateDiscovery(self._api)
        return self._certificate_discovery

    @property
    def certificate_enrollment_via_est_protocol(self) -> CertificateEnrollmentViaESTProtocol:
        self._certificate_enrollment_via_est_protocol = self._certificate_enrollment_via_est_protocol or CertificateEnrollmentViaESTProtocol(
            self._api)
        return self._certificate_enrollment_via_est_protocol

    @property
    def certificate_installation(self) -> CertificateInstallation:
        self._certificate_installation = self._certificate_installation or CertificateInstallation(
            self._api)
        return self._certificate_installation

    @property
    def dynamic_provisioning(self) -> DynamicProvisioning:
        self._dynamic_provisioning = self._dynamic_provisioning or DynamicProvisioning(
            self._api)
        return self._dynamic_provisioning

    @property
    def ssh_device_placement(self) -> SSHDevicePlacement:
        self._ssh_device_placement = self._ssh_device_placement or SSHDevicePlacement(
            self._api)
        return self._ssh_device_placement

    @property
    def ssh_discovery(self) -> SSHDiscovery:
        self._ssh_discovery = self._ssh_discovery or SSHDiscovery(
            self._api)
        return self._ssh_discovery

    @property
    def ssh_key_usage(self) -> SSHKeyUsage:
        self._ssh_key_usage = self._ssh_key_usage or SSHKeyUsage(
            self._api)
        return self._ssh_key_usage

    @property
    def ssh_remediation(self) -> SSHRemediation:
        self._ssh_remediation = self._ssh_remediation or SSHRemediation(
            self._api)
        return self._ssh_remediation

    @property
    def user_certificate_creation(self) -> UserCertificateCreation:
        self._user_certificate_creation = self._user_certificate_creation or UserCertificateCreation(
            self._api)
        return self._user_certificate_creation


class _Credential:
    def __init__(self, api):
        self._api = api

        self._amazon = None
        self._certificate = None
        self._generic = None
        self._google = None
        self._password = None
        self._private_key = None
        self._upcred = None

    @property
    def amazon(self) -> AmazonCredential:
        self._amazon = self._amazon or AmazonCredential(self._api)
        return self._amazon

    @property
    def certificate(self) -> CertificateCredential:
        self._certificate = self._certificate or CertificateCredential(self._api)
        return self._certificate

    @property
    def generic(self) -> GenericCredential:
        self._generic = self._generic or GenericCredential(self._api)
        return self._generic

    @property
    def google(self) -> GoogleCredential:
        self._google = self._google or GoogleCredential(self._api)
        return self._google

    @property
    def password(self) -> PasswordCredential:
        self._password = self._password or PasswordCredential(self._api)
        return self._password

    @property
    def private_key(self) -> PrivateKeyCredential:
        self._private_key = self._private_key or PrivateKeyCredential(self._api)
        return self._private_key

    @property
    def username_password(self) -> UsernamePasswordCredential:
        self._upcred = self._upcred or UsernamePasswordCredential(self._api)
        return self._upcred


class _Discovery:
    def __init__(self, api):
        self._api = api

        self._network = None

    @property
    def network(self) -> NetworkDiscovery:
        self._network = self._network or NetworkDiscovery(api=self._api)
        return self._network


class _Identity:
    def __init__(self, api):
        self._api = api

        self._group = None
        self._user = None

    @property
    def group(self) -> Group:
        self._group = self._group or Group(self._api)
        return self._group

    @property
    def user(self) -> User:
        self._user = self._user or User(self._api)
        return self._user


class _Workflow:
    def __init__(self, api):
        self._api = api

        self._adaptable = None
        self._reason_code = None
        self._standard = None
        self._ticket = None

    @property
    def adaptable(self) -> AdaptableWorkflow:
        self._adaptable = self._adaptable or AdaptableWorkflow(self._api)
        return self._adaptable

    @property
    def reason_code(self) -> ReasonCode:
        self._reason_code = self._reason_code or ReasonCode(self._api)
        return self._reason_code

    @property
    def standard(self) -> StandardWorkflow:
        self._standard = self._standard or StandardWorkflow(self._api)
        return self._standard

    @property
    def ticket(self) -> Ticket:
        self._ticket = self._ticket or Ticket(self._api)
        return self._ticket


class Features:
    def __init__(self, api):
        self._api = api

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
        self._jump_server = None
        self._objects = None
        self._permissions = None
        self._placement_rule_condition = None
        self._placement_rules = None
        self._platforms = None
        self._workflow = None

    @property
    def application(self) -> _Application:
        self._applications = self._applications or _Application(self._api)
        return self._applications

    @property
    def application_group(self) -> _ApplicationGroup:
        self._application_group = self._application_group or _ApplicationGroup(self._api)
        return self._application_group

    @property
    def certificate(self) -> Certificate:
        self._certificate = self._certificate or Certificate(self._api)
        return self._certificate

    @property
    def certificate_authority(self) -> _CertificateAuthority:
        self._ca = self._ca or _CertificateAuthority(self._api)
        return self._ca

    @property
    def client_groups(self) -> _ClientGroup:
        self._client_groups = self._client_groups or _ClientGroup(self._api)
        return self._client_groups

    @property
    def client_work(self) -> _ClientWork:
        self._client_work = self._client_work or _ClientWork(self._api)
        return self._client_work

    @property
    def credential(self) -> _Credential:
        self._credentials = self._credentials or _Credential(self._api)
        return self._credentials

    @property
    def custom_fields(self) -> CustomField:
        self._custom_fields = self._custom_fields or CustomField(self._api)
        return self._custom_fields

    @property
    def device(self) -> Device:
        self._device = self._device or Device(self._api)
        return self._device

    @property
    def discovery(self) -> _Discovery:
        self._discovery = self._discovery or _Discovery(self._api)
        return self._discovery

    @property
    def folder(self) -> Folder:
        self._folder = self._folder or Folder(self._api)
        return self._folder

    @property
    def identity(self) -> _Identity:
        self._identity = self._identity or _Identity(self._api)
        return self._identity

    @property
    def jump_server(self) -> JumpServer:
        self._jump_server = self._jump_server or JumpServer(self._api)
        return self._jump_server

    @property
    def objects(self) -> Objects:
        self._objects = self._objects or Objects(self._api)
        return self._objects

    @property
    def permissions(self) -> Permissions:
        self._permissions = self._permissions or Permissions(self._api)
        return self._permissions

    @property
    def placement_rule_condition(self) -> PlacementRuleCondition:
        self._placement_rule_condition = self._placement_rule_condition or PlacementRuleCondition()
        return self._placement_rule_condition

    @property
    def placement_rules(self) -> PlacementRules:
        self._placement_rules = self._placement_rules or PlacementRules(self._api)
        return self._placement_rules

    @property
    def platforms(self) -> Platforms:
        self._platforms = self._platforms or Platforms(self._api)
        return self._platforms

    @property
    def workflow(self) -> _Workflow:
        self._workflow = self._workflow or _Workflow(self._api)
        return self._workflow

# endregion
