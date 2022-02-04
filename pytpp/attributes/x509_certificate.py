from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.x509_certificate_base import X509CertificateBaseAttributes
from pytpp.attributes.x509_certificate_validation import X509CertificateValidationAttributes


class X509CertificateAttributes(X509CertificateBaseAttributes, X509CertificateValidationAttributes, metaclass=IterableMeta):
	__config_class__ = "X509 Certificate"
	acme_account_dn = Attribute('ACME Account DN', min_version='17.2')
	application_group_dn = Attribute('Application Group DN', min_version='19.4')
	geotrusttrueflex_ca_emails = Attribute('GeotrustTrueFlex CA:Emails', min_version='15.3')
	geotrusttrueflex_ca_enrollment_mode = Attribute('GeotrustTrueFlex CA:Enrollment Mode', min_version='15.3')
	geotrusttrueflex_ca_first_pickup_request = Attribute('GeotrustTrueFlex CA:First Pickup Request', min_version='15.3')
	geotrusttrueflex_ca_timestamp = Attribute('GeotrustTrueFlex CA:Timestamp', min_version='15.3')
	microsoft_ca_pool_certificate_authority = Attribute('Microsoft CA Pool:Certificate Authority', min_version='19.1')
	portal_download_count = Attribute('Portal Download Count')
	prohibited_san_types = Attribute('Prohibited SAN Types', min_version='18.3')
	ticket_dn = Attribute('Ticket DN')
	work_dn = Attribute('Work DN')
