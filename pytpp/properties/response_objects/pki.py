from pytpp.properties.response_objects.dataclasses import pki


class PKI:
    @staticmethod
    def PKI(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return pki.PKI(
            certificate_dn=response_object.get('CertificateDN'),
            certificate_guid=response_object.get('CertificateGuid'),
            pki_dn=response_object.get('PkiDn'),
            pki_guid=response_object.get('PkiGuid'),
        )

    @staticmethod
    def Certificate(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return pki.Certificate(
            city=response_object.get('City'),
            common_name=response_object.get('CommonName'),
            country=response_object.get('Country'),
            key_algorithm=response_object.get('KeyAlgorithm'),
            key_bit_size=response_object.get('KeyBitSize'),
            organization=response_object.get('Organization'),
            organizational_units=response_object.get('OrganizationalUnits'),
            sans=[PKI.SANS(sans) for sans in response_object.get('SANs', [])],
            state=response_object.get('State'),
        )

    @staticmethod
    def Installation(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return pki.Installation(
            credential_dn=response_object.get('CredentialDn'),
            host=response_object.get('Host'),
        )

    @staticmethod
    def SANS(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return pki.SANS(
            name=response_object.get('Name'),
            typename=response_object.get('TypeName'),
        )
