from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.tree_root import TreeRootAttributes


class BranchBaseAttributes(TreeRootAttributes, metaclass=IterableMeta):
	__config_class__ = "Branch Base"
