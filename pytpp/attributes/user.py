from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.person import PersonAttributes


class UserAttributes(PersonAttributes, metaclass=IterableMeta):
	__config_class__ = "User"
	creation_date = Attribute('Creation Date')
	password = Attribute('Password')
