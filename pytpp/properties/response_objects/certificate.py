from pytpp.tools.helpers.date_converter import from_date_string
from pytpp.properties.response_objects.dataclasses import certificate


class Certificate:
    @staticmethod
    def Certificate(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}

        return certificate.Certificate(
            created_on=response_object.get('CreatedOn'),
            dn=response_object.get('DN'),
            guid=response_object.get('Guid'),
            name=response_object.get('Name'),
            parent_dn=response_object.get('ParentDn'),
            schema_class=response_object.get('SchemaClass'),
            x509=Certificate._X509(response_object.get('X509')),
            links=[Certificate.Link(link) for link in response_object.get('_links', [])],
        )

    @staticmethod
    def Link(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate.Link(
            details=response_object.get('Details'),
            next=response_object.get('Next'),
            previous=response_object.get('Previous'),
        )

    @staticmethod
    def CSR(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate.CSR(
            details=Certificate._CSRDetails(response_object.get('Details')),
            enrollable=response_object.get('Enrollable'),
        )

    @staticmethod
    def Policy(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate.Policy(
            certificate_authority=Certificate._LockedSingleValue(response_object.get('CertificateAuthority')),
            csr_generation=Certificate._LockedSingleValue(response_object.get('CsrGeneration')),
            key_generation=Certificate._LockedSingleValue(response_object.get('KeyGeneration')),
            key_pair=Certificate._LockedKeyPair(response_object.get('KeyPair')),
            management_type=Certificate._LockedSingleValue(response_object.get('ManagementType')),
            private_key_reuse_allowed=response_object.get('PrivateKeyReuseAllowed'),
            subj_alt_name_dns_allowed=response_object.get('SubjAltNameDnsAllowed'),
            subj_alt_name_email_allowed=response_object.get('SubjAltNameEmailAllowed'),
            subj_alt_name_ip_allowed=response_object.get('SubjAltNameIpAllowed'),
            subj_alt_name_upn_allowed=response_object.get('SubjAltNameUpnAllowed'),
            subj_alt_name_uri_allowed=response_object.get('SubjAltNameUriAllowed'),
            subject=Certificate._LockedSubject(response_object.get('Subject')),
            unique_subject_enforced=response_object.get('UniqueSubjectEnforced'),
            whitelisted_domains=response_object.get('WhitelistedDomains'),
            wildcards_allowed=response_object.get('WildcardsAllowed'),
        )

    @staticmethod
    def CertificateDetails(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate.CertificateDetails(
            c=response_object.get('C'),
            cn=response_object.get('CN'),
            enhanced_key_usage=response_object.get('EnhancedKeyUsage'),
            issuer=response_object.get('Issuer'),
            key_algorithm=response_object.get('KeyAlgorithm'),
            key_size=response_object.get('KeySize'),
            key_usage=response_object.get('KeyUsage'),
            l=response_object.get('L'),
            o=response_object.get('O'),
            ou=response_object.get('OU'),
            public_key_hash=response_object.get('PublicKeyHash'),
            s=response_object.get('S'),
            ski_key_identifier=response_object.get('SKIKeyIdentifier'),
            serial=response_object.get('Serial'),
            signature_algorithm=response_object.get('SignatureAlgorithm'),
            signature_algorithm_oid=response_object.get('SignatureAlgorithmOID'),
            store_added=response_object.get('StoreAdded'),
            subject=response_object.get('Subject'),
            subject_alt_name_dns=response_object.get('SubjectAltNameDNS'),
            subject_alt_name_email=response_object.get('SubjectAltNameEmail'),
            subject_alt_name_ip=response_object.get('SubjectAltNameIp'),
            subject_alt_name_upn=response_object.get('SubjectAltNameUpn'),
            subject_alt_name_uri=response_object.get('SubjectAltNameUri'),
            thumbprint=response_object.get('Thumbprint'),
            valid_from=from_date_string(response_object.get('ValidFrom')),
            valid_to=from_date_string(response_object.get('ValidTo')),
        )

    @staticmethod
    def PreviousVersions(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate.PreviousVersions(
            certificate_details=Certificate.CertificateDetails(response_object.get('CertificateDetails')),
            vault_id=response_object.get('VaultId'),
        )

    @staticmethod
    def ProcessingDetails(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate.ProcessingDetails(
            in_error=response_object.get('InError'),
            stage=response_object.get('Stage'),
            status=response_object.get('Status'),
        )

    @staticmethod
    def RenewalDetails(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate.RenewalDetails(
            city=response_object.get('City'),
            country=response_object.get('Country'),
            organization=response_object.get('Organization'),
            organizational_unit=response_object.get('OrganizationUnit'),
            state=response_object.get('State'),
            subject=response_object.get('Subject'),
            subject_alt_name_dns=response_object.get('SubjectAltNameDNS'),
            subject_alt_name_email=response_object.get('SubjectAltNameEmail'),
            subject_alt_name_ip_address=response_object.get('SubjectAltNameIPAddress'),
            subject_alt_name_other_name_upn=response_object.get('SubjectAltNameOtherNameUPN'),
            subject_alt_name_uri=response_object.get('SubjectAltNameURI'),
            valid_from=from_date_string(response_object.get('ValidFrom')),
            valid_to=from_date_string(response_object.get('ValidTo')),
        )

    @staticmethod
    def ValidationDetails(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate.ValidationDetails(
            last_validation_state_update=response_object.get('LastValidationStateUpdate'),
            validation_state=response_object.get('ValidationState'),
        )

    @staticmethod
    def SslTls(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate.SslTls(
            host=response_object.get('Host'),
            ip_address=response_object.get('IpAddress'),
            port=response_object.get('Port'),
            result=Certificate._SslTlsResult(response_object.get('Result')),
            sources=response_object.get('Sources'),
        )

    @staticmethod
    def File(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate.File(
            installation=response_object.get('Installation'),
            performed_on=from_date_string(response_object.get('PerformedOn')),
            result=response_object.get('Result'),
        )

    @staticmethod
    def _SslTlsResult(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate._SslTlsResult(
            chain=Certificate._BitMaskValues(response_object.get('Chain')),
            end_entity=Certificate._BitMaskValues(response_object.get('EndEntity')),
            id=response_object.get('ID'),
            protocols=Certificate._BitMaskValues(response_object.get('Protocols')),
        )

    @staticmethod
    def _BitMaskValues(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate._BitMaskValues(
            bitmask=response_object.get('BitMask'),
            values=response_object.get('Values'),
        )

    @staticmethod
    def _SANS(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate._SANS(
            dns=response_object.get('DNS'),
            ip=response_object.get('IP'),
        )

    @staticmethod
    def _X509(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate._X509(
            cn=response_object.get('CN'),
            issuer=response_object.get('Issuer'),
            key_algorithm=response_object.get('KeyAlgorithm'),
            key_size=response_object.get('KeySize'),
            sans=response_object.get('SANS'),
            serial=response_object.get('Serial'),
            subject=response_object.get('Subject'),
            thumbprint=response_object.get('Thumbprint'),
            valid_from=from_date_string(response_object.get('ValidFrom')),
            valid_to=from_date_string(response_object.get('ValidTo')),
        )

    @staticmethod
    def _CompliantSingleValue(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate._CompliantSingleValue(
            compliant=response_object.get('Compliant'),
            value=response_object.get('Value'),
        )

    @staticmethod
    def _CompliantMultiValue(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate._CompliantMultiValue(
            compliant=response_object.get('Compliant'),
            values=response_object.get('Values'),
        )

    @staticmethod
    def _LockedSingleValue(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate._LockedSingleValue(
            locked=response_object.get('Locked'),
            value=response_object.get('Value'),
        )

    @staticmethod
    def _LockedMultiValue(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate._LockedMultiValue(
            locked=response_object.get('Locked'),
            values=response_object.get('Values'),
        )

    @staticmethod
    def _LockedKeyPair(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate._LockedKeyPair(
            key_algorithm=Certificate._LockedSingleValue(response_object.get('KeyAlgorithm')),
            key_size=Certificate._LockedSingleValue(response_object.get('KeySize')),
        )

    @staticmethod
    def _LockedSubject(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate._LockedSubject(
            city=Certificate._LockedSingleValue(response_object.get('City')),
            country=Certificate._LockedSingleValue(response_object.get('Country')),
            organization=Certificate._LockedSingleValue(response_object.get('Organization')),
            organizational_units=Certificate._LockedMultiValue(response_object.get('OrganizationalUnit')),
            state=Certificate._LockedSingleValue(response_object.get('State')),
        )

    @staticmethod
    def _CSRDetails(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return certificate._CSRDetails(
            city=Certificate._CompliantSingleValue(response_object.get('City')),
            common_name=Certificate._CompliantSingleValue(response_object.get('CommonName')),
            country=Certificate._CompliantSingleValue(response_object.get('Country')),
            key_algorithm=Certificate._CompliantSingleValue(response_object.get('KeyAlgorithm')),
            key_size=Certificate._CompliantSingleValue(response_object.get('KeySize')),
            organization=Certificate._CompliantSingleValue(response_object.get('Organization')),
            organizational_unit=Certificate._CompliantMultiValue(response_object.get('OrganizationalUnit')),
            private_key_reused=Certificate._CompliantSingleValue(response_object.get('PrivateKeyReused')),
            state=Certificate._CompliantSingleValue(response_object.get('State')),
            subj_alt_name_dns=Certificate._CompliantMultiValue(response_object.get('SubjAltNameDns')),
            subj_alt_name_email=Certificate._CompliantMultiValue(response_object.get('SubjAltNameEmail')),
            subj_alt_name_ip=Certificate._CompliantMultiValue(response_object.get('SubjAltNameIp')),
            subj_alt_name_upn=Certificate._CompliantMultiValue(response_object.get('SubjAltNameUpn')),
            subj_alt_name_uri=Certificate._CompliantMultiValue(response_object.get('SubjAltNameUri')),
        )
