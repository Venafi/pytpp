from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.flow_action_base import FlowActionBaseAttributes


class FlowEventActionAttributes(FlowActionBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Flow Event Action"
	condition = Attribute('Condition', min_version='19.2')
	data_content = Attribute('Data Content', min_version='19.2')
	event = Attribute('Event', min_version='19.2')
	severity = Attribute('Severity', min_version='19.2')
	text1_content = Attribute('Text1 Content', min_version='19.2')
	text2_content = Attribute('Text2 Content', min_version='19.2')
	value1_content = Attribute('Value1 Content', min_version='19.2')
	value2_content = Attribute('Value2 Content', min_version='19.2')
