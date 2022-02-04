from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.application_group import ApplicationGroupAttributes


class PKCS11ApplicationGroupAttributes(ApplicationGroupAttributes, metaclass=IterableMeta):
	__config_class__ = "PKCS11 Application Group"
	hsm_cblob = Attribute('HSM:CBlob')
	hsm_cka_label_format = Attribute('HSM:CKA LABEL Format')
	hsm_csr_subject_dn = Attribute('HSM:CSR Subject DN')
	hsm_embed_sans_in_csr = Attribute('HSM:Embed SANs in CSR')
	hsm_import_certificate = Attribute('HSM:Import Certificate')
	hsm_issued_id = Attribute('HSM:Issued ID')
	hsm_issued_label = Attribute('HSM:Issued Label')
	hsm_kpblob = Attribute('HSM:KPBlob')
	hsm_last_issued_id = Attribute('HSM:Last Issued ID')
	hsm_last_issued_kpblob = Attribute('HSM:Last Issued KPBlob')
	hsm_last_issued_label = Attribute('HSM:Last Issued Label')
	hsm_pkcs11attributes = Attribute('HSM:PKCS11Attributes')
	hsm_protection_type = Attribute('HSM:Protection Type')
	hsm_requested_cka_label = Attribute('HSM:Requested CKA LABEL')
	hsm_requested_ecdh = Attribute('HSM:Requested ECDH')
	hsm_requested_usecase = Attribute('HSM:Requested Usecase')
	hsm_reverse_subject_dn = Attribute('HSM:Reverse Subject DN')
	hsm_tmp_issued_cblob = Attribute('HSM:TMP Issued CBlob')
	hsm_tmp_issued_id = Attribute('HSM:TMP Issued ID')
	hsm_tmp_issued_kpblob = Attribute('HSM:TMP Issued KPBlob')
	hsm_token_label = Attribute('HSM:Token Label')
	hsm_token_password = Attribute('HSM:Token Password')
