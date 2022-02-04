from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class ApplicationGroupAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Application Group"
	certificate = Attribute('Certificate', min_version='19.4')
	common_data_location = Attribute('Common Data Location', min_version='19.4')
	common_data_vault_id = Attribute('Common Data Vault Id', min_version='19.4')
	enrollment_application_dn = Attribute('Enrollment Application DN', min_version='19.4')
	primary_application_dn = Attribute('Primary Application DN', min_version='19.4')
	private_key_stub_vault_id = Attribute('Private Key Stub Vault Id', min_version='19.4')
