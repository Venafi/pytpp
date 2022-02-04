from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.organization import OrganizationAttributes


class LayoutDriverContainerAttributes(OrganizationAttributes, metaclass=IterableMeta):
	__config_class__ = "Layout Driver Container"
