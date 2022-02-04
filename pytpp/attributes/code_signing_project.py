from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class CodeSigningProjectAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Project"
	approval_submission_date = Attribute('Approval Submission Date', min_version='21.2')
	auditor = Attribute('Auditor', min_version='19.2')
	certificate_issue_flow_dn = Attribute('Certificate Issue Flow DN', min_version='19.2')
	certificate_owner = Attribute('Certificate Owner', min_version='19.2')
	code_signing_application_dn = Attribute('Code Signing Application DN', min_version='19.2')
	flow_instance_macro = Attribute('Flow Instance Macro', min_version='19.3')
	key_issue_flow_dn = Attribute('Key Issue Flow DN', min_version='19.2')
	key_owner = Attribute('Key Owner', min_version='19.2')
	key_use_approver = Attribute('Key Use Approver', min_version='19.2')
	key_user = Attribute('Key User', min_version='19.2')
	owner = Attribute('Owner', min_version='19.2')
	project_delete_flow_dn = Attribute('Project Delete Flow DN', min_version='21.1')
	purpose = Attribute('Purpose', min_version='19.2')
	risk_level = Attribute('Risk Level', min_version='19.2')
	status = Attribute('Status', min_version='19.2')
