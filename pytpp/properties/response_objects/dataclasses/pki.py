from dataclasses import dataclass
from typing import List


@dataclass
class PKI:
    certificate_dn: str
    certificate_guid: str
    pki_dn: str
    pki_guid: str


@dataclass
class Certificate:
    city: str
    common_name: str
    country: str
    key_algorithm: str
    key_bit_size: str
    organization: str
    organizational_units: List[str]
    sans: 'List[SANS]'
    state: str


@dataclass
class Installation:
    credential_dn: str
    host: str


@dataclass
class SANS:
    name: str
    typename: str
