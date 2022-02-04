from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.branch_base import BranchBaseAttributes


class StatisticsRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Statistics Root"
