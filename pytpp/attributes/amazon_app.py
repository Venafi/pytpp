from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class AmazonAppAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Amazon App"
	access_key_id = Attribute('Access Key ID', min_version='16.1')
	aws_credential_dn = Attribute('Aws Credential DN', min_version='18.3')
	binding_target = Attribute('Binding Target', min_version='16.1')
	certificate_arn = Attribute('Certificate ARN', min_version='16.1')
	certificate_name = Attribute('Certificate Name', min_version='16.1')
	cloudfront_distribution_id = Attribute('CloudFront Distribution ID', min_version='16.1')
	create_binding = Attribute('Create Binding', min_version='18.2')
	file_validation_disabled = Attribute('File Validation Disabled', min_version='16.1')
	iam_certificate_id = Attribute('IAM Certificate ID', min_version='16.1')
	initial_binding_attempt = Attribute('Initial Binding Attempt', min_version='16.1')
	install_path = Attribute('Install Path', min_version='16.1')
	issued_by_aws = Attribute('Issued By AWS', min_version='16.1')
	load_balancer_name = Attribute('Load Balancer Name', min_version='16.1')
	load_balancer_port = Attribute('Load Balancer Port', min_version='16.1')
	load_balancer_region_code = Attribute('Load Balancer Region Code', min_version='16.1')
	minimum_protocol_version = Attribute('Minimum Protocol Version', min_version='21.3')
	network_validation_disabled = Attribute('Network Validation Disabled', min_version='16.1')
	provisioning_to = Attribute('Provisioning To', min_version='18.2')
	region_code = Attribute('Region Code', min_version='16.1')
	replace_store = Attribute('Replace Store', min_version='18.3')
	secret_access_key = Attribute('Secret Access Key', min_version='16.1')
	target_group = Attribute('Target Group', min_version='18.2')
	timeout = Attribute('Timeout', min_version='16.1')
