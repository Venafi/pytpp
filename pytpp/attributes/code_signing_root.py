from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class CodeSigningRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Root"
	default_ca_container = Attribute('Default CA Container', min_version='19.2')
	default_certificate_container = Attribute('Default Certificate Container', min_version='19.2')
	default_credential_container = Attribute('Default Credential Container', min_version='19.2')
	enforce_group_roles = Attribute('Enforce Group Roles', min_version='19.2')
	environment_template_update_flow_dn = Attribute('Environment Template Update Flow DN', min_version='21.4')
	flow_instance_macro = Attribute('Flow Instance Macro', min_version='19.3')
	key_storage_location = Attribute('Key Storage Location', min_version='19.2')
	key_use_timeout = Attribute('Key Use Timeout', min_version='19.2')
	prevent_self_dealing = Attribute('Prevent Self Dealing', min_version='19.2')
	project_delete_flow_dn = Attribute('Project Delete Flow DN', min_version='21.1')
	project_description_tooltip = Attribute('Project Description Tooltip', min_version='19.2')
	request_in_progress_message = Attribute('Request In Progress Message', min_version='19.3')
