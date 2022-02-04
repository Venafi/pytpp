from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.credential_base import CredentialBaseAttributes


class AmazonCredentialAttributes(CredentialBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Amazon Credential"
	authentication_credential = Attribute('Authentication Credential', min_version='18.3')
	authentication_source = Attribute('Authentication Source', min_version='18.3')
	ec2_assigned_role = Attribute('EC2 Assigned Role', min_version='21.2')
	region_code = Attribute('Region Code', min_version='18.3')
	role = Attribute('Role', min_version='18.3')
	web_service_url = Attribute('Web Service URL', min_version='18.3')
