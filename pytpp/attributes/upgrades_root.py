from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class UpgradesRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Upgrades Root"
	grouping_id = Attribute('Grouping Id', min_version='20.1')
	origin_version = Attribute('Origin Version', min_version='20.1')
	start_time = Attribute('Start Time', min_version='20.1')
	stop_time = Attribute('Stop Time', min_version='20.1')
	target_version = Attribute('Target Version', min_version='20.1')
