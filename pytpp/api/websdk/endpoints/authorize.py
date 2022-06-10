import logging
import warnings
from datetime import datetime
from pytpp.tools.logger import api_logger
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.tools.helpers.date_converter import from_date_string


class _Authorize(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Authorize')

        self.Certificate = self._Certificate(api_obj=api_obj)
        self.Device = self._Device(api_obj=api_obj)
        self.Integrated = self._Integrated(api_obj=api_obj)
        self.OAuth = self._OAuth(api_obj=api_obj)
        self.Token = self._Token(api_obj=api_obj)
        self.Verify = self._Verify(api_obj=api_obj)

    def post(self, username, password):
        """
        This POST method is written differently in order to effectively omit the password from being logged.
        """
        warnings.warn('Authorizing to TPP with only a username and password is being deprecated. '
                      'Refer to product documentation on using OAuth authentication.')
        body = {
            "Username": username,
            "Password": password
        }

        class _Response(APIResponse):
            def __init__(self, r):
                super().__init__(response=r)

            @property
            @api_response_property()
            def token(self) -> str:
                return self._from_json('APIKey')

        api_logger.debug(f'Authenticating to TPP as "{username}"...')
        with api_logger.suppressed(logging.WARNING):
            response = self._post(data=body)
        api_logger.debug(f'Authenticated as "{username}"!')
        return _Response(response)

    class _Certificate(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Authorize/Certificate')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, scope: str):
            body = {
                'client_id': client_id,
                'scope': scope
            }

            class _Response(APIResponse):
                def __init__(self, r):
                    super().__init__(response=r)

                @property
                @api_response_property()
                def access_token(self) -> str:
                    return self._from_json('access_token')

                @property
                @api_response_property()
                def expires(self):
                    return datetime.fromtimestamp(self._from_json('expires'))

                @property
                @api_response_property()
                def expires_in(self) -> int:
                    return self._from_json(key='expires_in')

                @property
                @api_response_property()
                def identity(self) -> str:
                    return self._from_json('identity')

                @property
                @api_response_property()
                def refresh_token(self) -> str:
                    return self._from_json('refresh_token')

                @property
                @api_response_property()
                def refresh_until(self):
                    return datetime.fromtimestamp(self._from_json(key='refresh_until'))

                @property
                @api_response_property()
                def scope(self) -> str:
                    return self._from_json('scope')

                @property
                @api_response_property()
                def token_type(self) -> str:
                    return self._from_json('token_type')

            api_logger.debug(f'Authenticating to TPP OAuth Application "{client_id}" '
                             f'with scope "{scope}" using a certificate file...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated!')
            return _Response(response)

    class _Device(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Authorize/Device')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, scope: str):
            body = {
                'client_id': client_id,
                'scope'    : scope
            }

            class _Response(APIResponse):
                def __init__(self, r):
                    super().__init__(response=r)

                @property
                @api_response_property()
                def device_code(self) -> str:
                    return self._from_json('device_code')

                @property
                @api_response_property()
                def interval(self) -> int:
                    return self._from_json('interval')

                @property
                @api_response_property()
                def user_code(self) -> str:
                    return self._from_json(key='user_code')

                @property
                @api_response_property()
                def verification_uri(self) -> str:
                    return self._from_json('verification_uri')

                @property
                @api_response_property()
                def verification_url_complete(self) -> str:
                    return self._from_json('verification_uri_complete')

                @property
                @api_response_property()
                def expires_in(self) -> int:
                    return self._from_json(key='expires_in')

                @property
                @api_response_property()
                def expires(self) -> int:
                    return self._from_json('expires')

            api_logger.debug(f'Authenticating to TPP OAuth Application "{client_id}" '
                             f'with scope "{scope}" using a certificate file...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated!')
            return _Response(response)

    class _Integrated(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Authorize/Integrated')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, scope: str, state: str = None):
            body = {
                'client_id': client_id,
                'scope'    : scope,
                'state'    : state
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def access_token(self) -> str:
                    return self._from_json('access_token')

                @property
                @api_response_property()
                def expires(self):
                    return datetime.fromtimestamp(self._from_json('expires'))

                @property
                @api_response_property()
                def expires_in(self) -> int:
                    return self._from_json(key='expires_in')

                @property
                @api_response_property()
                def identity(self) -> str:
                    return self._from_json('identity')

                @property
                @api_response_property()
                def refresh_token(self) -> str:
                    return self._from_json('refresh_token')

                @property
                @api_response_property()
                def refresh_until(self):
                    return datetime.fromtimestamp(self._from_json(key='refresh_until'))

                @property
                @api_response_property()
                def scope(self) -> str:
                    return self._from_json('scope')

                @property
                @api_response_property()
                def token_type(self) -> str:
                    return self._from_json('token_type')

            return _Response(response=self._post(data=body))

    class _OAuth(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Authorize/OAuth')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, password: str, scope: str, username: str, state: str = None):
            body = {
                'client_id': client_id,
                'password': password,
                'scope': scope,
                'username': username,
                'state': state
            }

            class _Response(APIResponse):
                def __init__(self, r):
                    super().__init__(response=r)

                @property
                @api_response_property()
                def access_token(self) -> str:
                    return self._from_json('access_token')

                @property
                @api_response_property()
                def expires(self) -> str:
                    return self._from_json('expires')

                @property
                @api_response_property()
                def identity(self) -> str:
                    return self._from_json('identity')

                @property
                @api_response_property()
                def refresh_token(self) -> str:
                    return self._from_json('refresh_token')

                @property
                @api_response_property()
                def scope(self) -> str:
                    return self._from_json('scope')

                @property
                @api_response_property()
                def token_type(self) -> str:
                    return self._from_json('token_type')

            api_logger.debug(f'Authenticating to TPP OAuth Application "{client_id}" '
                             f'with scope "{scope}" as "{username}"...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated as {username}!')
            return _Response(response)

    class _Token(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Authorize/Token')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, refresh_token: str, grant_type: str = None, device_code: str = None):
            body = {
                'client_id': client_id,
                'refresh_token': refresh_token,
                'grant_type': grant_type,
                'device_code': device_code
            }

            class _Response(APIResponse):
                def __init__(self, r):
                    super().__init__(response=r)

                @property
                @api_response_property()
                def access_token(self) -> str:
                    return self._from_json('access_token')

                @property
                @api_response_property()
                def expires(self) -> str:
                    return self._from_json('expires')

                @property
                @api_response_property()
                def refresh_token(self) -> str:
                    return self._from_json('refresh_token')

                @property
                @api_response_property()
                def refresh_until(self) -> str:
                    return self._from_json('refresh_until')

                @property
                @api_response_property()
                def scope(self) -> str:
                    return self._from_json('scope')

                @property
                @api_response_property()
                def token_type(self) -> str:
                    return self._from_json('token_type')

            api_logger.debug(f'Authenticating to TPP OAuth application with a refresh token...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated!')
            return _Response(response)

    class _Verify(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Authorize/Verify')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def get(self):
            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def access_issued_on(self):
                    return from_date_string(self._from_json(key='access_issued_on'))

                @property
                @api_response_property()
                def access_issued_on_ISO8601(self):
                    return from_date_string(self._from_json(key='access_issued_on_ISO8601'))

                @property
                @api_response_property()
                def access_issued_on_unix_time(self):
                    return datetime.fromtimestamp(self._from_json(key='access_issued_on_unix_time'))

                @property
                @api_response_property()
                def application(self) -> str:
                    return self._from_json(key='application')

                @property
                @api_response_property()
                def expires(self):
                    return from_date_string(self._from_json(key='expires'))

                @property
                @api_response_property()
                def expires_ISO8601(self):
                    return from_date_string(self._from_json(key='expires_ISO8601'))

                @property
                @api_response_property()
                def expires_unix_time(self):
                    return datetime.fromtimestamp(self._from_json(key='expires_unix_time'))

                @property
                @api_response_property()
                def grant_issued_on(self):
                    return from_date_string(self._from_json(key='grant_issued_on'))

                @property
                @api_response_property()
                def grant_issued_on_ISO8601(self):
                    return from_date_string(self._from_json(key='grant_issued_on_ISO8601'))

                @property
                @api_response_property()
                def grant_issued_on_unix_time(self):
                    return datetime.fromtimestamp(self._from_json(key='grant_issued_on_unix_time'))

                @property
                @api_response_property()
                def identity(self) -> str:
                    return self._from_json(key='identity')

                @property
                @api_response_property()
                def scope(self) -> str:
                    return self._from_json(key='scope')

                @property
                @api_response_property()
                def valid_for(self) -> int:
                    return self._from_json(key='valid_for')

            return _Response(response=self._get())
