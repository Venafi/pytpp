from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.organization import OrganizationAttributes


class CredentialContainerAttributes(OrganizationAttributes, metaclass=IterableMeta):
	__config_class__ = "Credential Container"
