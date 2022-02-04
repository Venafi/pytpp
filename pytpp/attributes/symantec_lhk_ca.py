from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes
from pytpp.attributes.proxy import ProxyAttributes


class SymantecLHKCAAttributes(HTTPCABaseAttributes, ProxyAttributes, metaclass=IterableMeta):
	__config_class__ = "Symantec LHK CA"
	fields = Attribute('Fields')
	uri = Attribute('URI')
