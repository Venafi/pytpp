from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.branch_base import BranchBaseAttributes


class SSOAttributes(BranchBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "SSO"
