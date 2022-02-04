from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.top import TopAttributes


class RemoteAccessScopeContainerAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Remote Access Scope Container"
