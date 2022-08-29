from datetime import datetime
from typing import List, Union
from pytpp.api.websdk.models import certificate
from pytpp.api.api_base import ObjectModel, WebSdkEndpoint, WebSdkOutputModel, generate_output, ApiField


class _Certificates(WebSdkEndpoint):
    def __init__(self, api_obj):
        super().__init__(api_obj=api_obj, url='/Certificates')
        self.Associate = self._Associate(api_obj=api_obj, url=f'{self._url}/Associate')
        self.CheckPolicy = self._CheckPolicy(api_obj=api_obj, url=f'{self._url}/CheckPolicy')
        self.Dissociate = self._Dissociate(api_obj=api_obj, url=f'{self._url}/Dissociate')
        self.Import = self._Import(api_obj=api_obj, url=f'{self._url}/Import')
        self.Push = self._Push(api_obj=api_obj, url=f'{self._url}/Push')
        self.Renew = self._Renew(api_obj=api_obj, url=f'{self._url}/Renew')
        self.Request = self._Request(api_obj=api_obj, url=f'{self._url}/Request')
        self.Reset = self._Reset(api_obj=api_obj, url=f'{self._url}/Reset')
        self.Retrieve = self._Retrieve(api_obj=api_obj, url=f'{self._url}/Retrieve')
        self.Retry = self._Retry(api_obj=api_obj, url=f'{self._url}/Retry')
        self.Revoke = self._Revoke(api_obj=api_obj, url=f'{self._url}/Revoke')
        self.Validate = self._Validate(api_obj=api_obj, url=f'{self._url}/Validate')

    def Guid(self, guid):
        return self._Guid(api_obj=self._api_obj, url=f'{self._url}/{guid}')

    def get(self, limit: int = None, offset: int = None, optional_fields: List[str] = None,
            filters: Union[dict, certificate.CertificateFilter] = None):
        params = {
            'Limit'         : limit,
            'Offset'        : offset,
            'OptionalFields': optional_fields
        }
        if isinstance(filters, dict):
            params.update(filters)
        elif isinstance(filters, ObjectModel):
            params.update(filters.dict(by_alias=True, exclude_none=True))

        class Output(WebSdkOutputModel):
            links: List[certificate.Link] = ApiField(default_factory=list, alias='_links')
            x_record_count: int = ApiField(alias='X-Record-Count')
            certificates: List[certificate.Certificate] = ApiField(default_factory=list, alias='Certificates')
            data_range: str = ApiField(alias='DataRange')
            total_count: int = ApiField(alias='TotalCount')

        return generate_output(response=self._get(params=params), output_cls=Output)

    def head(self, filters: Union[dict, certificate.CertificateFilter] = None):
        params = filters

        class Output(WebSdkOutputModel):
            @property
            def x_record_count(self):
                xrc = int(self.api_response.headers.get('X-Record-Count'))
                return xrc

        return generate_output(response=self._get(params=params), output_cls=Output)

    class _Associate(WebSdkEndpoint):
        def post(self, application_dn: str, certificate_dn: str, push_to_new: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'ApplicationDN': application_dn,
                'PushToNew'    : push_to_new
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _CheckPolicy(WebSdkEndpoint):
        def post(self, policy_dn: str, pkcs10: str = None):
            body = {
                'PolicyDN': policy_dn,
                'PKSC10'  : pkcs10
            }

            class Output(WebSdkOutputModel):
                csr: certificate.CSR = ApiField(alias='CSR')
                policy: certificate.Policy = ApiField(alias='Policy')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Dissociate(WebSdkEndpoint):
        def post(self, certificate_dn: str, application_dn: List[str], delete_orphans: bool = False):
            body = {
                'CertificateDN': certificate_dn,
                'ApplicationDN': application_dn,
                'DeleteOrphans': delete_orphans
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Guid(WebSdkEndpoint):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.PreviousVersions = self._PreviousVersions(api_obj=self._api_obj, url=f'{self._url}/PreviousVersions')
            self.ValidationResults = self._ValidationResults(api_obj=self._api_obj, url=f'{self._url}/ValidationResults')

        def delete(self):
            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._delete(), output_cls=Output)

        def get(self):
            class Output(WebSdkOutputModel):
                approver: List[str] = ApiField(default_factory=list, alias='Approver')
                certificate_authority_dn: datetime = ApiField(alias='CertificateAuthorityDN')
                certificate_details: certificate.CertificateDetails = ApiField(alias='CertificateDetails')
                consumers: List[str] = ApiField(alias='Consumers', default_factory=list)
                contact: List[str] = ApiField(default_factory=list, alias='Contact')
                created_by: str = ApiField(alias='CreatedBy')
                created_on: datetime = ApiField(alias='CreatedOn')
                custom_fields: List[certificate.NameTypeValue] = ApiField(default_factory=list, alias='CustomFields')
                disabled: bool = ApiField(alias='Disabled')
                dn: str = ApiField(alias='DN')
                guid: str = ApiField(alias='Guid')
                management_type: str = ApiField(alias='ManagementType')
                name: str = ApiField(alias='Name')
                parent_dn: str = ApiField(alias='ParentDN')
                processing_details: certificate.ProcessingDetails = ApiField(alias='ProcessingDetails')
                renewal_details: certificate.RenewalDetails = ApiField(alias='RenewalDetails')
                schema_class: str = ApiField(alias='SchemaClass')
                success: str = ApiField(alias='Success')
                validation_details: certificate.ValidationDetails = ApiField(alias='ValidationDetails')

            return generate_output(response=self._get(), output_cls=Output)

        def put(self, attribute_data: List[dict]):
            body = {
                "AttributeData": attribute_data
            }

            class Output(WebSdkOutputModel):
                success: str = ApiField(alias='Success')

            return generate_output(response=self._put(data=body), output_cls=Output)

        class _PreviousVersions(WebSdkEndpoint):
            def get(self, exclude_expired: bool = False, exclude_revoked: bool = False):
                params = {
                    'ExcludeExpired': exclude_expired,
                    'ExcludeRevoked': exclude_revoked
                }

                class Output(WebSdkOutputModel):
                    success: str = ApiField(default='', alias='Success')
                    previous_versions: List[certificate.PreviousVersions] = ApiField(
                        default_factory=list, alias='PreviousVersions'
                    )

                return generate_output(response=self._get(params=params), output_cls=Output)

        class _ValidationResults(WebSdkEndpoint):
            def get(self):
                class Output(WebSdkOutputModel):
                    file: List[certificate.File] = ApiField(default_factory=list, alias='File')
                    ssl_tls: List[certificate.SslTls] = ApiField(default_factory=list, alias='SslTls')

                return generate_output(response=self._get(), output_cls=Output)

    class _Import(WebSdkEndpoint):
        def post(self, certificate_data: str, policy_dn: str, ca_specific_attributes: List[certificate.NameValue] = None,
                 object_name: str = None,
                 password: str = None, private_key_data: str = None, reconcile: bool = False):
            body = {
                'CertificateData'     : certificate_data,
                'PolicyDN'            : policy_dn,
                'CASpecificAttributes': ca_specific_attributes,
                'ObjectName'          : object_name,
                'Password'            : password,
                'PrivateKeyData'      : private_key_data,
                'Reconcile'           : reconcile
            }

            class Output(WebSdkOutputModel):
                certificate_dn: str = ApiField(alias='CertificateDN')
                certificate_vault_id: int = ApiField(alias='CertificateVaultID')
                guid: str = ApiField(alias='Guid')
                private_key_vault_id: int = ApiField(alias='PrivateKeyVaultID')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Push(WebSdkEndpoint):
        def post(self, certificate_dn: str, application_dn: List[str] = None, push_to_all: bool = False):
            body = {
                'ApplicationDN': application_dn,
                'CertificateDN': certificate_dn,
                'PushToAll'    : push_to_all
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Renew(WebSdkEndpoint):
        # noinspection ALL
        def post(self, certificate_dn: str, pkcs10: str = None, reenable: bool = False, format: certificate.CertificateFormat = None,
                 password: str = None, include_private_key: bool = None, include_chain: bool = None,
                 friendly_name: str = None, root_first_order: bool = None, keystore_password: str = None,
                 work_to_do_timeout: int = None):
            body = {
                'CertificateDN'    : certificate_dn,
                'PKCS10'           : pkcs10,
                'Reenable'         : reenable,
                'Format'           : format,
                'Password'         : password,
                'IncludePrivateKey': include_private_key,
                'IncludeChain'     : include_chain,
                'FriendlyName'     : friendly_name,
                'RootFirstOrder'   : root_first_order,
                'KeystorePassword' : keystore_password,
                'WorkToDoTimeout'  : work_to_do_timeout
            }

            class Output(WebSdkOutputModel):
                certificate_data: str = ApiField(alias='CertificateData')
                certificate_dn: str = ApiField(alias='CertificateDN')
                filename: str = ApiField(alias='Filename')
                format: certificate.CertificateFormat = ApiField(alias='Format')
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Request(WebSdkEndpoint):
        def post(self, policy_dn: str, approvers: List[dict] = None, cadn: str = None,
                 ca_specific_attributes: List[dict] = None, certificate_type: str = None, city: str = None,
                 contacts: List[dict] = None, country: str = None, custom_fields: List[dict] = None, created_by: str = None,
                 devices: List[dict] = None, disable_automatic_renewal: bool = False, elliptic_curve: str = None,
                 format: certificate.CertificateFormat = None, friendly_name: str = None, include_private_key: bool = False,
                 include_chain: bool = None, key_algorithm: str = None, key_bit_size: int = None, keystore_password: str = None,
                 management_type: str = None, password: str = None, object_name: str = None,
                 organization: str = None, organizational_unit: str = None, origin: str = None, pkcs10: str = None,
                 reenable: bool = False, root_first_order: bool = None, set_work_todo: bool = True, state: str = None,
                 subject: str = None, subject_alt_names: List[dict] = None, work_to_do_timeout: int = None):
            body = {
                'Approvers'              : approvers,
                'CADN'                   : cadn,
                'CASpecificAttributes'   : ca_specific_attributes,
                'CertificateType'        : certificate_type,
                'City'                   : city,
                'Contacts'               : contacts,
                'Country'                : country,
                'CustomFields'           : custom_fields,
                'CreatedBy'              : created_by,
                'Devices'                : devices,
                'DisableAutomaticRenewal': disable_automatic_renewal,
                'EllipticCurve'          : elliptic_curve,
                'Format'                 : format,
                'FriendlyName'           : friendly_name,
                'IncludePrivateKey'      : include_private_key,
                'IncludeChain'           : include_chain,
                'KeystorePassword'       : keystore_password,
                'KeyAlgorithm'           : key_algorithm,
                'KeyBitSize'             : key_bit_size,
                'ManagementType'         : management_type,
                'ObjectName'             : object_name,
                'Origin'                 : origin,
                'Organization'           : organization,
                'OrganizationalUnit'     : organizational_unit,
                'Password'               : password,
                'PKCS10'                 : pkcs10,
                'PolicyDN'               : policy_dn,
                'Reenable'               : reenable,
                'RootFirstOrder'         : root_first_order,
                'SetWorkToDo'            : set_work_todo,
                'State'                  : state,
                'Subject'                : subject,
                'SubjectAltNames'        : subject_alt_names,
                'WorkToDoTimeout'        : work_to_do_timeout
            }

            class Output(WebSdkOutputModel):
                certificate_data: str = ApiField(alias='CertificateData')
                filename: str = ApiField(alias='Filename')
                format: certificate.CertificateFormat = ApiField(alias='Format')
                certificate_dn: str = ApiField(alias='CertificateDN')
                guid: str = ApiField(alias='Guid')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Reset(WebSdkEndpoint):
        def post(self, certificate_dn: str, restart: bool = False, work_to_do_timeout: int = None):
            body = {
                'CertificateDN'  : certificate_dn,
                'Restart'        : restart,
                'WorkToDoTimeout': work_to_do_timeout
            }

            class Output(WebSdkOutputModel):
                private_key_mismatch_reset_completed: bool = ApiField(alias='PrivateKeyMismatchResetCompleted')
                processing_reset_completed: bool = ApiField(alias='ProcessingResetCompleted')
                restart_completed: bool = ApiField(alias='RestartCompleted')
                revocation_reset_completed: bool = ApiField(alias='RevocationResetCompleted')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Retrieve(WebSdkEndpoint):
        # noinspection ALL
        def get(self, certificate_dn: str, format: certificate.CertificateFormat, friendly_name: str, include_chain: bool = False,
                include_private_key: bool = False, keystore_password: str = None, password: str = None,
                root_first_order: bool = False, work_to_do_timeout: int = None):
            params = {
                'CertificateDN'    : certificate_dn,
                'Format'           : format,
                'FriendlyName'     : friendly_name,
                'IncludeChain'     : include_chain,
                'IncludePrivateKey': include_private_key,
                'KeystorePassword' : keystore_password,
                'Password'         : password,
                'RootFirstOrder'   : root_first_order,
                'WorkToDoTimeout'  : work_to_do_timeout
            }

            return generate_output(response=self._get(params=params), output_cls=WebSdkOutputModel)

        def post(self, certificate_dn: str, format: certificate.CertificateFormat, friendly_name: str, include_chain: bool = False,
                 include_private_key: bool = False, keystore_password: str = None, password: str = None,
                 root_first_order: bool = False, work_to_do_timeout: int = None):
            body = {
                'CertificateDN'    : certificate_dn,
                'Format'           : format,
                'FriendlyName'     : friendly_name,
                'IncludeChain'     : include_chain,
                'IncludePrivateKey': include_private_key,
                'KeystorePassword' : keystore_password,
                'Password'         : password,
                'RootFirstOrder'   : root_first_order,
                'WorkToDoTimeout'  : work_to_do_timeout
            }

            class Output(WebSdkOutputModel):
                certificate_data: str = ApiField(alias='CertificateData')
                filename: str = ApiField(alias='Filename')
                format: certificate.CertificateFormat = ApiField(alias='Format')

            return generate_output(response=self._post(data=body), output_cls=Output)

        def VaultId(self, vault_id: int):
            return self._VaultId(api_obj=self._api_obj, url=f'{self._url}/{vault_id}')

        class _VaultId(WebSdkEndpoint):
            # noinspection ALL
            def get(self, format: certificate.CertificateFormat, friendly_name: str, include_chain: bool = False,
                    include_private_key: bool = False, keystore_password: str = None, password: str = None,
                    root_first_order: bool = False):
                params = {
                    'Format'           : format,
                    'FriendlyName'     : friendly_name,
                    'IncludeChain'     : include_chain,
                    'IncludePrivateKey': include_private_key,
                    'KeystorePassword' : keystore_password,
                    'Password'         : password,
                    'RootFirstOrder'   : root_first_order
                }

                return generate_output(response=self._get(params=params), output_cls=WebSdkOutputModel)

            # noinspection ALL
            def post(self, format: certificate.CertificateFormat, friendly_name: str, include_chain: bool = False,
                     include_private_key: bool = False, keystore_password: str = None, password: str = None,
                     root_first_order: bool = False):
                body = {
                    'Format'           : format,
                    'FriendlyName'     : friendly_name,
                    'IncludeChain'     : include_chain,
                    'IncludePrivateKey': include_private_key,
                    'KeystorePassword' : keystore_password,
                    'Password'         : password,
                    'RootFirstOrder'   : root_first_order
                }

                class Output(WebSdkOutputModel):
                    certificate_data: str = ApiField(alias='CertificateData')
                    filename: str = ApiField(alias='Filename')
                    format: certificate.CertificateFormat = ApiField(alias='Format')

                return generate_output(response=self._post(data=body), output_cls=Output)

    class _Retry(WebSdkEndpoint):
        def post(self, certificate_dn: str, work_to_do_timeout: int = None):
            body = {
                'CertificateDN'  : certificate_dn,
                'WorkToDoTimeout': work_to_do_timeout
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Revoke(WebSdkEndpoint):
        def post(self, certificate_dn: str = None, thumbprint: str = None, reason: int = None, comments: str = None,
                 disable: bool = None, work_to_do_timeout: int = None):
            body = {
                'CertificateDN'  : certificate_dn,
                'Thumbprint'     : thumbprint,
                'Reason'         : reason,
                'Comments'       : comments,
                'Disable'        : disable,
                'WorkToDoTimeout': work_to_do_timeout
            }

            class Output(WebSdkOutputModel):
                requested: bool = ApiField(alias='Requested')
                success: bool = ApiField(alias='Success')

            return generate_output(response=self._post(data=body), output_cls=Output)

    class _Validate(WebSdkEndpoint):
        def post(self, certificate_dns: List[str] = None, certificate_guids: List[str] = None):
            body = {
                'CertificateDNs'  : certificate_dns,
                'CertificateGUIDs': certificate_guids
            }

            class Output(WebSdkOutputModel):
                success: bool = ApiField(alias='Success')
                validated_certificate_dns: List[str] = ApiField(default_factory=list, alias='ValidatedCertificateDNs')
                validated_certificate_guids: List[str] = ApiField(default_factory=list, alias='ValidatedCertificateGUIDs')
                warnings: List[str] = ApiField(default_factory=list, alias='Warnings')

            return generate_output(response=self._post(data=body), output_cls=Output)
