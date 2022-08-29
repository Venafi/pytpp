class KeyContext:
    authentication = 'authentication'
    encryption = 'encryption'
    null = 'null'
    signing = 'signing'


class Mechanism:
    ec_dsa = 4161  # EcDsa
    ec_dsa_sha_1 = 4162  # EcDsaSha1
    ec_dsa_sha_224 = 4163  # EcDsaSha224
    ec_dsa_sha_256 = 4164  # EcDsaSha256
    ec_dsa_sha_384 = 4165  # EcDsaSha384
    ec_dsa_sha_512 = 4166  # EcDsaSha512
    ed_dsa = 4183  # EdDsa
    rsa_pkcs = 1  # RsaPkcs
    rsa_pkcs_oaep = 9  # RsaPkcsOaep
    rsa_pkcs_pss = 13  # RsaPkcsPss
    rsa_pss_sha_1 = 14  # RsaPssSha1
    rsa_pss_sha_224 = 71  # RsaPssSha224
    rsa_pss_sha_256 = 67  # RsaPssSha256
    rsa_pss_sha_384 = 68  # RsaPssSha384
    rsa_pss_sha_512 = 69  # RsaPssSha512
    rsa_sha_1 = 6  # RsaSha1
    rsa_sha_224 = 70  # RsaSha224
    rsa_sha_256 = 64  # RsaSha256
    rsa_sha_384 = 65  # RsaSha384
    rsa_sha_512 = 66  # RsaSha512
    sha_1 = 544  # Sha1
    sha_224 = 597  # Sha224
    sha_256 = 592  # Sha256
    sha_384 = 608  # Sha384
    sha_512 = 624  # Sha512
