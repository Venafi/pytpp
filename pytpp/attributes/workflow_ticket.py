from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class WorkflowTicketAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Workflow Ticket"
	approval_explanation = Attribute('Approval Explanation')
	approval_from = Attribute('Approval From')
	approval_reason = Attribute('Approval Reason')
	approver_not_found_timestamp = Attribute('Approver Not Found Timestamp', min_version='16.2')
	creation_date = Attribute('Creation Date')
	last_notification = Attribute('Last Notification')
	last_update = Attribute('Last Update')
	owner_object = Attribute('Owner Object')
	scheduled_start = Attribute('Scheduled Start')
	scheduled_stop = Attribute('Scheduled Stop')
	status = Attribute('Status')
	suspended_attribute = Attribute('Suspended Attribute', min_version='18.2')
	updated_by = Attribute('Updated By')
	user_data = Attribute('User Data')
	workflow = Attribute('Workflow')
