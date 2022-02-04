from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.driver_base import DriverBaseAttributes


class CloudInstanceMonitorDriverBaseAttributes(DriverBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Cloud Instance Monitor Driver Base"
	certificate_cleanup_options = Attribute('Certificate Cleanup Options', min_version='17.1')
	certificate_relocation_policy_dn = Attribute('Certificate Relocation Policy DN', min_version='17.1')
	cleanup_after = Attribute('Cleanup After', min_version='17.1')
	cloud_region = Attribute('Cloud Region', min_version='17.1')
	last_run = Attribute('Last Run', min_version='17.1')
	policydn = Attribute('PolicyDN', min_version='17.1')
