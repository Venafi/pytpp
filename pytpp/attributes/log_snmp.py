from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.log_channel import LogChannelAttributes


class LogSNMPAttributes(LogChannelAttributes, metaclass=IterableMeta):
	__config_class__ = "Log SNMP"
	community = Attribute('Community')
	message_body = Attribute('Message Body')
	snmp_authentication_password = Attribute('SNMP Authentication Password')
	snmp_authentication_protocol = Attribute('SNMP Authentication Protocol')
	snmp_engine_id = Attribute('SNMP Engine ID')
	snmp_privacy_password = Attribute('SNMP Privacy Password')
	snmp_privacy_protocol = Attribute('SNMP Privacy Protocol')
	snmp_username = Attribute('SNMP Username')
	snmp_v3_mode = Attribute('SNMP V3 Mode')
	snmp_version = Attribute('SNMP Version')
	target = Attribute('Target')
	trap_oid = Attribute('Trap OID')
