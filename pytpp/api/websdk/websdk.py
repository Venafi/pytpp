from typing import Union
from pytpp.tools.logger import logger, LogTags
from pytpp.api.session import Session
from pytpp.properties.oauth import Scope
from pytpp.api.websdk.endpoints.authorize import _Authorize
from pytpp.api.websdk.endpoints.certificates import _Certificates
from pytpp.api.websdk.endpoints.client import _Client
from pytpp.api.websdk.endpoints.codesign import _Codesign
from pytpp.api.websdk.endpoints.config import _Config
from pytpp.api.websdk.endpoints.config_schema import _ConfigSchema
from pytpp.api.websdk.endpoints.credentials import _Credentials
from pytpp.api.websdk.endpoints.crypto import _Crypto
from pytpp.api.websdk.endpoints.discovery import _Discovery
from pytpp.api.websdk.endpoints.flow import _Flow
from pytpp.api.websdk.endpoints.hsm_api import _HSMAPI
from pytpp.api.websdk.endpoints.identity import _Identity
from pytpp.api.websdk.endpoints.log import _Log
from pytpp.api.websdk.endpoints.metadata import _Metadata
from pytpp.api.websdk.endpoints.permissions import _Permissions
from pytpp.api.websdk.endpoints.pki import _PKI
from pytpp.api.websdk.endpoints.preferences import _Preferences
from pytpp.api.websdk.endpoints.processing_engines import _ProcessingEngines
from pytpp.api.websdk.endpoints.revoke import _Revoke
from pytpp.api.websdk.endpoints.secret_store import _SecretStore
from pytpp.api.websdk.endpoints.ssh import _SSH
from pytpp.api.websdk.endpoints.ssh_certificates import _SSHCertificates
from pytpp.api.websdk.endpoints.stats import _Stats
from pytpp.api.websdk.endpoints.system_status import _SystemStatus
from pytpp.api.websdk.endpoints.teams import _Teams
from pytpp.api.websdk.endpoints.workflow import _Workflow
from pytpp.api.websdk.endpoints.x509_certificate_store import _X509CertificateStore


class WebSDK:
    """
    Initializes a WebSDK session via username/password. Certificate authentication is not
    currently supported. Re-authentication occurs automatically when the API Key
    becomes invalidated. When initialized, all endpoints are also initialized.
    """
    @logger.wrap_func(log_tag=LogTags.api, mask_input_regexes=['password', 'token'])
    def __init__(self, host: str, username: str, password: str, token: str = None, application_id: str = None,
                 scope: Union[Scope, str] = None, refresh_token: str = None, proxies: dict = None,
                 certificate_path: str = None, key_file_path: str = None, verify_ssl: bool = False):
        """
        Authenticates the given user to WebSDK. The only supported method for authentication at this time
        is with a username and password. Either an OAuth bearer token can be obtained, which requires
        both an Application ID and scope to be supplied, or the X-Venafi-API-Key can be obtained, which has
        been deprecated since TPP version 20.1.

        Using the OAuth authentication method requires an API Application Integration to be created that
        defines the maximum possible scope and the users/groups that are authorized to use that scope. That
        can be accomplished through Aperture. The ``scope`` parameter simply has to define the subset of
        allowed scopes defined by that application.

        Args:
            host: Hostname or IP Address of TPP
            username: Username
            password: Password
            token: OAuth Access Bearer Token
            application_id: Application ID of the OAuth API Application Integration. Must supply ``scope``.
            scope: Scope of the OAuth API Application Integration to be used. Must supply ``application_id``.
            proxies: An OrderedDict used by the python Requests library.
            certificate_path: Absolute path to the public certificate file.
            key_file_path: Absolute path to the private key file.
            verify_ssl: If ``True``, verify the SSL certificate of the target endpoints.
        """
        # region Instance Variables
        self._host = host
        self._username = username
        self._password = password
        self._application_id = application_id
        self._oauth = None
        self._token = None
        self._proxies = proxies
        self._certificate_path = certificate_path
        self._key_file_path = key_file_path
        self._verify_ssl = verify_ssl

        # This is used by the endpoints to avoid redundancy.
        self._base_url = f'https://{host}/vedsdk'
        # endregion Instance Variables

        # region Authentication
        # This is used by the endpoints to authorize the API writes.
        self._session = Session(
            headers={'Content-Type': 'application/json'}, proxies=self._proxies,
            certificate_path=certificate_path, key_file_path=key_file_path,
            verify_ssl=verify_ssl
        )

        # Authorize the WebSDK session and store the API token.
        self.Authorize = _Authorize(self)

        if not token:
            if application_id:
                if not scope:
                    raise ValueError(f'OAuth authentication requires both an Application ID and a scope be. '
                                     f'The scope was not defined.')
                elif isinstance(scope, Scope):
                    scope = scope.to_string()

                if certificate_path and key_file_path:
                    oauth = self.Authorize.Certificate.post(
                        client_id=application_id,
                        scope=scope
                    )
                else:
                    oauth = self.Authorize.OAuth.post(
                        client_id=application_id,
                        username=username,
                        password=password,
                        scope=scope
                    )
                self._oauth = oauth
                token = oauth.access_token
            else:
                # Deprecated since TPP Version 20.1
                token = self.Authorize.post(username=username, password=password).token
        elif refresh_token:
            oauth = self.Authorize.Token.post(
                client_id=application_id,
                refresh_token=refresh_token
            )
            self._oauth = oauth
            token = oauth.access_token

        if token.endswith('=='):
            self._token = f'Bearer {token}'
            authorization_header = {
                'Authorization': self._token
            }
        else:
            self._token = token
            authorization_header = {
                'X-Venafi-API-Key': self._token
            }
        self._session.update_headers(authorization_header)
        # endregion Authentication

        # region Initialize All WebSDK Endpoints
        # Initialize the rest of the endpoints with self, which contains the base url,
        # the authorization token, and the re-authentication method.
        self.Certificates = _Certificates(self)
        self.Client = _Client(self)
        self.Codesign = _Codesign(self)
        self.Config = _Config(self)
        self.ConfigSchema = _ConfigSchema(self)
        self.Credentials = _Credentials(self)
        self.Crypto = _Crypto(self)
        self.Discovery = _Discovery(self)
        self.Flow = _Flow(self)
        self.HSMAPI = _HSMAPI(self)
        self.Identity = _Identity(self)
        self.Log = _Log(self)
        self.Metadata = _Metadata(self)
        self.Permissions = _Permissions(self)
        self.PKI = _PKI(self)
        self.Preferences = _Preferences(self)
        self.ProcessingEngines = _ProcessingEngines(self)
        self.Revoke = _Revoke(self)
        self.SecretStore = _SecretStore(self)
        self.SSH = _SSH(self)
        self.SSHCertificates = _SSHCertificates(self)
        self.Stats = _Stats(self)
        self.SystemStatus = _SystemStatus(self)
        self.Teams = _Teams(self)
        self.Workflow = _Workflow(self)
        self.X509CertificateStore = _X509CertificateStore(self)
        # endregion Initialize All WebSDK Endpoints

    def re_authenticate(self):
        """
        Performs a re-authentication using the same parameters used to authorize initially.
        """
        if self._oauth is not None:
            self.__init__(
                host=self._host,
                username=self._username,
                password=self._password,
                certificate_path=self._certificate_path,
                key_file_path=self._key_file_path,
                verify_ssl=self._verify_ssl,
                proxies=self._proxies,
                application_id=self._application_id,
                scope=self._oauth.scope,
                refresh_token=self._oauth.refresh_token,
            )
        else:
            self.__init__(
                host=self._host,
                username=self._username,
                password=self._password,
                certificate_path=self._certificate_path,
                key_file_path=self._key_file_path,
                verify_ssl=self._verify_ssl,
                proxies=self._proxies
            )
