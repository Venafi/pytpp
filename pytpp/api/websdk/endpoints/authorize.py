import warnings
from datetime import datetime
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.tools.helpers.date_converter import from_date_string


class _Authorize(API):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Authorize')

        self.Certificate = self._Certificate(api_obj=api_obj)
        self.Integrated = self._Integrated(api_obj=api_obj)
        self.OAuth = self._OAuth(api_obj=api_obj)
        self.Token = self._Token(api_obj=api_obj)
        self.Verify = self._Verify(api_obj=api_obj)

    def post(self, username, password):
        """
        This POST method is written differently in order to effectively omit the password from being logged.
        """
        self._log_api_deprecated_warning(alternate_api=self.OAuth._url)
        warnings.warn('Authorizing to TPP with only a username and password is being deprecated. '
                      'Refer to product documentation on using OAuth authentication.')
        body = {
            "Username": username,
            "Password": password
        }

        class _Response(APIResponse):
            def __init__(self, response):
                super().__init__(response=response)

            @property
            @api_response_property()
            def token(self) -> str:
                return self._from_json('APIKey')

        return _Response(
            response=self._post(data=body))

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

    class _Integrated(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='Authorize/Integrated')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, password: str, scope: str, username: str, state: str = None):
            body = {
                'client_id': client_id,
                'password' : password,
                'scope'    : scope,
                'username' : username,
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
                def __init__(self, response):
                    super().__init__(response=response)

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

            return _Response(
                response=self._post(data=body))

    class _Token(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/Authorize/Token')
            self._url = self._url.replace('vedsdk', 'vedauth')

        def post(self, client_id: str, refresh_token: str):
            body = {
                'client_id': client_id,
                'refresh_token': refresh_token
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

            return _Response(response=self._post(data=body))

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
