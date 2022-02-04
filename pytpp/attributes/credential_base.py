from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class CredentialBaseAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Credential Base"
	escalation_notice_interval = Attribute('Escalation Notice Interval')
	escalation_notice_start = Attribute('Escalation Notice Start')
	expiration = Attribute('Expiration')
	expiration_notice_interval = Attribute('Expiration Notice Interval')
	expiration_notice_start = Attribute('Expiration Notice Start')
	last_notification = Attribute('Last Notification')
	protection_key = Attribute('Protection Key')
	shared = Attribute('Shared')
	vault_id = Attribute('Vault Id')
