from pytpp.attributes._helper import IterableMeta, Attribute


class AgentCertificateBaseAttributes(metaclass=IterableMeta):
	__config_class__ = "Agent Certificate Base"
	certificate_scanner_capi = Attribute('Certificate Scanner CAPI')
	certificate_scanner_map = Attribute('Certificate Scanner Map')
	certificate_scanner_path = Attribute('Certificate Scanner Path')
	credential = Attribute('Credential')
	digest = Attribute('Digest')
	exclude_remote_mount_points = Attribute('Exclude Remote Mount Points')
	expiration = Attribute('Expiration')
	key_store_validation_disabled = Attribute('Key Store Validation Disabled')
	log_threshold = Attribute('Log Threshold')
	max_filesize = Attribute('Max Filesize')
	maximum_threads = Attribute('Maximum Threads')
