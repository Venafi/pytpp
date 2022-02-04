from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.top import TopAttributes


class GroupAttributes(TopAttributes, metaclass=IterableMeta):
	__config_class__ = "Group"
	assets = Attribute('Assets', min_version='20.1')
	closed_group = Attribute('Closed Group', min_version='20.1')
	foreign_security_principal = Attribute('Foreign Security Principal', min_version='19.3')
	full_name = Attribute('Full Name')
	group_membership = Attribute('Group Membership')
	member = Attribute('Member')
	owner = Attribute('Owner', min_version='20.1')
	products = Attribute('Products', min_version='20.1')
	suggested_member = Attribute('Suggested Member', min_version='20.1')
	team_member_added_by = Attribute('Team Member Added By', min_version='20.3')
	team_member_added_on = Attribute('Team Member Added On', min_version='20.3')
