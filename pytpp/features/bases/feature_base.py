import time
import os
import re
from typing import TYPE_CHECKING
from pytpp.features.definitions.exceptions import InvalidResultCode, ObjectDoesNotExist
from pytpp.properties.response_objects.config import Config
from pytpp.properties.response_objects.identity import Identity
from pytpp.properties.response_objects.dataclasses.config import Object as ConfigObject
from pytpp.properties.response_objects.dataclasses.identity import Identity
from pytpp.tools.logger import logger, LogTags
from pytpp.properties.secret_store import Namespaces
from typing import List, Dict, Union
from packaging.version import Version
if TYPE_CHECKING:
    from pytpp.api.authenticate import Authenticate


def feature(name: str):
    def decorate(cls):
        if int(os.getenv('PYTPP_DOC_IN_PROGRESS', 0)):
            return cls
        setattr(cls, '__feature__', name)
        return logger.wrap_class(
            log_tag=LogTags.feature,
            func_regex_exclude='_.*'
        )(cls)
    return decorate


class FeatureBase:
    def __init__(self, api: 'Authenticate'):
        self._api = api

    def _config_create(self, name: str, parent_folder_dn: str, config_class: str, attributes: dict = None,
                       get_if_already_exists: bool = True, keep_list_values: bool = False):
        if attributes:
            attributes = self._name_value_list(attributes=attributes, keep_list_values=keep_list_values)

        dn = f'{parent_folder_dn}\\{name}'
        response = self._api.websdk.Config.Create.post(object_dn=dn, class_name=str(config_class),
                                                 name_attribute_list=attributes or [])
        result = response.result
        if result.code != 1:
            if result.code == 401 and get_if_already_exists:
                return self._get_config_object(object_dn=dn)
            raise InvalidResultCode(code=result.code, code_description=result.config_result)

        return response.object

    def _config_delete(self, object_dn, recursive: bool = False):
        result = self._api.websdk.Config.Delete.post(object_dn=object_dn, recursive=recursive).result
        if result.code != 1:
            raise InvalidResultCode(code=result.code, code_description=result.config_result)

    def _get_config_object(self, object_dn: str = None, object_guid: str = None,
                           raise_error_if_not_exists: bool = True, valid_class_names: List[str] = None):
        if not (object_dn or object_guid):
            raise ValueError(
                'Must supply either an Object DN or Object GUID, but neither was provided.'
            )
        obj = Config.Object({})
        if isinstance(object_dn, ConfigObject):
            obj = object_dn
        elif isinstance(object_guid, ConfigObject):
            obj = object_guid
        else:
            response = self._api.websdk.Config.IsValid.post(object_dn=object_dn, object_guid=object_guid)
            if response.result.code == 400:
                if raise_error_if_not_exists:
                    raise ObjectDoesNotExist(f'"{object_dn or object_guid}" does not exist.')
            else:
                obj = response.object
        if valid_class_names and obj.type_name not in valid_class_names:
            valid_class_names = "\n".join(f"*  {i}" for i in valid_class_names)
            raise TypeError(f'"{object_dn or object_guid}" exists, but is not the expected class type.\n'
                             f'Got type "{obj.type_name}" instead of one of \n{valid_class_names}.')
        return obj

    def _get_identity_object(self, prefixed_name: str = None, prefixed_universal: str = None,
                             raise_error_if_not_exists: bool = True):
        if not (prefixed_name or prefixed_universal):
            raise ValueError(
                'Must supply either an prefixed_name or prefixed_universal, but neither was provided.'
            )
        if isinstance(prefixed_name, Identity):
            return prefixed_name
        if isinstance(prefixed_universal, Identity):
            return prefixed_universal

        result = self._api.websdk.Identity.Validate.post(
            identity=self._identity_dict(prefixed_name=prefixed_name, prefixed_universal=prefixed_universal)
        )
        if result.is_valid_response() and result.api_response.content:
            identity = result.identity
        elif raise_error_if_not_exists:
            target = prefixed_name or prefixed_universal
            raise ObjectDoesNotExist(f'Could not find identity "{target}".')
        else:
            identity = Identity.Identity(response_object={})
        return identity

    @staticmethod
    def _identity_dict(prefixed_name: str = None, prefixed_universal: str = None):
        """
        Creates an ID object to write to the Identity APIs.

        Args:
            prefixed_name: The prefixed name of the Identity object.
            prefixed_universal: The prefixed universal GUID of the Identity object.

        Returns:
            {
                'PrefixedUniversal': ``prefixed_universal``,
                'PrefixedName': ``prefixed_name``
            }
        """
        d = {}
        if prefixed_name:
            d.update({'PrefixedName': prefixed_name})
        if prefixed_universal:
            d.update({'PrefixedUniversal': prefixed_universal})
        return d

    @staticmethod
    def _is_prefixed_universal(identity):
        if isinstance(identity, str):
            if ':' not in identity:
                return False
            prefix, identity = identity.split(':', maxsplit=1)
            regex = '^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$'
            return bool(re.match(pattern=regex, string=identity))
        return False

    @staticmethod
    def _is_obj_guid(obj: str):
        regex = '^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$'
        return isinstance(obj, str) and bool(re.match(pattern=regex, string=obj))

    def _get_prefixed_name(self, identity: 'Union[Identity, str]'):
        if hasattr(identity, 'prefixed_name'):
            return identity.prefixed_name
        if self._is_prefixed_universal(identity):
            return self._get_identity_object(prefixed_universal=identity).prefixed_name
        return identity

    def _get_prefixed_universal(self, identity: 'Union[Identity, str]'):
        if hasattr(identity, 'prefixed_universal'):
            return identity.prefixed_universal
        if self._is_prefixed_universal(identity):
            return identity
        return self._get_identity_object(prefixed_name=identity).prefixed_universal

    def _get_dn(self, obj: 'Union[Config.Object, str]', parent_dn: str = None):
        if hasattr(obj, 'dn'):
            return obj.dn
        if self._is_obj_guid(obj):
            return self._get_config_object(object_guid=obj).dn
        if parent_dn and not obj.startswith(parent_dn):
            obj = parent_dn.rstrip('\\') + '\\' + obj.rstrip('\\')
        if not obj.startswith(r'\VED'):
            return '\\VED\\' + obj.strip("\\")
        else:
            return obj

    def _get_guid(self, obj: 'Union[Config.Object, str]', parent_dn: str = None):
        if hasattr(obj, 'guid'):
            return obj.guid
        if self._is_obj_guid(obj):
            return obj
        if parent_dn and not obj.startswith(parent_dn):
            obj = parent_dn.rstrip('\\') + f'\\{obj}'
        if not obj.startswith(r'\VED'):
            obj = '\\VED\\' + obj.strip("\\")
        return self._get_config_object(object_dn=obj).guid

    @staticmethod
    def _log_warning_message(msg: str):
        logger.warning(msg=msg, num_prev_callers=2)

    @staticmethod
    def __no_op(*args, **kwargs):
        pass

    @staticmethod
    def _name_type_value(name: str, type: str, value):
        return {'Name': str(name), 'Type': str(type), 'Value': str(value)}

    @staticmethod
    def _name_value_list(attributes: Dict[str, List[str]], keep_list_values: bool = False):
        nvl = []
        for name, value in attributes.items():
            if value is None:
                continue
            elif isinstance(value, list):
                if keep_list_values is True:
                    nvl.append({'Name': str(name), 'Value': value})
                else:
                    for v in value:
                        nvl.append({'Name': str(name), 'Value': str(v)})
            elif not isinstance(value, dict):
                nvl.append({'Name': str(name), 'Value': str(value)})
        return nvl

    def _secret_store_delete(self, object_dn: str, namespace: str = Namespaces.config):
        result = self._api.websdk.SecretStore.OwnerDelete.post(namespace=namespace, owner=object_dn).result
        if result.code != 0:
            raise InvalidResultCode(code=result.code, code_description=result.secret_store_result)

    def _is_version_compatible(self, minimum: str = '', maximum: str = ''):
        if minimum and self._api._tpp_version <= Version(minimum):
            logger.error(f'Incompatible version. This feature requires at least TPP {minimum}.')
            return False
        if maximum and self._api._tpp_version >= Version(maximum):
            logger.error(f'Incompatible version. This feature is no longer available after TPP {maximum}.')
            return False
        return True

    class _Timeout:
        def __init__(self, timeout):
            self.timeout = timeout
            self.max_time = timeout + time.time()

        def __enter__(self):
            logger.set_rule(
                log_tag=LogTags.feature,
                blacklist_function=lambda x: x is LogTags.api,
                why=f'Disabling all logs during timeout to reduce redundant logging.'
            )
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            logger.set_rule(
                log_tag=LogTags.feature,
                reset=True,
                why=f'Enabling all logs after timeout.'
            )
            return

        def is_expired(self, poll: float = 0.5):
            time.sleep(poll)
            return time.time() >= self.max_time
