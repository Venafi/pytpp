from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.log_channel import LogChannelAttributes


class LogSQLChannelAttributes(LogChannelAttributes, metaclass=IterableMeta):
	__config_class__ = "Log SQL Channel"
	create_sql_expression = Attribute('Create SQL Expression')
	dsn = Attribute('DSN')
	dsn_vault_id = Attribute('DSN Vault Id', min_version='18.1')
	database = Attribute('Database')
	expiration = Attribute('Expiration')
	expire_sql_expression = Attribute('Expire SQL Expression')
	last_run = Attribute('Last Run')
	max_log_age_days = Attribute('Max Log Age Days', min_version='16.2')
	table_name = Attribute('Table Name')
	timeout = Attribute('Timeout')
	view_dsn = Attribute('View DSN')
