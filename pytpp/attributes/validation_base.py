from pytpp.attributes._helper import IterableMeta, Attribute


class ValidationBaseAttributes(metaclass=IterableMeta):
	__config_class__ = "Validation Base"
	file_validation_error = Attribute('File Validation Error', min_version='15.3')
	file_validation_result = Attribute('File Validation Result', min_version='15.3')
	last_validation = Attribute('Last Validation')
	last_validation_result = Attribute('Last Validation Result')
	ssl_listen_host = Attribute('SSL Listen Host')
	ssl_listen_port = Attribute('SSL Listen Port')
	use_specified_host = Attribute('Use Specified Host')
	validation_disabled = Attribute('Validation Disabled')
	validation_errors = Attribute('Validation Errors', min_version='15.3')
	validation_results = Attribute('Validation Results', min_version='15.3')
