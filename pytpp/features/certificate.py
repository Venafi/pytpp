from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING
if TYPE_CHECKING:
    from pytpp.tools.vtypes import Config, Identity
from pytpp.attributes.x509_certificate import X509CertificateAttributes
from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.features.definitions.exceptions import FeatureException, UnexpectedValue
from pytpp.features.definitions.classes import Classes
from pytpp.tools.logger import logger, LogTags


@dataclass
class DownloadedCertificate:
    certificate_data: str
    filename: str
    format: str


@feature('Certificate')
class Certificate(FeatureBase):
    def __init__(self, api):
        super().__init__(api)

    def _get(self, certificate: 'Union[Config.Object, str]'):
        # High volume concurrency can cause a 500 internal error in IIS due to a deadlock.
        # In this case the error requests the client to "rerun the transaction".
        certificate_guid = self._get_guid(certificate)

        retries = 3
        result = self._api.websdk.Certificates.Guid(certificate_guid).get()
        for retry in range(retries):
            if 'Rerun the transaction' not in result.api_response.reason:
                result.assert_valid_response()
                return result
            logger.log('Rerunning Certificates/Get transaction due to deadlock...', log_tag=LogTags.feature)
            result = self._api.websdk.Certificates.Guid(certificate_guid).get()
        # It's likely at this point that we failed to get the certificate. Let the result.assert_valid_response()
        # handle the errors. In some unknown case where the response is valid, return it just in case.
        result.assert_valid_response()
        return result

    def associate_application(self, certificate: 'Union[Config.Object, str]', applications: 'List[Union[Config.Object, str]]',
                              push_to_new: bool = False):
        """
        Associates an application object to a certificate object.

        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.
            applications: A list of :ref:`config_object` or :ref:`dn` for each application object.
            push_to_new: If ``True``, the certificate will be pushed to the application once associated.
        """
        certificate_dn = self._get_dn(certificate)
        result = self._api.websdk.Certificates.Associate.post(
            application_dn=[self._get_dn(a) for a in applications],
            certificate_dn=certificate_dn,
            push_to_new=push_to_new
        )
        if not result.success:
            raise FeatureException(f'Unable to associate the given applications to the certificate "{certificate_dn}".')

    def create(self, name: str, parent_folder: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None, approvers: 'List[Union[Identity.Identity, str]]' = None,
               management_type: 'str' = None, service_generated_csr: 'bool' = None, generate_key_on_application: 'bool' = None,
               hash_algorithm: 'str' = None, common_name: 'str' = None, organization: 'str' = None, organization_unit: 'List[str]' = None,
               city: 'str' = None, state: 'str' = None, country: 'str' = None, san_dns: 'List[str]' = None, san_email: 'List[str]' = None,
               san_upn: 'List[str]' = None, san_ip: 'List[str]' = None, san_uri: 'List[str]' = None, key_algorithm: 'str' = None,
               key_strength: 'int' = None, elliptic_curve: 'str' = None, ca_template: 'Union[Config.Object, str]' = None,
               disable_automatic_renewal: 'bool' = None, renewal_window: 'int' = None, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        .. note::
            The certificate is not automatically requested. Use :meth:`renew` to obtain a certificate.

        Args:
            name: Name of the Certificate object.
            parent_folder: :ref:`config_object` or :ref:`dn` of the parent folder.
            description: Description of the certificate object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` of the contacts for this certificate.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` of the approvers for this certificate.
            management_type: Certificate management type.
            service_generated_csr: If ``True``, TPP generates the CSR.
            generate_key_on_application: If ``True``, the key/CSR are generated on the target application.
            hash_algorithm: Hash algorithm.
            common_name: Common name (CN) of the certificate.
            organization: Organization of the certificate.
            organization_unit: Organization units (OU) of the certificate.
            city: City.
            state: State.
            country: Country code.
            san_dns: List of Subject Alternative Names for DNS.
            san_email: List of Subject Alternative Names for e-mail addresses.
            san_upn: List of Subject Alternative Names for UPN.
            san_ip: List of Subject Alternative Names for IP addresses.
            san_uri: List of Subject Alternative Names for URI.
            key_algorithm: Signing key algorithm.
            key_strength: Key strength in bits.
            elliptic_curve: Elliptic curve.
            ca_template: :ref:`config_object` or :ref:`dn` of the Certificate Authority template.
            disable_automatic_renewal: If ``True``, disables automatic renewal.
            renewal_window: Number of days that make the renewal window.
            attributes: Additional attributes that define this certificate.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object`
        """
        cert_attrs = {
            X509CertificateAttributes.description: description,
            X509CertificateAttributes.contact: [self._get_prefixed_universal(c) for c in contacts] if contacts else None,
            X509CertificateAttributes.approver: [self._get_prefixed_universal(a) for a in approvers] if approvers else None,
            X509CertificateAttributes.management_type: management_type,
            X509CertificateAttributes.manual_csr: {True: "0", False: "1"}.get(service_generated_csr),
            X509CertificateAttributes.generate_keypair_on_application: {True: "1", False: "0"}.get(generate_key_on_application),
            X509CertificateAttributes.pkcs10_hash_algorithm: hash_algorithm,
            X509CertificateAttributes.x509_subject: common_name,
            X509CertificateAttributes.organization: organization,
            X509CertificateAttributes.organizational_unit: organization_unit,
            X509CertificateAttributes.city: city,
            X509CertificateAttributes.state: state,
            X509CertificateAttributes.country: country,
            X509CertificateAttributes.driver_name: 'appx509certificate',
            X509CertificateAttributes.x509_subjectaltname_dns: san_dns,
            X509CertificateAttributes.x509_subjectaltname_ipaddress: san_ip,
            X509CertificateAttributes.x509_subjectaltname_uri: san_uri,
            X509CertificateAttributes.x509_subjectaltname_othername_upn: san_upn,
            X509CertificateAttributes.x509_subjectaltname_rfc822: san_email,
            X509CertificateAttributes.key_algorithm: key_algorithm,
            X509CertificateAttributes.key_bit_strength: key_strength,
            X509CertificateAttributes.elliptic_curve: elliptic_curve,
            X509CertificateAttributes.certificate_authority: self._get_dn(ca_template) if ca_template else None,
            X509CertificateAttributes.disable_automatic_renewal: {True: "1", False: "0"}.get(disable_automatic_renewal),
            X509CertificateAttributes.renewal_window: renewal_window
        }
        if attributes:
            cert_attrs.update(attributes)
        return self._config_create(
            name=name,
            parent_folder_dn=self._get_dn(parent_folder),
            config_class=Classes.x509_certificate,
            attributes=cert_attrs,
            get_if_already_exists=get_if_already_exists
        )

    def delete(self, certificate: 'Union[Config.Object, str]'):
        """
        Deletes the certificate object from TPP.

        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.
        """
        certificate_guid = self._get_guid(certificate)
        result = self._api.websdk.Certificates.Guid(certificate_guid).delete()
        if not result.is_valid_response():
            certificate_dn = self._get_dn(certificate)
            raise FeatureException(f'Could not delete certificate {certificate_dn}.')

    def details(self, certificate: 'Union[Config.Object, str]'):
        """
        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.

        Returns:
            :class:`~.dataclasses.certificate.CertificateDetails`
        """
        return self._get(certificate=certificate).certificate_details

    def dissociate_application(self, certificate: 'Union[Config.Object, str]', applications: 'List[Union[Config.Object, str]]',
                               delete_orphans: bool = False):
        """
        Dissociate an application object from a certificate.

        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.
            applications: A list of :ref:`config_object` or :ref:`dn` to each application object.
            delete_orphans: Delete the application object. The corresponding device object will be delete if it has no
                            child applications. Use this option to completely remove the application object and corresponding
                            device objects.
        """
        certificate_dn = self._get_dn(certificate)
        result = self._api.websdk.Certificates.Dissociate.post(
            certificate_dn=certificate_dn,
            application_dn=[self._get_dn(a) for a in applications],
            delete_orphans=delete_orphans
        )
        result.assert_valid_response()

    def download(self, format: str, certificate: 'Union[Config.Object, str]' = None, friendly_name: str = None,
                 include_chain: bool = False, include_private_key: bool = False, keystore_password: str = None,
                 password: str = None, root_first_order: bool = False, vault_id: int = None):
        """
        Downloads a certificate and returns the encoded content, filename, and format as a single object. If ``vault_id``
        is provided, then that specific version of a certificate is downloaded, which is particularly useful when
        trying to download historical certificates.

        Args:
            format: One of the following:
                * Base64
                * Base64 (PKCS #8)
                * DER
                * JKS
                * PKCS #7
                * PKCS #12
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object. Not required if using vault id.
            friendly_name: Label or alias for the given format.
            include_chain: Include parent or root chain.
            include_private_key: Include the private key.
            keystore_password: JKS Keystore password.
            password: Password.
            root_first_order: If ``True``, show root certificate first, followed by intermediate, and finally the
                end entity certificate.
            vault_id: If provided, downloads the certificate with the given Vault ID. Use this when trying
                to download historical certificates. Not required if using certificate config object.

        Returns:
            A *DownloadedCertificate* with these properties

            * **certificate_data** *str* - Encoded certificate data.
            * **format** *str* - File Format.
            * **filename** *str* - File name.
        """
        if vault_id:
            result = self._api.websdk.Certificates.Retrieve.VaultId(vault_id).post(
                format=format,
                friendly_name=friendly_name,
                include_chain=include_chain,
                include_private_key=include_private_key,
                keystore_password=keystore_password,
                password=password,
                root_first_order=root_first_order
            )
        else:
            certificate_dn = self._get_dn(certificate)
            result = self._api.websdk.Certificates.Retrieve.post(
                certificate_dn=certificate_dn,
                format=format,
                friendly_name=friendly_name,
                include_chain=include_chain,
                include_private_key=include_private_key,
                keystore_password=keystore_password,
                password=password,
                root_first_order=root_first_order
            )

        return DownloadedCertificate(
            certificate_data=result.certificate_data,
            filename=result.filename,
            format=result.format
        )

    def get(self, certificate_dn: str, raise_error_if_not_exists: bool = True):
        """
        Args:
            certificate_dn: :ref:`dn` of the certificate object.
            raise_error_if_not_exists: Raise an exception if the object DN does not exist.

        Returns:
            :ref:`config_object`
        """
        return self._get_config_object(object_dn=certificate_dn, raise_error_if_not_exists=raise_error_if_not_exists)

    def get_previous_versions(self, certificate: 'Union[Config.Object, str]', exclude_expired: bool = False,
                              exclude_revoked: bool = False):
        """
        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.
            exclude_expired: If ``True``, do not include expired certificates.
            exclude_revoked: If ``True``, do not include revoked certificates.

        Returns:
            List[:class:`~.dataclasses.certificate.PreviousVersions`]
        """
        certificate_guid = self._get_guid(certificate)
        result = self._api.websdk.Certificates.Guid(certificate_guid).PreviousVersions.get(
            exclude_expired=exclude_expired,
            exclude_revoked=exclude_revoked
        )
        return result.previous_versions

    def get_validation_results(self, certificate: 'Union[Config.Object, str]'):
        """
        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.

        Returns:
            Tuple[:class:`~.dataclasses.certificate.File`, :class:`~.dataclasses.certificate.SslTls`]
        """
        certificate_guid = self._get_guid(certificate)
        result = self._api.websdk.Certificates.Guid(certificate_guid).ValidationResults.get()
        return result.file, result.ssl_tls

    def push_to_applications(self, certificate: 'Union[Config.Object, str]', applications: 'List[Union[Config.Object, str]]' = None):
        """
        Pushes the active ``certificate`` to the ``applications``.

        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.
            applications: A list of :ref:`config_object` or :ref:`dn` to each application object.
        """
        if not applications:
            certificate_dn = self._get_dn(certificate)
            applications = self._api.websdk.Config.ReadDn.post(
                object_dn=certificate_dn,
                attribute_name=X509CertificateAttributes.consumers
            ).values

        self.associate_application(
            certificate=certificate,
            applications=applications,
            push_to_new=True
        )

    def renew(self, certificate: 'Union[Config.Object, str]', csr: str = None, re_enable: bool = False):
        """
        Renews or requests a certificate.

        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.
            csr: If provided, uploads the PKCS10 CSR to TPP to send to the CA. If not provided, TPP generates the CSR.
            re_enable: The action to control a previously disabled certificate:
                If ``False``, do not renew a previously disabled certificate.
                If ``True``, clear the Disabled attribute, re-enable, and then renew the certificate (in this request).

        Returns:
            str: The current thumbprint of the active certificate. This should be used when checking the renewal status \
                 to ensure that TPP has registered a new certificate to its vault with a new thumbprint.
        """
        certificate = self._get(certificate)
        current_thumbprint = certificate.certificate_details.thumbprint
        result = self._api.websdk.Certificates.Renew.post(certificate_dn=certificate.dn, pkcs10=csr, reenable=re_enable)
        result.assert_valid_response()
        return current_thumbprint

    def reset(self, certificate: 'Union[Config.Object, str]'):
        """
        Resets the certificate to a non-processing state. No attempt to reprocess the certificate renewal is made.

        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.
        """
        certificate_dn = self._get_dn(certificate)
        result = self._api.websdk.Certificates.Reset.post(certificate_dn=certificate_dn, restart=False)
        result.assert_valid_response()
        if not result.processing_reset_completed:
            raise UnexpectedValue(f'Processing reset was not completed for {certificate_dn}.')

    def retry_from_current_stage(self, certificate: 'Union[Config.Object, str]'):
        """
        Retries renewal from the current processing stage of the ``certificate``.

        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.
        """
        certificate_dn = self._get_dn(certificate)
        result = self._api.websdk.Certificates.Retry.post(certificate_dn=certificate_dn)
        result.assert_valid_response()

    def retry_from_stage_0(self, certificate: 'Union[Config.Object, str]'):
        """
        Retries renewal from stage 0. This clears all current processing data and restarts
        processing.

        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.
        """
        certificate_dn = self._get_dn(certificate)
        result = self._api.websdk.Certificates.Reset.post(certificate_dn=certificate_dn, restart=True)
        result.assert_valid_response()
        if not result.restart_completed:
            raise UnexpectedValue(f'Restart renewal from stage 0 was not triggered on {certificate_dn}.')

    def revoke(self, certificate: 'Union[Config.Object, str]', comments: str = None, disable: bool = None,
               reason: int = None, thumbprint: str = None):
        """
        Revokes the ``certificate``. If a thumbprint is provided, then the particular historical certificate
        associated to the certificate having that thumbprint will be revoked.

        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.
            comments: Any comments to include in the revoke request.
            disable: If ``True``, disables the certificate object.
            reason: Reason for revoking.
            thumbprint: If given, the thumbprint of the historical certificate to be revoked.
        """
        certificate_dn = self._get_dn(certificate)
        result = self._api.websdk.Certificates.Revoke.post(
            certificate_dn=certificate_dn,
            comments=comments,
            disable=disable,
            reason=reason,
            thumbprint=thumbprint
        )
        result.assert_valid_response()
        if result.success is not True:
            raise UnexpectedValue(
                f'Cannot revoke {certificate_dn} due to this error:\n{result.error}.'
            )

    def upload(self, certificate_data: str, parent_folder: 'Union[Config.Object, str]', certificate_authority_attributes: dict = None,
               name: str = None, password: str = None, private_key_data: str = None, reconcile: bool = False):
        """
        Uploads the certificate data to TPP to create a certificate object under the given parent folder DN. If the BEGIN/END
        header or footer is missing, the data is assumed to be Base 64 encoded in the PKCS#12 format. For Base 64 encoded
        certificates, characters, such as spaces and new line escape characters (/n), are optional. White space characters are
        removed before any attempt is made to decode the certificate.

        Args:
            certificate_data: Encoded certificate data.
            parent_folder: :ref:`config_object` or :ref:`dn` of the parent folder.
            certificate_authority_attributes: Attributes pertaining to the Certificate Authority to store with the certificate
                object. This is not a DN to a Certificate Authority in TPP.
            name: If given, the name of the new certificate object. If not given, then the Common Name is used.
            password: Password to decrypt the private key.
            private_key_data: Encoded private key data.
            reconcile: If ``False``, replaces the current certificate, if it exists, and stores the current certificate as a
                historical certificate. If ``True``, then TPP activates the certificate with the newest "ValidFrom" date and
                archives the other certificate as a historical certificate.

        Returns:
            :ref:`config_object` of the uploaded certificate.
        """
        if certificate_authority_attributes:
            certificate_authority_attributes = self._name_value_list(attributes=certificate_authority_attributes)

        result = self._api.websdk.Certificates.Import.post(
            certificate_data=certificate_data,
            policy_dn=self._get_dn(parent_folder),
            ca_specific_attributes=certificate_authority_attributes,
            object_name=name,
            password=password,
            private_key_data=private_key_data,
            reconcile=reconcile
        )
        result.assert_valid_response()
        return self._api.websdk.Config.IsValid.post(object_dn=result.certificate_dn).object

    def validate(self, certificates: 'List[Union[Config.Object, str]]'):
        """
        Performs SSL/TLS network validation of certificate on all applications associated to certificate that are not disabled.

        Args:
            certificates: List of :ref:`config_object` or :ref:`dn` to validate.

        Returns:
            Tuple[str, List[str]]: Tuple of :ref:`dn` and validation warnings
        """
        certificate_dns = [self._get_dn(certificate) for certificate in certificates]
        result = self._api.websdk.Certificates.Validate.post(certificate_dns=certificate_dns)
        if not result.success:
            raise UnexpectedValue(
                f'TPP failed to perform validation. Got this error: "{result.error}".'
            )
        return result.validated_certificate_dns, result.warnings

    def wait_for_enrollment_to_complete(self, certificate: 'Union[Config.Object, str]', current_thumbprint: str,
                                        timeout: int = 60, poll_interval: int = 1):
        """
        Waits for the certificate renewal to complete over a period of ``timeout`` seconds. The ``current_thumbprint``
        is returned by :meth:`renew`. Renewal is complete when the ``current_thumbprint`` does not match the new
        thumbprint and either the processing stage is "None" or greater than or equal to 800, which is the start of the
        provisioning stage. If the certificate management type is set to *Provisioning*, use the application feature
        ``wait_for_installation_to_complete()``.

        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.
            current_thumbprint: Thumbprint of the `current` certificate object.
            timeout: Timeout in seconds before raising an error.
            poll_interval: Interval to poll TPP for the renewal status.

        Returns:
            :class:`~.dataclasses.certificate.CertificateDetails`
        """
        cert = self._get(certificate=certificate)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired(poll=poll_interval):
                cert.assert_valid_response()
                thumbprint = cert.certificate_details.thumbprint
                if thumbprint and thumbprint != current_thumbprint and cert.processing_details.stage in {None, 800}:
                    return cert.certificate_details
                elif cert.processing_details.in_error:
                    break
                cert = self._get(certificate=certificate)

        raise TimeoutError(
            f'Certificate renewal for "{cert.dn}" encountered an error at stage {cert.processing_details.stage} with '
            f'status "{cert.processing_details.status}".'
        )

    def wait_for_stage(self, certificate: 'Union[Config.Object, str]', stage: int, expect_workflow: bool = True,
                       timeout: int = 60, poll_interval: int = 1):
        """
        Waits for the current processing of the certificate to reach the given ``stage`` over a period of
        ``timeout`` seconds. If the timeout is reached, an error is raised.

        Args:
            certificate: :ref:`config_object` or :ref:`dn` of the certificate object.
            stage: Stage at which to return
            expect_workflow: If ``True``, validates that a Ticket DN has been issued to the certificate.
            timeout: Timeout in seconds before throwing an error.
            poll_interval: Interval to poll TPP for the renewal status.

        Returns:
            The values returned by the |Websdk|, namely

            * **approver** *(List[str])* - List of approvers on the certificate object.
            * **certificate_details** (:class:`~.dataclasses.certificate.CertificateDetails`) - Certificate details.
            * **contact** *(List[str])* - List of contacts on the certificate object.
            * **created_on** *(datetime)* - Date on which the certificate object was created.
            * **custom_fields** *(List[dict])* - Custom fields on the certificate object.
            * **dn** *(str)* - :ref:`dn` of the certificate object.
            * **guid** *(str)* - :ref:`guid` of the certificate object.
            * **name** *(str)* - Name of the certificate object.
            * **parent_dn** *(str)* - Parent :ref:`dn` of the certificate object.
            * **processing_details** (:class:`~.dataclasses.certificate.ProcessingDetails`) - Certificate processing details.
            * **renewal_details** (:class:`~.dataclasses.certificate.RenewalDetails`) - Certificate renewal settings details.
            * **schema_class** *(str)* - Schema class.
            * **validation_details** (:class:`~.dataclasses.certificate.ValidationDetails`) - Certificate validation details.
        """
        cert = self._get(certificate=certificate)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired(poll=poll_interval):
                if cert.processing_details.in_error is True:
                    break
                if cert.processing_details.stage is not None:
                    if expect_workflow and cert.processing_details.stage == stage:
                        if 'pending workflow resolution' in cert.processing_details.status.lower():
                            return cert
                    elif not expect_workflow and cert.processing_details.stage >= stage:
                        return cert
                cert = self._get(certificate=certificate)

        if expect_workflow and stage == cert.processing_details.stage:
            msg = f'After {timeout} seconds certificate renewal reached stage {stage}, but no workflow was issued. ' \
                  f'The current stage is {cert.processing_details.stage} with status {cert.processing_details.status}.'
        else:
            msg = f'Certificate renewal did not reach stage {stage} after {timeout} seconds. The current ' \
                  f'stage is {cert.processing_details.stage} with status {cert.processing_details.status}.'
        raise UnexpectedValue(msg)
