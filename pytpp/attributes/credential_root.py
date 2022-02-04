from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class CredentialRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Credential Root"
	escalation_notice_interval = Attribute('Escalation Notice Interval')
	escalation_notice_start = Attribute('Escalation Notice Start')
	expiration_notice_interval = Attribute('Expiration Notice Interval')
	expiration_notice_start = Attribute('Expiration Notice Start')
	protection_key = Attribute('Protection Key')
	start_time = Attribute('Start Time')
