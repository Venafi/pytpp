from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.branch_base import BranchBaseAttributes


class MetadataRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Metadata Root"
