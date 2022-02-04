from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes
from pytpp.attributes.proxy import ProxyAttributes


class zOSCAAttributes(HTTPCABaseAttributes, ProxyAttributes, metaclass=IterableMeta):
	__config_class__ = "zOS CA"
	client_port = Attribute('Client Port')
	client_secure = Attribute('Client Secure')
	domain = Attribute('Domain')
	secure = Attribute('Secure')
