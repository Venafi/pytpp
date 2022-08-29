import json
import requests
from datetime import datetime
from pydantic import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from packaging.version import Version


class Session:
    """
    This class is responsible for holding the appropriate headers to authenticate each
    request. It also removes all null values from all data sent to TPP.
    """

    def __init__(self, headers: dict, proxies: dict = None, certificate_path: str = None,
                 key_file_path: str = None, verify_ssl: bool = False, tpp_version: 'Version' = None,
                 connection_timeout: float = None, read_timeout: float = None):
        self.requests = requests
        # noinspection PyUnresolvedReferences
        self.requests.packages.urllib3.disable_warnings()
        self.request_kwargs = {
            'headers': headers,
            'verify' : verify_ssl,
            'timeout': (connection_timeout, read_timeout)
        }
        if proxies:
            self.request_kwargs['proxies'] = proxies
        if bool(certificate_path) != bool(key_file_path):
            raise ValueError('The path to both the certificate file and the key file must be '
                             'given for certificate authentication.')
        if certificate_path and key_file_path:
            self.request_kwargs['cert'] = (certificate_path, key_file_path)
        self.tpp_version = tpp_version

    def update_headers(self, new_headers):
        self.request_kwargs['headers'].update(new_headers)

    def delete(self, url: str, params: dict = None):
        """
        Sends a DELETE request to the given URL.

        Args:
            url: URL endpoint
            params: Dictionary of parameters to append to the URL

        Returns:
            Returns the raw response returned by the server.
        """
        return self.requests.delete(url, params=self._sanitize(obj=params), **self.request_kwargs)

    def get(self, url: str, params: dict = None):
        """
        Sends a GET request to the given URL with the given URL parameters.

        Args:
            url: URL endpoint
            params: Dictionary of parameters to append to the URL

        Returns:
            Returns the raw response returned by the server.
        """
        return self.requests.get(url=url, params=self._sanitize(obj=params), **self.request_kwargs)

    def post(self, url: str, data: dict):
        """
        Sends a POST request to the given URL with the given data.

        Args:
            url: URL endpoint
            data: Dictionary of data

        Returns:
            Returns the raw response returned by the server.
        """
        return self.requests.post(url=url, data=self._to_json(obj=data), **self.request_kwargs)

    def put(self, url: str, data: dict):
        """
        Sends a PUT request to the given URL with the given data.

        Args:
            url: URL endpoint
            data: Dictionary of data

        Returns:
            Returns the raw response returned by the server.
        """
        return self.requests.put(url=url, data=self._to_json(obj=data), **self.request_kwargs)

    def _to_json(self, obj):
        sanitized_obj = self._sanitize(obj)
        return json.dumps(sanitized_obj, default=self._json_default)

    @staticmethod
    def _json_default(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return str(obj)

    @staticmethod
    def _validate_value(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return obj

    def _sanitize(self, obj):
        if isinstance(obj, BaseModel):
            obj = obj.dict(by_alias=True, exclude_none=True)
        if isinstance(obj, dict):
            new_values = {}
            for k, v in obj.items():
                if v is None:
                    continue
                new_k = self._validate_value(k)
                new_v = self._sanitize(v)
                new_values[new_k] = new_v
            return new_values
        elif isinstance(obj, (list, tuple, set)):
            return [self._sanitize(item) for item in obj if item is not None]
        else:
            return self._validate_value(obj)
