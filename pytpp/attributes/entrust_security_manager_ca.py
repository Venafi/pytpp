from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.certificate_authority_base import CertificateAuthorityBaseAttributes


class EntrustSecurityManagerCAAttributes(CertificateAuthorityBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Entrust Security Manager CA"
	certificate_type = Attribute('Certificate Type', min_version='15.3')
	create_entrust_user = Attribute('Create Entrust User')
	epf_credential = Attribute('EPF Credential')
	epf_credential_dn = Attribute('EPF Credential DN')
	enrollment_server_for_web_folder = Attribute('Enrollment Server for Web Folder')
	ini_file = Attribute('INI File')
	role = Attribute('Role', min_version='15.3')
	searchbase = Attribute('Searchbase')
	user_class_name = Attribute('User Class Name', min_version='15.3')
