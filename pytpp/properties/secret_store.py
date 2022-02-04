class Namespaces:
    config = 'config'


class KeyNames:
    software_default = 'Software:Default'
    null_null = 'Null:Null'


class VaultTypes:
    none = 0
    private_key = 1
    certificate = 2
    pkcs12 = 4
    symmetric_key = 8
    state = 16  # Obsolete
    password = 32
    csr = 64  # Obsolete: use pkcs10 instead
    blob = 128
    pkcs8 = 256
    pkcs10 = 512
    file = 1024
    rsa_public_key = 2048  # Obsolete: use archived_public_key instead
    public_key = 4096
    archived_certificate = 1073741826
    archived_pkcs12 = 1073741828
    archived_symmetric_key = 1073741832
    archived_state = 1073741840  # Obsolete
    archived_password = 1073741856
    archived_blob = 1073741952
    archived_pkcs8 = 1073742080
    archived_pkcs10 = 1073742336
    archived_file = 1073742848
    archived_rsa_public_key  = 1073743872  # Obsolete: use archived_public_key instead
    archived_public_key = 1073745920
