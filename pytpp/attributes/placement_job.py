from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.schedule_base import ScheduleBaseAttributes
from pytpp.attributes.top import TopAttributes


class PlacementJobAttributes(ScheduleBaseAttributes, TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Placement Job"
	archive_old_certificates = Attribute('Archive Old Certificates', min_version='19.1')
	default_container = Attribute('Default Container', min_version='19.1')
	include_subfolders = Attribute('Include Subfolders', min_version='19.1')
	last_run = Attribute('Last Run', min_version='19.1')
	layout_rules = Attribute('Layout Rules', min_version='19.1')
	objects_combined = Attribute('Objects Combined', min_version='19.1')
	objects_evaluated = Attribute('Objects Evaluated', min_version='19.1')
	objects_moved = Attribute('Objects Moved', min_version='19.1')
	progress = Attribute('Progress', min_version='19.1')
	rules_order = Attribute('Rules Order', min_version='19.1')
	scan_folders = Attribute('Scan Folders', min_version='19.1')
	status = Attribute('Status', min_version='19.1')
