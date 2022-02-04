from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class TreeRootAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Tree Root"
	company_name = Attribute('Company Name', min_version='17.3')
	migration_task = Attribute('Migration Task')
	pendo_eula_version = Attribute('Pendo EULA Version', min_version='19.2')
	pendo_optional_data_collection = Attribute('Pendo Optional Data Collection', min_version='19.2')
	schema_version = Attribute('Schema Version')
	usage_tracking = Attribute('Usage Tracking', min_version='19.2')
	use_company_name_for_analytics = Attribute('Use Company Name for Analytics', min_version='17.3')
	version = Attribute('Version')
