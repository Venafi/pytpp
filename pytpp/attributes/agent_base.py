from pytpp.attributes._helper import IterableMeta, Attribute


class AgentBaseAttributes(metaclass=IterableMeta):
    __config_class__ = "{key}"
    agent_guid = Attribute('Agent GUID')
    location = Attribute('Location')
