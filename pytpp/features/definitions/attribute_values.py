from pytpp.properties.config import (
    ApplicationAttributeValues, ClientGroupsAttributeValues, CertificateAttributeValues, CertificateAuthorityAttributeValues,
    DeviceAttributeValues, DiscoveryAttributeValues, CustomFieldAttributeValues, IdentityAttributeValues, WorkflowAttributeValues,
    PlacementRulesAttributeValues, ClientWorkAttributeValues, JumpServerAttributeValues
)

class AttributeValues:
    Application = ApplicationAttributeValues
    Certificate = CertificateAttributeValues
    CertificateAuthority = CertificateAuthorityAttributeValues
    ClientGroups = ClientGroupsAttributeValues
    ClientWork = ClientWorkAttributeValues
    CustomField = CustomFieldAttributeValues
    Device = DeviceAttributeValues
    Discovery = DiscoveryAttributeValues
    Identity = IdentityAttributeValues
    JumpServer = JumpServerAttributeValues
    PlacementRules = PlacementRulesAttributeValues
    Workflow = WorkflowAttributeValues
