from typing import Union
from pytpp.properties.oauth import Scope
from pytpp.api.websdk.websdk import WebSDK
from packaging.version import Version, parse


class Authenticate:
    """
    Authenticates to TPP WebSDK.
    """
    def __init__(self, host: str, username: str = None, password: str = None, application_id: str = None,
                 scope: Union[Scope, str] = None, websdk_token: str = None, proxies: dict = None,
                 certificate_path: str = None, key_file_path: str = None, verify_ssl: bool = False, **kwargs):
        """
        For WebSDK, either an OAuth bearer token can be obtained, which requires both an Application ID and scope
        to be supplied, or the X-Venafi-API-Key can be obtained, which has been deprecated since TPP version 20.1.

        Using the OAuth authentication method requires an API Application Integration to be created via Aperture
        that defines the maximum possible scope and the users/groups that are authorized to use that scope.

        Args:
            host: Hostname or IP Address of TPP
            username: Username
            password: Password
            application_id: Application ID of the OAuth API Application Integration. Must supply ``scope``.
            scope: Scope of the OAuth API Application Integration to be used. Must supply ``application_id``.
            websdk_token: OAuth Access Bearer Token.
            version: Version of the TPP server.
            proxies: An OrderedDict used by the python Requests library.
            certificate_path: Absolute path to the public certificate file.
            key_file_path: Absolute path to the private key file.
            verify_ssl: If ``True``, verify the SSL certificate of the target endpoints.
        """
        self.websdk = WebSDK(host=host, username=username, password=password, token=websdk_token,
                             application_id=application_id, scope=scope, proxies=proxies,
                             certificate_path=certificate_path, key_file_path=key_file_path,
                             verify_ssl=verify_ssl)
        tpp_version = parse(self.websdk.SystemStatus.Version.get().version)
        self._tpp_version = tpp_version
        self.websdk._session.tpp_version = Version(f'{tpp_version.major}.{tpp_version.minor}')
        self._host = host
        self._username = username
        self._password = password
        self._certificate_path = certificate_path
        self._key_file_path = key_file_path
        self._application_id = application_id
        self._scope = scope
        self._proxies = proxies
        self._verify_ssl = verify_ssl

    @property
    def host(self):
        return self._host

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    def re_authenticate(self, host: str = None, username: str = None, password: str = None,
                        application_id: str = None, scope: str = None, proxies: dict = None,
                        certificate_path: str = None, key_file_path: str = None,
                        verify_ssl: bool = None, **kwargs):
        """
        Performs a re-authentication using the same parameters used to authorize initially.

        Args:
            host: Hostname or IP Address
            username: Username
            password: Password
            application_id: Application ID applicable to OAuth. Must supply ``scope``.
            scope: Scope within the Application. Must supply ``application_id``.
            proxies: An OrderedDict used by the python Requests library.
            certificate_path: Absolute path to the public certificate file.
            key_file_path: Absolute path to the private key file.
            verify_ssl: If ``True``, verify the SSL certificate of the target endpoints.
        """
        if any([host, username, password, application_id, scope, certificate_path, key_file_path, proxies]):
            self.__init__(
                host=host or self._host,
                username=username or self._username,
                password=password or self._password,
                application_id=application_id or self._application_id,
                scope=scope or self._scope,
                version=str(self._tpp_version),
                proxies=self._proxies,
                certificate_path=certificate_path or self._certificate_path,
                key_file_path=key_file_path or self._key_file_path,
                verify_ssl=verify_ssl if verify_ssl is not None else self._verify_ssl
            )
        else:
            self.websdk.re_authenticate()
