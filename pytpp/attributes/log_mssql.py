from pytpp.attributes._helper import IterableMeta
from pytpp.attributes.log_sql_channel import LogSQLChannelAttributes


class LogMSSQLAttributes(LogSQLChannelAttributes, metaclass=IterableMeta):
	__config_class__ = "Log MSSQL"
