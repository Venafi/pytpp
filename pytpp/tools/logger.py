from logboss import Logger, LogTagTypes
from logboss.logger import _LoggerPickler

MASKED_REGEXES = [
    '.*password.*',
    '.*token.*',
    '.*private.*key.*',
    'self',
    'cls',
    'apikey',
]

class LogTags:
    api = LogTagTypes.Debug(name='API')
    feature = LogTagTypes.Info(name='Feature')


logger = Logger()
logger.add_log_tags(LogTags)
_LoggerPickler.MASKED_REGEXES = MASKED_REGEXES
