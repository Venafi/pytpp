from typing import List, Union
from pytpp.api.websdk.models import pki
from pytpp.api.api_base import WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _PKI(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/PKI')
        self.HashiCorp = self._HashiCorp(api_obj=api_obj, url=f'{self._url}/HashiCorp')

    class _HashiCorp(WebSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.CA = self._CA(api_obj=self._api_obj, url=f'{self._url}/CA')
            self.Role = self._Role(api_obj=self._api_obj, url=f'{self._url}/Role')

        class _CA(WebSdkEndpoint):
            def Guid(self, guid: str):
                return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

            def get(self):
                class Output(WebSdkOutputModel):
                    pkis: List[pki.PKI] = ApiField(default_factory=list, alias='pkis')

                return generate_output(output_cls=Output, response=self._get())

            def post(self, certificate: Union[dict, pki.Certificate], folder_dn: str, pki_path: str, roles: List[str],
                     create_certificate_authority: bool = True, create_pki_role: bool = False, crl_address: str = None,
                     installation: Union[dict, pki.Installation] = None, key_algorithm: str = None, key_bit_size: str = None,
                     ocsp_address: str = None):
                body = {
                    'Certificate'               : certificate,
                    'CreateCertificateAuthority': create_certificate_authority,
                    'CreatePKIRole'             : create_pki_role,
                    'CRLAddress'                : crl_address,
                    'FolderDn'                  : folder_dn,
                    'Installation'              : installation,
                    'KeyAlgorithm'              : key_algorithm,
                    'KeyBitSize'                : key_bit_size,
                    'OCSPAddress'               : ocsp_address,
                    'PkiPath'                   : pki_path,
                    'Roles'                     : roles
                }

                class Output(WebSdkOutputModel):
                    certificate_dn: str = ApiField(alias='CertificateDN')
                    certificate_guid: str = ApiField(alias='CertificateGuid')
                    guid: str = ApiField(alias='Guid')

                return generate_output(output_cls=Output, response=self._post(data=body))

            class _Guid(WebSdkEndpoint):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
                    self.Renew = self._Renew(api_obj=self._api_obj, url=f'{self._url}/Renew')

                def delete(self):
                    class Output(WebSdkOutputModel):
                        certificate_dn: str = ApiField(alias='CertificateDN')
                        certificate_guid: str = ApiField(alias='CertificateGuid')
                        guid: str = ApiField(alias='Guid')

                    return generate_output(output_cls=Output, response=self._delete())

                def get(self):
                    class Output(WebSdkOutputModel):
                        certificate: pki.Certificate = ApiField(alias='Certificate')
                        create_certificate_authority: bool = ApiField(alias='CreateCertificateAuthority')
                        create_pki_role: bool = ApiField(alias='CreatePKIRole')
                        folder_dn: str = ApiField(alias='FolderDn')
                        installation: pki.Installation = ApiField(alias='Installation')
                        pki_path: str = ApiField(alias='PkiPath')
                        roles: List[str] = ApiField(alias='Roles', default_factory=list)

                    return generate_output(output_cls=Output, response=self._get())

                def post(self):
                    class Output(WebSdkOutputModel):
                        certificate_dn: str = ApiField(alias='CertificateDN')
                        certificate_guid: str = ApiField(alias='CertificateGuid')
                        guid: str = ApiField(alias='Guid')

                    return generate_output(output_cls=Output, response=self._post(data={}))

                def put(self, folder_dn: str, pki_path: str, roles: List[str], certificate: Union[dict, pki.Certificate] = None,
                        create_certificate_authority: bool = True, create_pki_role: bool = False, crl_address: str = None,
                        installation: Union[dict, pki.Installation] = None, key_algorithm: str = None,
                        key_bit_size: str = None, ocsp_address: str = None):
                    body = {
                        'Certificate'               : certificate,
                        'CreateCertificateAuthority': create_certificate_authority,
                        'CreatePKIRole'             : create_pki_role,
                        'CRLAddress'                : crl_address,
                        'FolderDn'                  : folder_dn,
                        'Installation'              : installation,
                        'KeyAlgorithm'              : key_algorithm,
                        'KeyBitSize'                : key_bit_size,
                        'OCSPAddress'               : ocsp_address,
                        'PkiPath'                   : pki_path,
                        'Roles'                     : roles
                    }

                    class Output(WebSdkOutputModel):
                        certificate_dn: str = ApiField(alias='CertificateDN')
                        certificate_guid: str = ApiField(alias='CertificateGuid')
                        guid: str = ApiField(alias='Guid')

                    return generate_output(output_cls=Output, response=self._put(data=body))

                class _Renew(WebSdkEndpoint):
                    def post(self):
                        class Output(WebSdkOutputModel):
                            certificate_dn: str = ApiField(alias='CertificateDN')
                            certificate_guid: str = ApiField(alias='CertificateGuid')
                            guid: str = ApiField(alias='Guid')

                        return generate_output(output_cls=Output, response=self._post(data={}))

        class _Role(WebSdkEndpoint):
            def post(self, folder_dn: str, role_name: str, city: str = None, country: str = None,
                     enhanced_key_usage: List[str] = None, key_algorithm: str = None, key_bit_size: str = None,
                     organization: str = None, organizational_units: List[str] = None, state: str = None,
                     whitelisted_domains: List[str] = None):
                body = {
                    'City'               : city,
                    'Country'            : country,
                    'EnhancedKeyUsage'   : enhanced_key_usage,
                    'FolderDn'           : folder_dn,
                    'KeyAlgorithm'       : key_algorithm,
                    'KeyBitSize'         : key_bit_size,
                    'Organization'       : organization,
                    'OrganizationalUnits': organizational_units,
                    'RoleName'           : role_name,
                    'State'              : state,
                    'WhitelistedDomains' : whitelisted_domains
                }

                class Output(WebSdkOutputModel):
                    guid: str = ApiField(alias='Guid')

                return generate_output(output_cls=Output, response=self._post(data=body))

            def Guid(self, guid: str):
                return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

            class _Guid(WebSdkEndpoint):
                def delete(self):
                    class Output(WebSdkOutputModel):
                        guid: str = ApiField(alias='Guid')

                    return generate_output(output_cls=Output, response=self._delete())

                def get(self):
                    class Output(WebSdkOutputModel):
                        city: str = ApiField(alias='City')
                        country: str = ApiField(alias='Country')
                        enhanced_key_usage: str = ApiField(alias='EnhancedKeyUsage')
                        folder_dn: str = ApiField(alias='FolderDn')
                        guid: str = ApiField(alias='Guid')
                        key_algorithm: str = ApiField(alias='KeyAlgorithm')
                        key_bit_size: str = ApiField(alias='KeyBitSize')
                        organization: str = ApiField(alias='Organization')
                        organizational_units: List[str] = ApiField(default_factory=list, alias='OrganizationalUnits')
                        role_name: str = ApiField(alias='RoleName')
                        state: str = ApiField(alias='State')
                        whitelisted_domains: List[str] = ApiField(default_factory=list, alias='WhitelistedDomains')

                    return generate_output(output_cls=Output, response=self._get())

                def put(self, city: str = None, country: str = None,
                        enhanced_key_usage: List[str] = None, key_algorithm: str = None, key_bit_size: str = None,
                        organization: str = None, organizational_units: List[str] = None, state: str = None,
                        whitelisted_domains: List[str] = None):
                    body = {
                        'City'               : city,
                        'Country'            : country,
                        'EnhancedKeyUsage'   : enhanced_key_usage,
                        'KeyAlgorithm'       : key_algorithm,
                        'KeyBitSize'         : key_bit_size,
                        'Organization'       : organization,
                        'OrganizationalUnits': organizational_units,
                        'State'              : state,
                        'WhitelistedDomains' : whitelisted_domains
                    }

                    class Output(WebSdkOutputModel):
                        guid: str = ApiField(alias='Guid')

                    return generate_output(output_cls=Output, response=self._put(data=body))
