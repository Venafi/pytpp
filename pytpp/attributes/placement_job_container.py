from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.organization import OrganizationAttributes


class PlacementJobContainerAttributes(OrganizationAttributes, metaclass=IterableMeta):
	__config_class__ = "Placement Job Container"
