from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes
from pytpp.attributes.x509_certificate_base import X509CertificateBaseAttributes


class ClientCertificateWorkAttributes(ClientWorkBaseAttributes, X509CertificateBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Client Certificate Work"
	certificate_container = Attribute('Certificate Container')
	naming_pattern = Attribute('Naming Pattern')
	transfer_allowed = Attribute('Transfer Allowed', min_version='18.3')
