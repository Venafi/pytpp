from typing import Union
import re
import json
from pytpp.api.session import Session
from requests import Response, HTTPError
from pytpp.tools.logger import logger, LogTags


def api_response_property(return_on_204: type = None):
    """
    This function serves as a decorator for all API response objects. Each
    response property must be validated before returning the object. This
    function depends upon the API class.

    The ``on_204`` parameter suggests what data type is expected to be
    returned when the response status code is valid, but has no content.
    Since there is no content to return, an empty object representing that
    object will be returned instead. For example,

    .. code-block:: python

        # No 204 should ever be returned, so just validate the response
        # status codes and return the object on 200.
        @property
        @api_response_property()
        def value1(self) -> str:
            return self._from_json(key='Value1')

        # 204 could be returned by TPP, so just send an empty response
        # of the same object type as the expected response.
        @property
        @api_response_property(on_204=list)
        def value2(self) -> list:
            return self._from_json(key='Value2')

    Args:
        return_on_204: type

    Returns: Key of response content returned by TPP.

    """
    def pre_validation(func):
        def wrap(self: APIResponse, *args, **kwargs):
            if not self._validated:
                self._validate()
            if return_on_204 and self.api_response.status_code == 204:
                if callable(return_on_204):
                    return return_on_204()
                else:
                    return return_on_204
            return func(self, *args, **kwargs)
        return wrap
    return pre_validation


class API:
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
        self._api_obj = api_obj
        if not url.startswith('/'):
            url = '/' + url
        self._url = self._api_obj._base_url + url
        self.retries = 3

    @property
    def _session(self) -> 'Session':
        return self._api_obj._session

    def _is_api_key_invalid(self, response: Response):
        """
        Uses a regular expression to search the response text for an indication that the API key
        is expired.

        Args:
            response: The raw response object.

        Returns:
            Returns True if the API key expired. Otherwise False.

        """
        return response.status_code == 401 and bool(re.match('.*API key.*is not valid.*', response.text))

    def _delete(self, params: dict = None):
        """
        Performs a DELETE method request. If the response suggests the API Key is expired, then
        a single attempt is made to re-authenticate to TPP. Otherwise, the raw response is returned.

        Returns:
            Returns the raw JSON response.
        """
        self._log_rest_call(method='DELETE', data=params)
        retried = 0
        exc = None
        while retried < self.retries:
            try:
                response = self._session.delete(url=self._url, params=params)
                self._log_response(response=response)
                if self._is_api_key_invalid(response=response):
                    self._re_authenticate()
                    return self._session.delete(url=self._url, params=params)
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            retried += 1
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
        retried = 0
        exc = None
        while retried < self.retries:
            try:
                response = self._session.get(url=self._url, params=params)
                self._log_response(response=response)
                if self._is_api_key_invalid(response=response):
                    self._re_authenticate()
                    return self._session.get(url=self._url, params=params)
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            retried += 1
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
        retried = 0
        exc = None
        while retried < self.retries:
            try:
                response = self._session.post(url=self._url, data=data)
                self._log_response(response=response)
                if self._is_api_key_invalid(response=response):
                    self._re_authenticate()
                    return self._session.post(url=self._url, data=data)
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            retried += 1
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
        retried = 0
        exc = None
        while retried < self.retries:
            try:
                response = self._session.put(url=self._url, data=data)
                self._log_response(response=response)
                if self._is_api_key_invalid(response=response):
                    self._re_authenticate()
                    self._session.put(url=self._url, data=data)
                return response
            except (ConnectionResetError, ConnectionError) as e:
                exc = e
            retried += 1
        raise exc

    def _re_authenticate(self):
        """
        The current API token expired and the session needs to be re-authenticated.
        """
        logger.log(
            msg=f'{self._api_obj.__class__.__name__} API authentication token expired. Re-authenticating...',
            log_tag=LogTags.api
        )
        self._api_obj.re_authenticate()

    def _log_api_deprecated_warning(self, alternate_api: str = None, num_prev_callers=2):
        msg = f'API DEPRECATION WARNING: {self._url} is no longer supported by Venafi.'
        if alternate_api:
            msg += f'\nUse {alternate_api} instead.'
        logger.warning(
            msg=msg,
            num_prev_callers=num_prev_callers
        )

    def _log_rest_call(self, method: str, data: dict = None, num_prev_callers: int = 3):
        """
        Logs the URL and any additional data. This enforces consistency in logging across all API calls.
        """
        if data:
            payload = logger._jsonpickle.dumps(data)
            logger.log(
                msg=f'{method}\nURL: {self._url}\nBODY: {payload}',
                log_tag=LogTags.api,
                num_prev_callers=num_prev_callers
            )
        else:
            logger.log(
                msg=f'{method}\nURL: {self._url}',
                log_tag=LogTags.api,
                num_prev_callers=3
            )

    def _log_response(self, response: Response, num_prev_callers: int = 3):
        """
        Logs the URL, response code, and the content returned by TPP.
        This enforces consistency in logging across all API calls.
        """
        try:
            pretty_json = logger._jsonpickle.dumps(response.json())
        except json.JSONDecodeError:
            pretty_json = response.text or response.reason or 'No Content'
        except:
            pretty_json = 'No Content'

        logger.log(
            msg=f'URL: "{self._url}"\nRESPONSE CODE: {response.status_code}\nCONTENT: {pretty_json}',
            log_tag=LogTags.api,
            num_prev_callers=num_prev_callers
        )

class APIResponse:
    def __init__(self, response: Response):
        """
        """
        self._api_response = response
        self._decoded_api_response = None
        self._validated = False

    @property
    def api_response(self):
        return self._api_response

    @api_response.setter
    def api_response(self, value):
        # When set, a new raw response is stored and hasn't been validated, so invalidate.
        self._validated = False
        self._api_response = value

    def assert_valid_response(self):
        """
        Use this method when no response property is available after an API call or to simply
        throw an error if the return code is invalid. This simply asserts that a valid response
        status code was returned by TPP.
        """
        if not self._validated:
            self._validate()

    def is_valid_response(self):
        """
        Returns ``True`` when the response is valid, meaning a valid return code was returned by
        TPP, otherwise ``False``.
        """
        try:
            self._validate()
            return True
        except:
            return False

    def _from_json(self, key: str = None, error_key: str = None, return_on_error: type = None):
        """
        Returns the particular key within the response dictionary. If no key is provided, then
        the full response is returned as a dictionary.

        If ``key`` is provided, then it is searched in the response content. It is not case
        sensitive. If ``key`` is not found, an error is thrown and logged.

        TPP often returns a key with an error message. When an ``error_key`` is provided and an
        error message is returned an error is thrown and logged with the message provided by TPP.

        Args:
            key: Key within the top level of the response content.
            error_key: Error key within the top level of the response content.
            return_on_error: If an error occurs in retrieving content or accessing a key, this
                type will be returned instead of throwing an error.

        Returns:
            If a key is provided, returns the response content at that key. Otherwise, the full
            response content.
        """
        try:
            result = self.api_response.json()
        except json.decoder.JSONDecodeError:
            if return_on_error:
                return return_on_error()
            raise InvalidResponseError(f'{self.api_response.url} return no content. '
                                       f'Got status code {self.api_response.status_code}.')
        if error_key and error_key in result.keys():
            raise InvalidResponseError('An error occurred: "%s"' % result[error_key])
        if not key:
            return result
        for k in result.keys():
            if key.lower() == k.lower():
                return result[k]

        if return_on_error:
            return return_on_error()
        raise KeyError(f'{key} was not returned by TPP.')

    def _validate(self):
        """
        Validates the current response property by validating that there are expected return codes
        and that the actual return code is one of the valid return codes. If the return code is
        invalid, an error is thrown and logged.
        """
        self._validated = True
        try:
            self.api_response.raise_for_status()
        except HTTPError as err:
            error_msg = self.api_response.text or self.api_response.reason or 'No error message found.'
            body = logger._jsonpickle.dumps(
                json.loads(err.request.body)
            ) if err.request.body else ''
            raise InvalidResponseError('\n'.join(err.args) + f"\nERROR: {error_msg}\nCONTENT: {body}")


class InvalidResponseError(Exception):
    pass
