from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.organization import OrganizationAttributes


class LayoutRuleContainerAttributes(OrganizationAttributes, metaclass=IterableMeta):
	__config_class__ = "Layout Rule Container"
