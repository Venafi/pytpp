from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.service_module import ServiceModuleAttributes


class CertificatePreEnrollmentAttributes(ServiceModuleAttributes, metaclass=IterableMeta):
	__config_class__ = "Certificate Pre-Enrollment"
