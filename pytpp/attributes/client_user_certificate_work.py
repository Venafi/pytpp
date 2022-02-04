from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.client_portal_base import ClientPortalBaseAttributes
from pytpp.attributes.client_work_base import ClientWorkBaseAttributes
from pytpp.attributes.x509_certificate_base import X509CertificateBaseAttributes


class ClientUserCertificateWorkAttributes(ClientPortalBaseAttributes, ClientWorkBaseAttributes, X509CertificateBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "Client User Certificate Work"
	certificate_bundle_capacity = Attribute('Certificate Bundle Capacity', min_version='18.3')
	certificate_bundle_capacity_mobile_config = Attribute('Certificate Bundle Capacity Mobile Config', min_version='18.3')
	certificate_container = Attribute('Certificate Container', min_version='15.2')
	certificate_icon = Attribute('Certificate Icon', min_version='18.4')
	download_instructions = Attribute('Download Instructions', min_version='15.4')
	download_limit = Attribute('Download Limit', min_version='15.4')
	include_historic_certificates = Attribute('Include Historic Certificates', min_version='15.2')
	membership_loss_disable = Attribute('Membership Loss Disable', min_version='15.2')
	membership_loss_revoke = Attribute('Membership Loss Revoke', min_version='15.2')
	naming_pattern = Attribute('Naming Pattern', min_version='15.2')
	outlook_profile_generation = Attribute('Outlook Profile Generation', min_version='15.2')
	outlook_profile_name = Attribute('Outlook Profile Name', min_version='15.2')
	outlook_profile_options = Attribute('Outlook Profile Options', min_version='15.2')
	portal_friendly_name = Attribute('Portal Friendly Name', min_version='15.4')
	publish_to_identity = Attribute('Publish To Identity', min_version='15.2')
	publish_to_identity_on_pre_enroll = Attribute('Publish To Identity on Pre-Enroll', min_version='15.2')
	required_member_identity = Attribute('Required Member Identity', min_version='15.2')
	transfer_allowed = Attribute('Transfer Allowed', min_version='18.3')
