from pytpp.tools.deprecation import DeprecationMeta
from pytpp.properties.config import (
    ApplicationGroupClassNames, ApplicationClassNames, CertificateClassNames, DevicesClassNames, DiscoveryClassNames,
    IdentityClassNames, PlacementRulesClassNames, PlatformsClassNames, WorkflowClassNames, ClientWorkClassNames,
    ClientGroupsClassNames, FolderClassNames, CertificateAuthorityClassNames
)

class Classes(metaclass=DeprecationMeta):
    __deprecation_reason__ = 'Using Classes will be deprecated soon. Get the TPP class names from the attributes using ' \
                             'pytpp.Attributes (from pytpp import Attributes) instead. Alternatively you can import ' \
                             'pytpp.ClassNames, which provides all class names in TPP whereas the Attributes only ' \
                             'provide the commonly used TPP class names.'
    Application = ApplicationClassNames
    ApplicationGroup = ApplicationGroupClassNames
    Certificate = CertificateClassNames
    CertificateAuthority = CertificateAuthorityClassNames
    ClientGroups = ClientGroupsClassNames
    ClientWork = ClientWorkClassNames
    Device = DevicesClassNames
    Discovery = DiscoveryClassNames
    Folder = FolderClassNames
    Identity = IdentityClassNames
    PlacementRules = PlacementRulesClassNames
    Platforms = PlatformsClassNames
    Workflow = WorkflowClassNames
