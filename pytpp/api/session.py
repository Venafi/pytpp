import requests
import json
from typing import TYPE_CHECKING
from pytpp.attributes._helper import Attribute
if TYPE_CHECKING:
    from packaging.version import Version


class Session:
    """
    This class is responsible for holding the appropriate headers to authenticate each
    request. It also removes all null values from all data sent to TPP.
    """
    def __init__(self, headers: dict, proxies: dict = None, certificate_path: str = None,
                 key_file_path: str = None, verify_ssl: bool = False, tpp_version: 'Version' = None):
        self.requests = requests
        self.requests.packages.urllib3.disable_warnings()
        self.request_kwargs = {
            'headers': headers,
            'verify': verify_ssl
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

    def post(self, url: str, data: dict):
        """
        Sends a POST request to the given URL with the given data.

        Args:
            url: URL endpoint
            data: Dictionary of data

        Returns:
            Returns the raw response returned by the server.
        """
        data = self._remove_null_values_from_dictionary(d=data)
        return self.requests.post(url=url, data=json.dumps(data), **self.request_kwargs)

    def get(self, url: str, params: dict = None):
        """
        Sends a GET request to the given URL with the given URL parameters.

        Args:
            url: URL endpoint
            params: Dictionary of parameters to append to the URL

        Returns:
            Returns the raw response returned by the server.
        """
        params = self._remove_null_values_from_dictionary(d=params)
        return self.requests.get(url=url, params=params, **self.request_kwargs)

    def delete(self, url: str, params: dict = None):
        """
        Sends a DELETE request to the given URL.

        Args:
            url: URL endpoint
            params: Dictionary of parameters to append to the URL

        Returns:
            Returns the raw response returned by the server.
        """
        params = self._remove_null_values_from_dictionary(d=params)
        return self.requests.delete(url, params=params, **self.request_kwargs)

    def put(self, url: str, data: dict):
        """
        Sends a PUT request to the given URL with the given data.

        Args:
            url: URL endpoint
            data: Dictionary of data

        Returns:
            Returns the raw response returned by the server.
        """
        data = self._remove_null_values_from_dictionary(d=data)
        return self.requests.put(url=url, data=json.dumps(data), **self.request_kwargs)

    def _remove_null_values_from_dictionary(self, d: dict):
        """
        Removes all values that are of NoneType recursively within a dictionary.
        """
        if not isinstance(d, dict):
            return d

        for key, value in list(d.items()):
            if self.tpp_version:
                if isinstance(key, Attribute) and key.min_version and self.tpp_version < value.min_version:
                    raise AttributeError(f'The attribute "{key}" is not available until TPP version {key.min_version}.')
                if isinstance(value, Attribute) and value.min_version and self.tpp_version < value.min_version:
                    raise AttributeError(f'The attribute "{value}" is not available until TPP version {value.min_version}.')
                if hasattr(value, '__config_class__'):
                    d[key] = value.__config_class__
            if value is None:
                del d[key]
            elif isinstance(value, dict):
                self._remove_null_values_from_dictionary(value)
        return d
