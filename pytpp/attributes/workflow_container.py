from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class WorkflowContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Workflow Container"
