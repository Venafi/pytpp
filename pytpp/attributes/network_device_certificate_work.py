from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.client_certificate_work import ClientCertificateWorkAttributes


class NetworkDeviceCertificateWorkAttributes(ClientCertificateWorkAttributes, metaclass=IterableMeta):
	__config_class__ = "Network Device Certificate Work"
	authentication_credentials = Attribute('Authentication Credentials', min_version='20.1')
	ca_template_trust_anchors_enabled = Attribute('CA Template Trust Anchors Enabled', min_version='20.1')
	certificates_distribution_type = Attribute('Certificates Distribution Type', min_version='20.1')
	client_certificate_eku_checks_enabled = Attribute('Client Certificate Eku Checks Enabled', min_version='20.1')
	explicit_trust_anchors = Attribute('Explicit Trust Anchors', min_version='20.1')
	fallback_to_http_auth = Attribute('Fallback To Http Auth', min_version='20.1')
	http_basic_auth_disabled = Attribute('Http Basic Auth Disabled', min_version='20.1')
	http_digest_auth_disabled = Attribute('Http Digest Auth Disabled', min_version='20.1')
	pop_mode = Attribute('PoP Mode', min_version='20.1')
	reenrollment_subset_subject_matching_disabled = Attribute('ReEnrollment Subset Subject Matching Disabled', min_version='20.1')
	require_additional_http_auth = Attribute('Require Additional Http Auth', min_version='20.1')
	retryafter_disabled = Attribute('RetryAfter Disabled', min_version='20.1')
	revocation_check_timeout = Attribute('Revocation Check Timeout', min_version='20.1')
	revocation_mode = Attribute('Revocation Mode', min_version='20.1')
	revoke_existing_certificate_on_reenrollment = Attribute('Revoke Existing Certificate On ReEnrollment', min_version='20.1')
	revoke_existing_certificate_on_reenrollment_delay = Attribute('Revoke Existing Certificate On ReEnrollment Delay', min_version='20.1')
	use_implicit_trust_anchors = Attribute('Use Implicit Trust Anchors', min_version='20.1')
