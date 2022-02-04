from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.http_ca_base import HTTPCABaseAttributes
from pytpp.attributes.proxy import ProxyAttributes


class VeriSignCAAttributes(HTTPCABaseAttributes, ProxyAttributes, metaclass=IterableMeta):
	__config_class__ = "VeriSign CA"
	additional_field = Attribute('Additional Field')
	admin_isd = Attribute('Admin Isd')
	allow_reissue = Attribute('Allow Reissue', min_version='17.2')
	attempt_renewal = Attribute('Attempt Renewal', min_version='17.2')
	certificate_block = Attribute('Certificate Block')
	certificate_transparency = Attribute('Certificate Transparency', min_version='16.3')
	domain = Attribute('Domain')
	interval = Attribute('Interval')
	jurisdiction_hash = Attribute('Jurisdiction Hash')
	mpki_url = Attribute('Mpki Url')
	organization = Attribute('Organization')
	organizational_unit = Attribute('Organizational Unit')
	renewal_window = Attribute('Renewal Window', min_version='17.2')
	retrieval_period = Attribute('Retrieval Period')
	vice_url = Attribute('Vice Url')
