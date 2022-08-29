import logging
import warnings
from datetime import datetime
from pytpp.tools.logger import api_logger
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Authorize(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Authorize')

        vedauth_url = self._url.replace('vedsdk', 'vedauth')
        self.Certificate = self._Certificate(api_obj=api_obj, url=f'{vedauth_url}/Certificate')
        self.Device = self._Device(api_obj=api_obj, url=f'{vedauth_url}/Device')
        self.Integrated = self._Integrated(api_obj=api_obj, url=f'{vedauth_url}/Integrated')
        self.OAuth = self._OAuth(api_obj=api_obj, url=f'{vedauth_url}/OAuth')
        self.Token = self._Token(api_obj=api_obj, url=f'{vedauth_url}/Token')
        self.Verify = self._Verify(api_obj=api_obj, url=f'{vedauth_url}/Verify')

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

        class Output(WebSdkOutputModel):
            token: str = ApiField(alias='APIKey')
            valid_until: datetime = ApiField(alias='ValidUntil')

        api_logger.debug(f'Authenticating to TPP as "{username}"...')
        with api_logger.suppressed(logging.WARNING):
            response = self._post(data=body)
        api_logger.debug(f'Authenticated as "{username}"!')
        return generate_output(response=response, output_cls=Output)

    class _Certificate(WebSdkEndpoint):
        def post(self, client_id: str, scope: str):
            body = {
                'client_id': client_id,
                'scope'    : scope
            }

            class Output(WebSdkOutputModel):
                access_token: str = ApiField(alias='access_token')
                expires: datetime = ApiField(alias='expires')
                expires_in: int = ApiField(alias='expires_in')
                identity: str = ApiField(alias='identity')
                refresh_token: str = ApiField(alias='refresh_token')
                refresh_until: datetime = ApiField(alias='refresh_until')
                scope: str = ApiField(alias='scope')
                token_type: str = ApiField(alias='token_type')

            api_logger.debug(f'Authenticating to TPP OAuth Application "{client_id}" '
                             f'with scope "{scope}" using a certificate file...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated!')
            return generate_output(response=response, output_cls=Output)

    class _Device(WebSdkEndpoint):
        def post(self, client_id: str, scope: str):
            body = {
                'client_id': client_id,
                'scope'    : scope
            }

            class Output(WebSdkOutputModel):
                device_code: str = ApiField(alias='device_code')
                interval: int = ApiField(alias='interval')
                user_code: str = ApiField(alias='user_code')
                verification_uri: str = ApiField(alias='verification_uri')
                verification_url_complete: str = ApiField(alias='verification_uri_complete')
                expires_in: int = ApiField(alias='expires_in')
                expires: datetime = ApiField(alias='expires')

            api_logger.debug(f'Authenticating to TPP OAuth Application "{client_id}" '
                             f'with scope "{scope}" using a certificate file...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated!')
            return generate_output(response=response, output_cls=Output)

    class _Integrated(WebSdkEndpoint):
        def post(self, client_id: str, scope: str, state: str = None):
            body = {
                'client_id': client_id,
                'scope'    : scope,
                'state'    : state
            }

            class Output(WebSdkOutputModel):
                access_token: str = ApiField(alias='access_token', default=None)
                expires: datetime = ApiField(alias='expires')
                expires_in: int = ApiField(alias='expires_in')
                identity: str = ApiField(alias='identity')
                refresh_token: str = ApiField(alias='refresh_token')
                refresh_until: datetime = ApiField(alias='refresh_until')
                scope: str = ApiField(alias='scope')
                token_type: str = ApiField(alias='token_type')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _OAuth(WebSdkEndpoint):
        def post(self, client_id: str, password: str, scope: str, username: str, state: str = None):
            body = {
                'client_id': client_id,
                'password' : password,
                'scope'    : scope,
                'username' : username,
                'state'    : state
            }

            class Output(WebSdkOutputModel):
                access_token: str = ApiField(alias='access_token', default=None)
                expires: datetime = ApiField(alias='expires')
                expires_in: int = ApiField(alias='expires_in')
                identity: str = ApiField(alias='identity')
                refresh_token: str = ApiField(alias='refresh_token')
                refresh_until: datetime = ApiField(alias='refresh_until')
                scope: str = ApiField(alias='scope')
                token_type: str = ApiField(alias='token_type')

            api_logger.debug(f'Authenticating to TPP OAuth Application "{client_id}" '
                             f'with scope "{scope}" as "{username}"...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated as {username}!')
            return generate_output(response=response, output_cls=Output)

    class _Token(WebSdkEndpoint):
        def post(self, client_id: str, refresh_token: str, grant_type: str = None, device_code: str = None):
            body = {
                'client_id'    : client_id,
                'refresh_token': refresh_token,
                'grant_type'   : grant_type,
                'device_code'  : device_code
            }

            class Output(WebSdkOutputModel):
                access_token: str = ApiField(alias='access_token')
                expires: datetime = ApiField(alias='expires')
                expires_in: int = ApiField(alias='expires_in')
                refresh_token: str = ApiField(alias='refresh_token')
                refresh_until: datetime = ApiField(alias='refresh_until')
                scope: str = ApiField(alias='scope')
                token_type: str = ApiField(alias='token_type')

            api_logger.debug(f'Authenticating to TPP OAuth application with a refresh token...')
            with api_logger.suppressed(logging.WARNING):
                response = self._post(data=body)
            api_logger.debug(f'Authenticated!')
            return generate_output(response=response, output_cls=Output)

    class _Verify(WebSdkEndpoint):
        def get(self):
            class Output(WebSdkOutputModel):
                access_issued_on_unix_time: datetime = ApiField(alias='access_issued_on_unix_time')
                application: str = ApiField(alias='application')
                expires_unix_time: datetime = ApiField(alias='expires_unix_time')
                grant_issued_on_unix_time: datetime = ApiField(alias='grant_issued_on_unix_time')
                identity: str = ApiField(alias='identity')
                scope: str = ApiField(alias='scope')
                valid_for: int = ApiField(alias='valid_for')

                @property
                def access_issued_on(self):
                    return self.access_issued_on_unix_time

                @property
                def access_issued_on_ISO8601(self):
                    return self.access_issued_on_unix_time

                @property
                def expires(self):
                    return self.expires_unix_time

                @property
                def expires_ISO8601(self):
                    return self.expires_unix_time

                @property
                def grant_issued_on(self):
                    return self.grant_issued_on_unix_time

                @property
                def grant_issued_on_ISO8601(self):
                    return self.grant_issued_on_unix_time

            return generate_output(response=self._get(), output_cls=Output)
