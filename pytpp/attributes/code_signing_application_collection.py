from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class CodeSigningApplicationCollectionAttributes(TopAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    code_signing_application_dn = Attribute('Code Signing Application DN', min_version='19.2')
