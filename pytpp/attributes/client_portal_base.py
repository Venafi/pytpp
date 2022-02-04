from pytpp.attributes._helper import IterableMeta, Attribute


class ClientPortalBaseAttributes(metaclass=IterableMeta):
	__config_class__ = "Client Portal Base"
	client_field_mapping = Attribute('Client Field Mapping', min_version='15.2')
	client_portal_access_enabled = Attribute('Client Portal Access Enabled', min_version='15.2')
