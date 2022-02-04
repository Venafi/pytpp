from typing import List
from pytpp.api.api_base import API, APIResponse, api_response_property
from pytpp.properties.response_objects.ssh_certificates import SSHCertificate
from pytpp.tools.helpers.date_converter import from_date_string


class _SSHCertificates:
    def __init__(self, api_obj):
        self.CAKeyPair = self._CAKeyPair(api_obj=api_obj)
        self.Request = self._Request(api_obj=api_obj)
        self.Retrieve = self._Retrieve(api_obj=api_obj)
        self.Template = self._Template(api_obj=api_obj)

    class _CAKeyPair:
        def __init__(self, api_obj):
            self.Create = self._Create(api_obj=api_obj)
        
        class _Create(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='SSHCertificates/CAKeyPair/Create')
            
            def post(self, name: str, parent_dn: str = None, key_algorithm: str = None,
                     key_storage: str = None, private_key_data: str = None,
                     private_key_passphrase: str = None):
                body = {
                    'Name': name,
                    'ParentDN': parent_dn,
                    'KeyAlgorithm': key_algorithm,
                    'KeyStorage': key_storage,
                    'PrivateKeyData': private_key_data,
                    'PrivateKeyPassphrase': private_key_passphrase
                }
                
                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def created_on(self):
                        return from_date_string(self._from_json(key='CreatedOn'))

                    @property
                    @api_response_property()
                    def dn(self) -> str:
                        return self._from_json(key='DN')

                    @property
                    @api_response_property()
                    def fingerprint_sha_256(self) -> str:
                        return self._from_json(key='FingerprintSHA256')

                    @property
                    @api_response_property()
                    def guid(self) -> str:
                        return self._from_json(key='Guid')

                    @property
                    @api_response_property()
                    def key_algorithm(self) -> str:
                        return self._from_json(key='KeyAlgorithm')

                    @property
                    @api_response_property()
                    def key_storage(self) -> str:
                        return self._from_json(key='KeyStorage')

                    @property
                    @api_response_property()
                    def name(self) -> str:
                        return self._from_json(key='Name')

                    @property
                    @api_response_property()
                    def processing_details(self):
                        return SSHCertificate.ProcessingDetails(self._from_json(key='ProcessingDetails'))

                    @property
                    @api_response_property()
                    def public_key_data(self) -> str:
                        return self._from_json(key='PublicKeyData')

                    @property
                    @api_response_property()
                    def response(self):
                        return SSHCertificate.Response(self._from_json(key='Response'))
                        
                return _Response(response=self._post(data=body))

    class _Request(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSHCertificates/Request')

        def post(self, ca_dn: str,
                 key_id: str,
                 destination_address: str = None,
                 extensions: str = None,
                 force_command: str = None,
                 object_name: str = None,
                 origin: str = None,
                 policy_dn: str = None,
                 principals: List[str] = None,
                 public_key_data: str = None,
                 source_addresses: List[str] = None,
                 validity_period: str = None
                 ):

            body = {
                'CADN': ca_dn,
                'KeyId': key_id,
                'DestinationAddress': destination_address,
                'Extensions': extensions,
                'ForceCommand': force_command,
                'ObjectName': object_name,
                'Origin': origin,
                'PolicyDN': policy_dn,
                'Principals': principals,
                'PublicKeyData': public_key_data,
                'SourceAddresses': source_addresses,
                'ValidityPeriod': validity_period
            }
            

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def ssh_certificate_dn(self) -> str:
                    return self._from_json('DN')

                @property
                @api_response_property()
                def ssh_certificate_guid(self) -> str:
                    return self._from_json('Guid')

                @property
                @api_response_property()
                def response(self) -> SSHCertificate.Response:
                    return SSHCertificate.Response(self._from_json('Response'))

                @property
                @api_response_property()
                def processing_details(self) -> SSHCertificate.ProcessingDetails:
                    return SSHCertificate.ProcessingDetails(self._from_json('ProcessingDetails'))


            return _Response(response=self._post(data=body))

    class _Retrieve(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSHCertificates/Retrieve')

        def post(self, certificate_dn: str = None,
                 certificate_guid: str = None,
                 include_certificate_details: bool = None,
                 include_private_key_data: bool = None,
                 private_key_passphrase: str = None):

            body = {
                'DN': certificate_dn,
                'Guid': certificate_guid,
                'IncludeCertificateDetails': include_certificate_details,
                'IncludePrivateKeyData': include_private_key_data,
                'PrivateKeyPassphrase': private_key_passphrase
            }

            class _Response(APIResponse):
                def __init__(self, response):
                    super().__init__(response=response)

                @property
                @api_response_property()
                def ca_dn(self) -> str:
                    return self._from_json('CADN')

                @property
                @api_response_property()
                def ca_guid(self) -> str:
                    return self._from_json('CAGuid')

                @property
                @api_response_property()
                def certificate_data(self) -> str:
                    return self._from_json('CertificateData')

                @property
                @api_response_property()
                def certificate_details(self) -> SSHCertificate.CertificateDetails:
                    return SSHCertificate.CertificateDetails(self._from_json('CertificateDetails'))

                @property
                @api_response_property()
                def guid(self) -> str:
                    return self._from_json('Guid')

                @property
                @api_response_property()
                def key_id(self) -> str:
                    return self._from_json('KeyID')

                @property
                @api_response_property()
                def private_key_data(self) -> str:
                    return self._from_json('PrivateKeyData')

                @property
                @api_response_property()
                def processing_details(self) -> SSHCertificate.ProcessingDetails:
                    return SSHCertificate.ProcessingDetails(self._from_json('ProcessingDetails'))

                @property
                @api_response_property()
                def public_key_data(self) -> str:
                    return self._from_json('PublicKeyData')

                @property
                @api_response_property()
                def request_details(self) -> SSHCertificate.RequestDetails:
                    return SSHCertificate.RequestDetails(self._from_json('RequestDetails'))

                @property
                @api_response_property()
                def response(self):
                    return SSHCertificate.Response(self._from_json('Response'))

            return _Response(response=self._post(data=body))

    class _Template(API):
        def __init__(self, api_obj):
            super().__init__(api_obj=api_obj, url='/SSHCertificates/Template')
            self.Retrieve = self._Retrieve(api_obj=api_obj)

        class _Retrieve(API):
            def __init__(self, api_obj):
                super().__init__(api_obj=api_obj, url='/SSHCertificates/Template/Retrieve')
                self.PublicKeyData = self._PublicKeyData(api_obj=api_obj)

            def post(self, template_dn: str = None, template_guid: str = None, include_ca_keypair_details: bool = None):
                body = {
                    'DN': template_dn,
                    'Guid'  : template_guid,
                    'IncludeCAKeyPairDetails' : include_ca_keypair_details
                }

                class _Response(APIResponse):
                    def __init__(self, response):
                        super().__init__(response=response)

                    @property
                    @api_response_property()
                    def access_control(self) -> dict:
                        return self._from_json('AccessControl')

                    @property
                    @api_response_property()
                    def api_client(self) -> SSHCertificate.APIClient:
                        return SSHCertificate.APIClient(self._from_json('APIClient'))

                    @property
                    @api_response_property()
                    def ca_keypair_guid(self) -> str:
                        return self._from_json('CAKeyPairGuid')

                    @property
                    @api_response_property()
                    def ca_keypair_dn(self) -> str:
                        return self._from_json('CAKeyPairDN')

                    @property
                    @api_response_property()
                    def ca_keypair(self) -> SSHCertificate.CAKeyPair:
                        return SSHCertificate.CAKeyPair(self._from_json('CAKeyPair'))

                    @property
                    @api_response_property()
                    def certificate(self) -> SSHCertificate.Certificate:
                        return SSHCertificate.Certificate(self._from_json('Certificate'))

                    @property
                    @api_response_property()
                    def contacts(self) -> List[str]:
                        return self._from_json('Contacts')

                    @property
                    @api_response_property()
                    def created_on(self) -> str:
                        return self._from_json('CreatedOn')

                    @property
                    @api_response_property()
                    def guid(self) -> str:
                        return self._from_json('Guid')

                    @property
                    @api_response_property()
                    def name(self) -> str:
                        return self._from_json('Name')

                    @property
                    @api_response_property()
                    def response(self):
                        return SSHCertificate.Response(self._from_json('Response'))

                return _Response(response=self._post(data=body))

            class _PublicKeyData(API):
                def __init__(self, api_obj):
                    super().__init__(api_obj=api_obj, url='SSHCertificates/Template/Retrieve/PublicKeyData')

                def get(self, template_dn: str = None, template_guid: str = None):
                    params = {
                        'DN'  : template_dn,
                        'Guid': template_guid,
                    }

                    class _Response(APIResponse):
                        def __init__(self, response):
                            super().__init__(response=response)

                        @property
                        def response(self) -> str:
                            return self.response

                    return _Response(response=self._get(params=params))
