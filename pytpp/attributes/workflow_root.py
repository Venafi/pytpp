from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class WorkflowRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Workflow Root"
	approval_reason = Attribute('Approval Reason')
	approver_not_found_expiration = Attribute('Approver Not Found Expiration', min_version='16.2')
	expiration_days = Attribute('Expiration Days')
