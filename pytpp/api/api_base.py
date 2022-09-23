import re
import json
import time
import pydantic.main
from datetime import datetime
from pydantic.fields import Undefined
from requests import Response, HTTPError
from pydantic import BaseModel, root_validator, Field
from pytpp.tools.logger import api_logger, json_pickler
from typing import Any, Callable, Optional, Union, Protocol, TYPE_CHECKING, Type, TypeVar, get_origin

if TYPE_CHECKING:
    from pydantic.typing import AbstractSetIntStr, MappingIntStrAny, NoArgAnyCallable
    from pytpp.api.session import Session

T_ = TypeVar('T_')


class ApiModelMetaclass(pydantic.main.ModelMetaclass):
    def __new__(mcs, name, bases, namespaces, **kwargs):
        annotations = namespaces.get('__annotations__', {})
        for base in bases:
            annotations.update(getattr(base, '__annotations__', {}))
        for field in annotations:
            if not field.startswith('__') and get_origin(annotations[field]) is not Union:
                annotations[field] = Union[annotations[field], Any]
        namespaces['__annotations__'] = annotations
        return super().__new__(mcs, name, bases, namespaces, **kwargs)


# region Endpoint Definitions
class ApiSource(Protocol):
    _host: str
    _username: str
    _password: str
    _token: str
    _base_url: str
    _app_url: str
    _scheme: str
    _session: 'Session'

    def re_authenticate(self): ...


class ApiEndpoint(object):
    """
    This is the backbone of all API definitions. It performs all requests,
    validations, logging, re-authentication, and holds the raw response. This
    class MUST be inherited by all API definitions.
    """

    def __init__(self, api_obj, url: str):
        """
        Args:
            api_obj: This is passed down from the API type object (eg. WebSDK, etc.) and
                represents that type. This type is REQUIRED because it contains the
                authenticated sessions, base URL, and re-authentication methods. It is
                through these properties this class is able to send and receive requests
                to TPP.
            url: This is the URL extension from the base URL.
        """
        self._api_obj: 'ApiSource' = api_obj
        url = url.strip('/')
        if url.startswith(self._api_obj._base_url):
            self._url = url
        else:
            self._url = f'{self._api_obj._app_url}/{url}'
        self._retries = 3
        self.retry_interval = 0.5

    @property
    def retries(self):
        return self._retries + 1  # The first time isn't a "retry".

    @property
    def _session(self) -> 'Session':
        return self._api_obj._session

    def _should_re_authenticate(self, response: 'Response'):
        return response.status_code == 401 and self._api_obj._token is not None

    @staticmethod
    def _rerun_transaction_required(response: Response):
        """
        Uses a regular expression to search the response text for an indication that the transaction was deadlocked
        and needs to be reran.

        Args:
            response: The raw response object.

        Returns:
            Returns ``True`` if the API key expired. Otherwise ``False``.
        """
        return response.status_code == 500 and bool(re.match('.*rerun the transaction.*', response.text,
                                                             flags=re.IGNORECASE))

    def _delete(self, params: dict = None):
        """
        Performs a DELETE method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate to TPP. Otherwise, the raw response is returned.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(method='DELETE', data=params)
        exc = None
        for _ in range(self.retries):
            try:
                response = self._session.delete(url=self._url, params=params)
                self._log_response(response=response)
                if self._should_re_authenticate(response=response):
                    self._re_authenticate()
                    # Trigger the retry.
                    continue
                elif self._rerun_transaction_required(response=response):
                    # Trigger the retry.
                    continue
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            time.sleep(self.retry_interval)
        raise exc

    def _get(self, params: dict = None):
        """
        Performs a GET method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate to TPP. Otherwise, the raw response is returned.

        Args:
            params: A dictionary of URL parameters to append to the URL.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(method='GET', data=params)
        exc = None
        for _ in range(self.retries):
            try:
                response = self._session.get(url=self._url, params=params)
                self._log_response(response=response)
                if self._should_re_authenticate(response=response):
                    self._re_authenticate()
                    # Trigger the retry.
                    continue
                elif self._rerun_transaction_required(response=response):
                    # Trigger the retry.
                    continue
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            time.sleep(self.retry_interval)
        raise exc

    def _post(self, data: Union[list, dict]):
        """
        Performs a POST method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate to TPP. Otherwise, the raw response is returned.

        Args:
            data: A dictionary of data to send with the URL.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(method='POST', data=data)
        exc = None
        for _ in range(self.retries):
            try:
                response = self._session.post(url=self._url, data=data)
                self._log_response(response=response)
                if self._should_re_authenticate(response=response):
                    self._re_authenticate()
                    # Trigger the retry.
                    continue
                elif self._rerun_transaction_required(response=response):
                    # Trigger the retry.
                    continue
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            time.sleep(self.retry_interval)
        raise exc

    def _put(self, data: Union[list, dict]):
        """
        Performs a PUT method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate to TPP. Otherwise, the raw response is returned.

        Args:
            data: A dictionary of data to send with the URL.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(method='PUT', data=data)
        exc = None
        for _ in range(self.retries):
            try:
                response = self._session.put(url=self._url, data=data)
                self._log_response(response=response)
                if self._should_re_authenticate(response=response):
                    self._re_authenticate()
                    # Trigger the retry.
                    continue
                elif self._rerun_transaction_required(response=response):
                    # Trigger the retry.
                    continue
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            time.sleep(self.retry_interval)
        raise exc

    def _re_authenticate(self):
        """
        The current API token expired and the session needs to be re-authenticated.
        """
        api_logger.debug(
            f'{self._api_obj.__class__.__name__} API authentication token expired. Re-authenticating...',
            stacklevel=2
        )
        self._api_obj.re_authenticate()

    def _log_api_deprecated_warning(self, alternate_api: str = None):
        msg = f'API DEPRECATION WARNING: {self._url} is no longer supported by Venafi.'
        if alternate_api:
            msg += f'\nUse {alternate_api} instead.'
        api_logger.warning(msg, stacklevel=2)

    def _log_rest_call(self, method: str, data: dict = None):
        """
        Logs the URL and any additional data. This enforces consistency in logging across all API calls.
        """
        if data:
            payload = json_pickler.dumps(data)
            api_logger.debug(
                f'{method}\nURL: {self._url}\nBODY: {payload}',
                stacklevel=2
            )
        else:
            api_logger.debug(
                msg=f'{method}\nURL: {self._url}',
                stacklevel=2
            )

    def _log_response(self, response: Response):
        """
        Logs the URL, response code, and the content returned by TPP.
        This enforces consistency in logging across all API calls.
        """
        try:
            pretty_json = json_pickler.dumps(response.json())
        except json.JSONDecodeError:
            pretty_json = response.text or response.reason or 'No Content'
        except:
            pretty_json = 'No Content'

        api_logger.debug(
            msg=f'URL: "{self._url}"\nRESPONSE CODE: {response.status_code}\nCONTENT: {pretty_json}',
            stacklevel=2
        )


class WebSdkEndpoint(ApiEndpoint):  ...


# endregion Endpoint Definitions


# region Model And Field Definitions
def ApiField(default: Any = None, *, default_factory: 'Optional[NoArgAnyCallable]' = None, alias: str = None, title: str = None,
             description: str = None, exclude: 'Union[AbstractSetIntStr, MappingIntStrAny, Any]' = None,
             include: 'Union[AbstractSetIntStr, MappingIntStrAny, Any]' = None, const: bool = None, gt: float = None,
             ge: float = None, lt: float = None, le: float = None, multiple_of: float = None, max_digits: int = None,
             decimal_places: int = None, min_items: int = None, max_items: int = None, unique_items: bool = None,
             min_length: int = None, max_length: int = None, allow_mutation: bool = True, regex: str = None,
             discriminator: str = None, repr: bool = True, converter: Callable[[Any], Any] = None, **extra: Any) -> Any:
    if callable(default_factory):
        default = Undefined
    if converter is not None and callable(converter):
        extra['converter'] = converter
    return Field(default=default, default_factory=default_factory, alias=alias, title=title, description=description,
                 exclude=exclude, include=include, const=const, gt=gt, ge=ge, lt=lt, le=le, multiple_of=multiple_of,
                 max_digits=max_digits, decimal_places=decimal_places, min_items=min_items, max_items=max_items,
                 unique_items=unique_items, min_length=min_length, max_length=max_length, allow_mutation=allow_mutation,
                 regex=regex, discriminator=discriminator, repr=repr, **extra)


# region Output Models
def generate_output(response: Response, output_cls: Type[T_], root_field: str = None) -> T_:
    """
    Args:
        response: Response instance returned by the ``requests`` call to the server.
        output_cls: Custom APIResponse class.
        root_field: In the case that the returned JSON is an array of objects, then the ``root_field``
            is used to assign that value.

    Returns:
        An instance of ``response_cls``.
    """
    try:
        result = response.json()
    except:
        result = {}
    if not isinstance(result, dict):
        result = {str(root_field): result} if root_field else {}
    elif root_field:
        result = {
            str(root_field): result,
            **result
        }
    response_inst = output_cls(api_response=response, **result)
    try:
        response.raise_for_status()
        if isinstance(result, dict) and (error_key := getattr(response_inst, 'error', 'Unknown')) in result.keys():
            # There is an error message, but the status is a valid status, so just log the error instead.
            api_logger.error('An error occurred: "%s"' % result[error_key], response=response)
        return response_inst
    except HTTPError as error:
        if isinstance(result, dict) and (error_msg := getattr(response_inst, 'error', None)) is not None:
            raise InvalidResponseError(f'An error occurred: "{error_msg}"', response=response) from error
        raise InvalidResponseError(str(error), response=response)


class ObjectModel(BaseModel, metaclass=ApiModelMetaclass):
    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

    @root_validator(pre=True, allow_reuse=True)
    def _case_insensitive_validator(cls, values: dict):
        new_values = {}
        lowered_values = {k.lower(): v for k, v in values.items()}
        for fk, fv in cls.__fields__.items():
            if fv.name in values:
                new_value = values[fv.name]
            elif fv.alias.lower() in lowered_values:
                new_value = lowered_values[fv.alias.lower()]
            else:
                continue
            if fv.type_ is datetime and '\\Date' in new_value:
                new_value = re.sub(r'\D', '', new_value)
            if (converter := fv.field_info.extra.get('converter')) is not None:
                new_value = converter(new_value)
            new_values[fv.alias] = new_value
        return new_values


class RootOutputModel(ObjectModel):
    api_response: Response = ApiField(alias='api_response', exclude=True)

    class Config(ObjectModel.Config):
        fields = {'api_response': {'exclude': True}}

    def assert_valid_response(self):
        """
        Use this method when no response property is available after an API call or to simply
        throw an error if the return code is invalid. This simply asserts that a valid response
        status code was returned by TPP.
        """
        self.api_response.raise_for_status()

    def is_valid_response(self):
        """
        Returns ``True`` when the response is valid, meaning a valid return code was returned by
        TPP, otherwise ``False``.
        """
        try:
            self.api_response.raise_for_status()
            return True
        except:
            return False


class WebSdkOutputModel(RootOutputModel):
    error: str = ApiField(alias='Error')


# endregion Output Models


class InvalidResponseError(Exception):
    def __init__(self, msg: str, response: Response):
        self.response = response
        super().__init__(msg, response)
# endregion Response Definitions
