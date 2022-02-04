from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.schedule_base import ScheduleBaseAttributes
from pytpp.attributes.top import TopAttributes


class CodeSigningKeyTimeConstraintAttributes(ScheduleBaseAttributes, TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Code Signing Key Time Constraint"
