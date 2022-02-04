from pytpp.attributes._helper import IterableMeta, Attribute


class TopAttributes(metaclass=IterableMeta):
	__config_class__ = "Top"
	contact = Attribute('Contact')
	created_by = Attribute('Created By', min_version='15.1')
	description = Attribute('Description')
	disabled = Attribute('Disabled')
	escalation_contact = Attribute('Escalation Contact')
	guid = Attribute('GUID')
	managed_by = Attribute('Managed By')
	metadata = Attribute('Metadata')
	reference = Attribute('Reference')
	workflow = Attribute('Workflow')
	workflow_block = Attribute('Workflow Block')
