from pytpp.attributes._helper import IterableMeta, Attribute


class ProxyAttributes(metaclass=IterableMeta):
	__config_class__ = "Proxy"
	bypass_proxy_on_local = Attribute('Bypass Proxy on Local')
	credential = Attribute('Credential')
	proxy_credential = Attribute('Proxy Credential')
	proxy_host = Attribute('Proxy Host')
	proxy_port = Attribute('Proxy Port')
	proxy_use_host_configuration = Attribute('Proxy Use Host Configuration')
