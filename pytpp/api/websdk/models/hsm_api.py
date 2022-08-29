from __future__ import annotations
from datetime import datetime
from pytpp.api.api_base import ObjectModel, ApiField


class Certificate(ObjectModel):
    authentication: str = ApiField(alias='Authentication')
    check_value: str = ApiField(alias='CheckValue')
    created_on: datetime = ApiField(alias='CreatedOn')
    encipherment: bool = ApiField(alias='Encipherment')
    end_date: datetime = ApiField(alias='EndDate')
    environment_type: int = ApiField(alias='EnvironmentType')
    handle: int = ApiField(alias='Handle')
    id: int = ApiField(alias='Id')
    issuer: str = ApiField(alias='Issuer')
    key_context: str = ApiField(alias='KeyContext')
    key_id: str = ApiField(alias='KeyId')
    label: str = ApiField(alias='Label')
    object_type: int = ApiField(alias='ObjectType')
    signing: bool = ApiField(alias='Signing')
    start_date: datetime = ApiField(alias='StartDate')
    subject: str = ApiField(alias='Subject')
    token: bool = ApiField(alias='Token')
    trusted: bool = ApiField(alias='Trusted')
    value: str = ApiField(alias='Value')


class PrivateKey(ObjectModel):
    authentication: bool = ApiField(alias='Authentication')
    created_on: datetime = ApiField(alias='CreatedOn')
    curve: str = ApiField(alias='Curve')
    decrypt: bool = ApiField(alias='Decrypt')
    encipherment: bool = ApiField(alias='Encipherment')
    environment_type: int = ApiField(alias='EnvironmentType')
    exponent: str = ApiField(alias='Exponent')
    handle: int = ApiField(alias='Handle')
    id: str = ApiField(alias='Id')
    key_context: str = ApiField(alias='KeyContext')
    key_id: str = ApiField(alias='KeyId')
    key_type: str = ApiField(alias='KeyType')
    label: str = ApiField(alias='Label')
    modulus: str = ApiField(alias='Modulus')
    object_type: int = ApiField(alias='ObjectType')
    params: str = ApiField(alias='Params')
    private: bool = ApiField(alias='Private')
    sign: bool = ApiField(alias='Sign')
    signing: bool = ApiField(alias='Signing')
    token: bool = ApiField(alias='Token')
    unwrap: bool = ApiField(alias='Unwrap')


class PublicKey(ObjectModel):
    authentication: bool = ApiField(alias='Authentication')
    bits: str = ApiField(alias='Bits')
    created_on: datetime = ApiField(alias='CreatedOn')
    curve: str = ApiField(alias='Curve')
    ec_point: str = ApiField(alias='ECPoint')
    encipherment: bool = ApiField(alias='Encipherment')
    encrypt: str = ApiField(alias='Encrypt')
    environment_type: int = ApiField(alias='EnvironmentType')
    exponent: str = ApiField(alias='Exponent')
    handle: int = ApiField(alias='Handle')
    id: str = ApiField(alias='Id')
    key_context: str = ApiField(alias='KeyContext')
    key_id: str = ApiField(alias='KeyId')
    key_type: str = ApiField(alias='KeyType')
    label: str = ApiField(alias='Label')
    modulus: str = ApiField(alias='Modulus')
    object_type: int = ApiField(alias='ObjectType')
    params: str = ApiField(alias='Params')
    signing: bool = ApiField(alias='Signing')
    token: bool = ApiField(alias='Token')
    verify: str = ApiField(alias='Verify')
    wrap: str = ApiField(alias='Wrap')


class ClientInfo(ObjectModel):
    client_library_name: str = ApiField(alias='ClientLibraryName')
    client_library_version: str = ApiField(alias='ClientLibraryVersion')


class ProcessInfo(ObjectModel):
    command_line: str = ApiField(alias='CommandLine')
    executable: str = ApiField(alias='Executable')
    executable_hash: str = ApiField(alias='ExecutableHash')
    executable_issuer: str = ApiField(alias='ExecutableIssuer')
    executable_signer: str = ApiField(alias='ExecutableSigner')
    executable_size: int = ApiField(alias='ExecutableSize')
    machine: str = ApiField(alias='Machine')
    username: str = ApiField(alias='Username')


class Parameter(ObjectModel):
    hash_alg: str = ApiField(alias='HashAlg')
    iv: str = ApiField(alias='IV')
    mgf: str = ApiField(alias='MGF')
    parameter_type: str = ApiField(alias='ParameterType')
    salt_len: int = ApiField(alias='SaltLen')
    source: int = ApiField(alias='Source')
    source_data: str = ApiField(alias='SourceData')
