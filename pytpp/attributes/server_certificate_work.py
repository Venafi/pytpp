from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes
from pytpp.attributes.x509_certificate_base import X509CertificateBaseAttributes


class ServerCertificateWorkAttributes(ApplicationBaseAttributes, ClientWorkBaseAttributes, X509CertificateBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Server Certificate Work"
	application_attribute = Attribute('Application Attribute', min_version='18.3')
	application_type = Attribute('Application Type', min_version='18.3')
	certificate_container = Attribute('Certificate Container', min_version='18.3')
	friendly_name = Attribute('Friendly Name', min_version='18.3')
	interval = Attribute('Interval', min_version='18.3')
	log_threshold = Attribute('Log Threshold', min_version='18.3')
	naming_pattern = Attribute('Naming Pattern', min_version='18.3')
	nix_key_store = Attribute('Nix Key Store', min_version='18.3')
	nix_private_key = Attribute('Nix Private Key', min_version='18.3')
	path_type = Attribute('Path Type')
	private_key_trustee = Attribute('Private Key Trustee', min_version='20.2')
	win_key_store = Attribute('Win Key Store', min_version='18.3')
	win_private_key = Attribute('Win Private Key', min_version='18.3')
