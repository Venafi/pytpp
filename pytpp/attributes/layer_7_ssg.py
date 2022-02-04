from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_base import ApplicationBaseAttributes


class Layer7SSGAttributes(ApplicationBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Layer 7 SSG"
	certificate_oid = Attribute('Certificate OID')
	certificate_only = Attribute('Certificate Only')
	chain_cert = Attribute('Chain Cert')
	database_validation_disabled = Attribute('Database Validation Disabled')
	file_validation_disabled = Attribute('File Validation Disabled', min_version='15.3')
	first_backup_certificate_oid = Attribute('First Backup Certificate OID')
	first_backup_private_key_oid = Attribute('First Backup Private Key OID')
	https_port = Attribute('HTTPS Port')
	network_validation_disabled = Attribute('Network Validation Disabled')
	outbound_ssl = Attribute('Outbound SSL')
	private_key_oid = Attribute('Private Key OID')
	provision_manner = Attribute('Provision Manner')
	revocation_checking_enabled = Attribute('Revocation Checking Enabled')
	saml_attesting = Attribute('SAML Attesting')
	second_backup_certificate_oid = Attribute('Second Backup Certificate OID')
	second_backup_private_key_oid = Attribute('Second Backup Private Key OID')
	service = Attribute('Service')
	signing_client = Attribute('Signing Client')
	signing_outbound_ssl = Attribute('Signing Outbound SSL')
	signing_saml = Attribute('Signing SAML')
	trust_anchor = Attribute('Trust Anchor')
	verify_hostname = Attribute('Verify Hostname')
	web_credential = Attribute('Web Credential')
	web_service_url = Attribute('Web Service URL')
