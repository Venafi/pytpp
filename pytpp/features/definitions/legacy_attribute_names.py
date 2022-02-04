from pytpp.tools.deprecation import DeprecationMeta
from pytpp.properties.config import (
    FolderAttributes, ClientGroupsAttributes, ClientWorkAttributes, WorkflowAttributes, CustomFieldAttributes,
    CertificateAttributes, DeviceAttributes, ApplicationAttributes, CredentialAttributes, DiscoveryAttributes,
    CertificateAuthorityAttributes, PlatformsAttributes, PlacementRulesAttributeNames, ApplicationGroupAttributes
)

class AttributeNames(metaclass=DeprecationMeta):
    __deprecation_reason__ = 'Using AttributeNames will be deprecated soon. Please use ' \
                             'pytpp.Attributes (from pytpp import Attributes) instead.'
    Application = ApplicationAttributes
    ApplicationGroup = ApplicationGroupAttributes
    Certificate = CertificateAttributes
    CertificateAuthority = CertificateAuthorityAttributes
    ClientGroups = ClientGroupsAttributes
    ClientWork = ClientWorkAttributes
    Credentials = CredentialAttributes
    CustomField = CustomFieldAttributes
    Device = DeviceAttributes
    Discovery = DiscoveryAttributes
    Folder = FolderAttributes
    PlacementRules = PlacementRulesAttributeNames
    Platforms = PlatformsAttributes
    Workflow = WorkflowAttributes
