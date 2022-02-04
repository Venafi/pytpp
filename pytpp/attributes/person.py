from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class PersonAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Person"
	full_name = Attribute('Full Name')
	given_name = Attribute('Given Name')
	group_membership = Attribute('Group Membership')
	internet_email_address = Attribute('Internet EMail Address')
	language = Attribute('Language')
	surname = Attribute('Surname')
