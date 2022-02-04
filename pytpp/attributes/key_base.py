from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.monitoring_base import MonitoringBaseAttributes
from pytpp.attributes.top import TopAttributes


class KeyBaseAttributes(MonitoringBaseAttributes, TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Key Base"
	algorithm = Attribute('Algorithm', min_version='20.2')
	approver = Attribute('Approver', min_version='20.2')
	consumers = Attribute('Consumers', min_version='20.2')
	disable_automatic_renewal = Attribute('Disable Automatic Renewal', min_version='20.2')
	in_error = Attribute('In Error', min_version='20.2')
	internet_email_address = Attribute('Internet EMail Address', min_version='20.2')
	key_storage_location = Attribute('Key Storage Location', min_version='20.2')
	label = Attribute('Label', min_version='20.2')
	last_evaluated_on = Attribute('Last Evaluated On', min_version='20.2')
	last_notification = Attribute('Last Notification', min_version='20.2')
	last_renewed_by = Attribute('Last Renewed By', min_version='20.2')
	last_renewed_on = Attribute('Last Renewed On', min_version='20.2')
	management_type = Attribute('Management Type', min_version='20.2')
	max_uses = Attribute('Max Uses', min_version='20.2')
	origin = Attribute('Origin', min_version='20.2')
	private_key_vault_id = Attribute('Private Key Vault Id', min_version='20.2')
	real_name = Attribute('Real Name', min_version='20.2')
	status = Attribute('Status', min_version='20.2')
	use_count = Attribute('Use Count', min_version='20.2')
	validity_period = Attribute('Validity Period', min_version='20.2')
