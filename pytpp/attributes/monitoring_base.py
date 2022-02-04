from pytpp.attributes._helper import IterableMeta, Attribute


class MonitoringBaseAttributes(metaclass=IterableMeta):
	__config_class__ = "Monitoring Base"
	creation_date = Attribute('Creation Date')
	escalation_notice_interval = Attribute('Escalation Notice Interval')
	escalation_notice_start = Attribute('Escalation Notice Start')
	expiration_notice_interval = Attribute('Expiration Notice Interval')
	expiration_notice_start = Attribute('Expiration Notice Start')
	last_notification = Attribute('Last Notification')
	notes = Attribute('Notes')
	notification_disabled = Attribute('Notification Disabled')
	validity_period = Attribute('Validity Period')
