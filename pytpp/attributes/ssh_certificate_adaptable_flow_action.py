from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.adaptable_flow_action_base import AdaptableFlowActionBaseAttributes


class SSHCertificateAdaptableFlowActionAttributes(AdaptableFlowActionBaseAttributes, metaclass=IterableMeta):
	__config_class__ = "SSH Certificate Adaptable Flow Action"
	allow_to_modify_certificate_request = Attribute('Allow To Modify Certificate Request', min_version='21.4')
	certificate_credential = Attribute('Certificate Credential', min_version='21.4')
	ssh_certificate_adaptable_flow_action_text_field_1 = Attribute('SSH Certificate Adaptable Flow Action Text Field 1', min_version='21.4')
	ssh_certificate_adaptable_flow_action_text_field_10 = Attribute('SSH Certificate Adaptable Flow Action Text Field 10', min_version='21.4')
	ssh_certificate_adaptable_flow_action_text_field_11 = Attribute('SSH Certificate Adaptable Flow Action Text Field 11', min_version='21.4')
	ssh_certificate_adaptable_flow_action_text_field_12 = Attribute('SSH Certificate Adaptable Flow Action Text Field 12', min_version='21.4')
	ssh_certificate_adaptable_flow_action_text_field_2 = Attribute('SSH Certificate Adaptable Flow Action Text Field 2', min_version='21.4')
	ssh_certificate_adaptable_flow_action_text_field_3 = Attribute('SSH Certificate Adaptable Flow Action Text Field 3', min_version='21.4')
	ssh_certificate_adaptable_flow_action_text_field_4 = Attribute('SSH Certificate Adaptable Flow Action Text Field 4', min_version='21.4')
	ssh_certificate_adaptable_flow_action_text_field_5 = Attribute('SSH Certificate Adaptable Flow Action Text Field 5', min_version='21.4')
	ssh_certificate_adaptable_flow_action_text_field_6 = Attribute('SSH Certificate Adaptable Flow Action Text Field 6', min_version='21.4')
	ssh_certificate_adaptable_flow_action_text_field_7 = Attribute('SSH Certificate Adaptable Flow Action Text Field 7', min_version='21.4')
	ssh_certificate_adaptable_flow_action_text_field_8 = Attribute('SSH Certificate Adaptable Flow Action Text Field 8', min_version='21.4')
	ssh_certificate_adaptable_flow_action_text_field_9 = Attribute('SSH Certificate Adaptable Flow Action Text Field 9', min_version='21.4')
	secondary_credential = Attribute('Secondary Credential', min_version='21.4')
	service_address = Attribute('Service Address', min_version='21.4')
	username_credential = Attribute('Username Credential', min_version='21.4')
	validate_certificate_request_before_issuance = Attribute('Validate Certificate Request Before Issuance', min_version='21.4')
