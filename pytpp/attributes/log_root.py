from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.branch_base import BranchBaseAttributes


class LogRootAttributes(BranchBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "{key}"
    log_application_container = Attribute('Log Application Container')
