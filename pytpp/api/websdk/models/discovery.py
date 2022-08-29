from typing import List

from pytpp.api.api_base import ApiField, ObjectModel


class Certificate(ObjectModel):
    certificate: str = ApiField(alias='certificate')
    fingerprint: str = ApiField(alias='fingerprint')


class Protocol(ObjectModel):
    certificates: List[str] = ApiField(alias='certificates')
    protocol: str = ApiField(alias='protocol')


class Endpoint(ObjectModel):
    certificates: List[Certificate] = ApiField(alias='certificates')
    host: str = ApiField(alias='host')
    ip: str = ApiField(alias='ip')
    port: int = ApiField(alias='port')
    protocols: List[Protocol] = ApiField(alias='protocols')
