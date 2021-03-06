from pytpp.attributes._helper import IterableMeta, Attribute
from pytpp.attributes.driver_base import DriverBaseAttributes
from pytpp.attributes.monitoring_base import MonitoringBaseAttributes


class X509CertificateBaseAttributes(DriverBaseAttributes, MonitoringBaseAttributes, metaclass=IterableMeta):
    __config_class__ = "X509 Certificate Base"
    adaptable_ca_binary_data_vault_id = Attribute('Adaptable CA:Binary Data Vault ID', min_version='16.2')
    adaptable_ca_early_password_vault_id = Attribute('Adaptable CA:Early Password Vault ID', min_version='17.4')
    adaptable_ca_early_pkcs7_vault_id = Attribute('Adaptable CA:Early Pkcs7 Vault ID', min_version='16.2')
    adaptable_ca_early_private_key_vault_id = Attribute('Adaptable CA:Early Private Key Vault ID', min_version='17.4')
    adaptable_ca_script_hash_mismatch_error = Attribute('Adaptable CA:Script Hash Mismatch Error', min_version='18.4')
    adaptable_workflow_approvers = Attribute('Adaptable Workflow Approvers', min_version='18.3')
    adaptable_workflow_reference_id = Attribute('Adaptable Workflow Reference ID', min_version='18.3')
    adaptable_workflow_stage = Attribute('Adaptable Workflow Stage', min_version='18.3')
    address = Attribute('Address')
    allow_private_key_reuse = Attribute('Allow Private Key Reuse', min_version='15.4')
    amazon_ca_first_pickup_request = Attribute('Amazon CA:First Pickup Request', min_version='16.1')
    amazon_ca_timestamp = Attribute('Amazon CA:Timestamp', min_version='16.1')
    approved_issuer = Attribute('Approved Issuer')
    approver = Attribute('Approver')
    csr_thumbprint = Attribute('CSR Thumbprint', min_version='20.1')
    csr_vault_id = Attribute('CSR Vault Id')
    certificate_authority = Attribute('Certificate Authority')
    certificate_download_pbes2_algorithm = Attribute('Certificate Download: PBES2 Algorithm', min_version='16.3')
    certificate_process_validator = Attribute('Certificate Process Validator', min_version='19.3')
    certificate_vault_id = Attribute('Certificate Vault Id')
    city = Attribute('City')
    comodo_ca_dcv_email = Attribute('Comodo CA:DCV Email')
    comodo_ca_server_type_id = Attribute('Comodo CA:Server Type Id')
    comodo_ccm_ca_pass_phrase = Attribute('Comodo CCM CA:Pass Phrase')
    comodo_ccm_ca_server_type = Attribute('Comodo CCM CA:Server Type')
    consumers = Attribute('Consumers')
    country = Attribute('Country')
    created_by = Attribute('Created By', min_version='15.1')
    digicert_ca_address = Attribute('DigiCert CA:Address')
    digicert_ca_request_id = Attribute('DigiCert CA:Request Id')
    digicert_ca_server_type = Attribute('DigiCert CA:Server Type')
    digicert_ca_specific_end_date = Attribute('DigiCert CA:Specific End Date', min_version='17.3')
    digicert_ca_zip = Attribute('DigiCert CA:Zip')
    disable_automatic_renewal = Attribute('Disable Automatic Renewal')
    disable_password_complexity = Attribute('Disable Password Complexity', min_version='15.4')
    discovered_by_dn = Attribute('Discovered By DN', min_version='19.1')
    discovered_on = Attribute('Discovered On')
    domain_suffix_whitelist = Attribute('Domain Suffix Whitelist', min_version='15.4')
    esm_ca_override_default_key_update_policy = Attribute('ESM CA:Override Default Key Update Policy')
    est_reenrollment_in_progress = Attribute('EST ReEnrollment In Progress', min_version='20.1')
    elliptic_curve = Attribute('Elliptic Curve', min_version='17.1')
    encryption_driver = Attribute('Encryption Driver')
    enforce_unique_subject = Attribute('Enforce Unique Subject', min_version='15.4')
    entrust_pki_gateway_early_private_key_vault_id = Attribute('Entrust PKI Gateway:Early Private Key Vault ID', min_version='20.2')
    entrust_pki_gateway_early_x509_vault_id = Attribute('Entrust PKI Gateway:Early X509 Vault ID', min_version='20.2')
    entrustnet_ca_additional_emails = Attribute('EntrustNET CA:Additional Emails', min_version='17.1')
    entrustnet_ca_additional_field_value = Attribute('EntrustNET CA:Additional Field Value')
    entrustnet_ca_email_address = Attribute('EntrustNET CA:Email Address')
    entrustnet_ca_first_name = Attribute('EntrustNET CA:First Name')
    entrustnet_ca_first_pickup_request = Attribute('EntrustNET CA:First Pickup Request', min_version='15.4')
    entrustnet_ca_last_name = Attribute('EntrustNET CA:Last Name')
    entrustnet_ca_specific_end_date = Attribute('EntrustNET CA:Specific End Date')
    entrustnet_ca_timestamp = Attribute('EntrustNET CA:Timestamp', min_version='15.4')
    escalation_notice_interval = Attribute('Escalation Notice Interval')
    escalation_notice_start = Attribute('Escalation Notice Start')
    expiration_notice_interval = Attribute('Expiration Notice Interval')
    expiration_notice_start = Attribute('Expiration Notice Start')
    fields = Attribute('Fields')
    generate_keypair_on_application = Attribute('Generate Keypair On Application')
    geotrust_ca_address = Attribute('GeoTrust CA:Address')
    geotrust_ca_admin_contact_address = Attribute('GeoTrust CA:Admin Contact Address')
    geotrust_ca_admin_contact_city = Attribute('GeoTrust CA:Admin Contact City')
    geotrust_ca_admin_contact_country = Attribute('GeoTrust CA:Admin Contact Country')
    geotrust_ca_admin_contact_email_address = Attribute('GeoTrust CA:Admin Contact Email Address')
    geotrust_ca_admin_contact_first_name = Attribute('GeoTrust CA:Admin Contact First Name')
    geotrust_ca_admin_contact_last_name = Attribute('GeoTrust CA:Admin Contact Last Name')
    geotrust_ca_admin_contact_organization = Attribute('GeoTrust CA:Admin Contact Organization')
    geotrust_ca_admin_contact_phone_number = Attribute('GeoTrust CA:Admin Contact Phone Number')
    geotrust_ca_admin_contact_postal_code = Attribute('GeoTrust CA:Admin Contact Postal Code')
    geotrust_ca_admin_contact_state = Attribute('GeoTrust CA:Admin Contact State')
    geotrust_ca_admin_contact_title = Attribute('GeoTrust CA:Admin Contact Title')
    geotrust_ca_authentication_comments = Attribute('GeoTrust CA:Authentication Comments')
    geotrust_ca_authentication_statuses = Attribute('GeoTrust CA:Authentication Statuses')
    geotrust_ca_enrollment_mode = Attribute('GeoTrust CA:Enrollment Mode', min_version='15.1')
    geotrust_ca_order_id = Attribute('GeoTrust CA:Order Id')
    geotrust_ca_postal_code = Attribute('GeoTrust CA:Postal Code')
    geotrust_ca_server_count = Attribute('GeoTrust CA:Server Count')
    geotrust_ca_server_type = Attribute('GeoTrust CA:Server Type')
    geotrust_ca_telephone_number = Attribute('GeoTrust CA:Telephone Number')
    geotrust_ca_timestamp = Attribute('GeoTrust CA:Timestamp')
    geotrust_enterprise_ca_address = Attribute('GeoTrust Enterprise CA:Address')
    geotrust_enterprise_ca_admin_contact_email_address = Attribute('GeoTrust Enterprise CA:Admin Contact Email Address')
    geotrust_enterprise_ca_admin_contact_first_name = Attribute('GeoTrust Enterprise CA:Admin Contact First Name')
    geotrust_enterprise_ca_admin_contact_last_name = Attribute('GeoTrust Enterprise CA:Admin Contact Last Name')
    geotrust_enterprise_ca_admin_contact_phone_number = Attribute('GeoTrust Enterprise CA:Admin Contact Phone Number')
    geotrust_enterprise_ca_admin_contact_title = Attribute('GeoTrust Enterprise CA:Admin Contact Title')
    geotrust_enterprise_ca_approver_email = Attribute('GeoTrust Enterprise CA:Approver Email')
    geotrust_enterprise_ca_enrollment_mode = Attribute('GeoTrust Enterprise CA:Enrollment Mode', min_version='15.1')
    geotrust_enterprise_ca_postal_code = Attribute('GeoTrust Enterprise CA:Postal Code')
    geotrust_enterprise_ca_server_count = Attribute('GeoTrust Enterprise CA:Server Count')
    geotrust_enterprise_ca_server_type = Attribute('GeoTrust Enterprise CA:Server Type')
    geotrust_enterprise_ca_telephone_number = Attribute('GeoTrust Enterprise CA:Telephone Number')
    geotrust_enterprise_ca_timestamp = Attribute('GeoTrust Enterprise CA:Timestamp')
    given_name = Attribute('Given Name')
    globalsign_mssl_ca_email = Attribute('GlobalSign MSSL CA:Email')
    globalsign_mssl_ca_first_name = Attribute('GlobalSign MSSL CA:First Name')
    globalsign_mssl_ca_last_name = Attribute('GlobalSign MSSL CA:Last Name')
    globalsign_mssl_ca_phone = Attribute('GlobalSign MSSL CA:Phone')
    google_cloud_ca_early_x509_chain_vault_id = Attribute('Google Cloud CA:Early X509 Chain Vault ID', min_version='21.3')
    google_cloud_ca_early_x509_vault_id = Attribute('Google Cloud CA:Early X509 Vault ID', min_version='21.3')
    grouping_id = Attribute('Grouping Id')
    in_error = Attribute('In Error')
    in_process = Attribute('In Process', min_version='15.3')
    internet_email_address = Attribute('Internet EMail Address')
    issued_to = Attribute('Issued To')
    key_algorithm = Attribute('Key Algorithm', min_version='17.1')
    key_bit_strength = Attribute('Key Bit Strength')
    key_storage_location = Attribute('Key Storage Location', min_version='19.2')
    keynectis_sequoia_ca_fields = Attribute('Keynectis Sequoia CA:Fields')
    last_evaluated_on = Attribute('Last Evaluated On', min_version='17.2')
    last_notification = Attribute('Last Notification')
    last_renewed_by = Attribute('Last Renewed By', min_version='16.2')
    last_renewed_on = Attribute('Last Renewed On', min_version='16.2')
    last_validation_state_update = Attribute('Last Validation State Update', min_version='16.3')
    license_count = Attribute('License Count')
    management_type = Attribute('Management Type')
    manual_approval = Attribute('Manual Approval')
    manual_csr = Attribute('Manual Csr')
    microsoft_ca_request_approved = Attribute('Microsoft CA:Request Approved')
    microsoft_ca_specific_end_date = Attribute('Microsoft CA:Specific End Date', min_version='18.2')
    network_validation_disabled = Attribute('Network Validation Disabled')
    opentrust_pki_ca_fields = Attribute('OpenTrust PKI CA:Fields')
    opentrust_pki_ca_first_pickup_request = Attribute('OpenTrust PKI CA:First Pickup Request')
    opentrust_pki_ca_requester_email = Attribute('OpenTrust PKI CA:Requester Email')
    options = Attribute('Options')
    organization = Attribute('Organization')
    organizational_unit = Attribute('Organizational Unit')
    origin = Attribute('Origin', min_version='19.1')
    pkcs10_hash_algorithm = Attribute('PKCS10 Hash Algorithm', min_version='15.1')
    postal_code = Attribute('Postal Code')
    private_key_vault_id = Attribute('Private Key Vault Id')
    prohibit_wildcard = Attribute('Prohibit Wildcard', min_version='15.4')
    prohibited_subject_attributes = Attribute('Prohibited Subject Attributes', min_version='19.1')
    protection_key = Attribute('Protection Key')
    public_key_vault_id = Attribute('Public Key Vault Id', min_version='19.4')
    renewal_window = Attribute('Renewal Window')
    reverse_dc_order = Attribute('Reverse DC Order', min_version='19.1')
    revocation_check_disabled = Attribute('Revocation Check Disabled')
    revocation_check_in_error = Attribute('Revocation Check In Error')
    revocation_check_last_checked = Attribute('Revocation Check Last Checked', min_version='16.2')
    revocation_check_now = Attribute('Revocation Check Now')
    revocation_check_status = Attribute('Revocation Check Status')
    revocation_original_request = Attribute('Revocation Original Request', min_version='17.2')
    revocation_request = Attribute('Revocation Request')
    scep_transaction_id = Attribute('Scep Transaction Id')
    server_type = Attribute('Server Type')
    signing_request_subject = Attribute('Signing Request Subject')
    specific_end_date = Attribute('Specific End Date', min_version='20.2')
    stage = Attribute('Stage')
    state = Attribute('State')
    status = Attribute('Status')
    surname = Attribute('Surname')
    symantec_lhk_ca_fields = Attribute('Symantec LHK CA:Fields')
    telephone = Attribute('Telephone')
    thawte_ca_emails = Attribute('Thawte CA:Emails', min_version='15.4')
    thawte_ca_enrollment_mode = Attribute('Thawte CA:Enrollment Mode', min_version='15.4')
    thawte_ca_first_pickup_request = Attribute('Thawte CA:First Pickup Request', min_version='15.4')
    thawte_ca_timestamp = Attribute('Thawte CA:Timestamp', min_version='15.4')
    transaction_id = Attribute('Transaction Id')
    trusted_status = Attribute('Trusted Status')
    trustwave_ca_enrollment_mode = Attribute('Trustwave CA:Enrollment Mode')
    trustwave_ca_first_pickup_request = Attribute('Trustwave CA:First Pickup Request')
    trustwave_ca_timestamp = Attribute('Trustwave CA:Timestamp')
    validation_state = Attribute('Validation State', min_version='16.3')
    validity_period = Attribute('Validity Period')
    verisign_ca_additional_field_value = Attribute('VeriSign CA:Additional Field Value')
    verisign_ca_challenge_credential = Attribute('VeriSign CA:Challenge Credential')
    verisign_ca_comment = Attribute('VeriSign CA:Comment')
    verisign_ca_enrollment_mode = Attribute('VeriSign CA:Enrollment Mode')
    verisign_ca_first_pickup_request = Attribute('VeriSign CA:First Pickup Request')
    verisign_ca_license_count = Attribute('VeriSign CA:License Count')
    verisign_ca_original_challenge_credential = Attribute('VeriSign CA:Original Challenge Credential')
    verisign_ca_replacement_reason = Attribute('VeriSign CA:Replacement Reason')
    verisign_ca_server_type = Attribute('VeriSign CA:Server Type')
    verisign_ca_specific_end_date = Attribute('VeriSign CA:Specific End Date')
    verisign_ca_timestamp = Attribute('VeriSign CA:Timestamp')
    verizon_ca_additional_field_value = Attribute('Verizon CA:Additional Field Value', min_version='15.4')
    verizon_ca_challenge_credential = Attribute('Verizon CA:Challenge Credential', min_version='15.4')
    verizon_ca_challenge_credential_hint = Attribute('Verizon CA:Challenge Credential Hint', min_version='15.4')
    verizon_ca_enrollment_mode = Attribute('Verizon CA:Enrollment Mode', min_version='15.4')
    verizon_ca_first_pickup_request = Attribute('Verizon CA:First Pickup Request', min_version='15.4')
    verizon_ca_license_count = Attribute('Verizon CA:License Count', min_version='15.4')
    verizon_ca_number_of_servers = Attribute('Verizon CA:Number Of Servers', min_version='15.4')
    verizon_ca_organization_summary = Attribute('Verizon CA:Organization Summary', min_version='15.4')
    verizon_ca_server_name = Attribute('Verizon CA:Server Name', min_version='15.4')
    verizon_ca_server_type = Attribute('Verizon CA:Server Type', min_version='15.4')
    verizon_ca_tech_email = Attribute('Verizon CA:Tech Email', min_version='15.4')
    verizon_ca_tech_firstname = Attribute('Verizon CA:Tech Firstname', min_version='15.4')
    verizon_ca_tech_surname = Attribute('Verizon CA:Tech Surname', min_version='15.4')
    verizon_ca_tech_telnumber = Attribute('Verizon CA:Tech Telnumber', min_version='15.4')
    verizon_ca_timestamp = Attribute('Verizon CA:Timestamp', min_version='15.4')
    want_renewal = Attribute('Want Renewal')
    x509_d = Attribute('X509 D', min_version='15.2')
    x509_dc = Attribute('X509 DC', min_version='15.2')
    x509_dnq = Attribute('X509 DNQ', min_version='15.2')
    x509_e = Attribute('X509 E', min_version='15.2')
    x509_extension_fields = Attribute('X509 Extension Fields')
    x509_gn = Attribute('X509 GN', min_version='15.2')
    x509_gq = Attribute('X509 GQ', min_version='15.2')
    x509_i = Attribute('X509 I', min_version='15.2')
    x509_p = Attribute('X509 P', min_version='15.2')
    x509_pa = Attribute('X509 PA', min_version='15.2')
    x509_pc = Attribute('X509 PC', min_version='15.2')
    x509_sa = Attribute('X509 SA', min_version='15.2')
    x509_sn = Attribute('X509 SN', min_version='15.2')
    x509_sno = Attribute('X509 SNO', min_version='15.2')
    x509_subject = Attribute('X509 Subject')
    x509_subjectaltname = Attribute('X509 SubjectAltName')
    x509_subjectaltname_dns = Attribute('X509 SubjectAltName DNS')
    x509_subjectaltname_ipaddress = Attribute('X509 SubjectAltName IPAddress')
    x509_subjectaltname_othername_upn = Attribute('X509 SubjectAltName OtherName UPN')
    x509_subjectaltname_rfc822 = Attribute('X509 SubjectAltName RFC822')
    x509_subjectaltname_uri = Attribute('X509 SubjectAltName URI')
    x509_t = Attribute('X509 T', min_version='15.2')
    x509_tn = Attribute('X509 TN', min_version='15.2')
    x509_ua = Attribute('X509 UA', min_version='15.2')
    x509_uid = Attribute('X509 UID', min_version='15.2')
    x509_un = Attribute('X509 UN', min_version='15.2')
    xolphin_ca_address = Attribute('Xolphin CA:Address')
    xolphin_ca_approver_email_address = Attribute('Xolphin CA:Approver Email Address')
    xolphin_ca_approver_first_name = Attribute('Xolphin CA:Approver First Name')
    xolphin_ca_approver_last_name = Attribute('Xolphin CA:Approver Last Name')
    xolphin_ca_approver_phone_number = Attribute('Xolphin CA:Approver Phone Number')
    xolphin_ca_approver_type = Attribute('Xolphin CA:Approver Type')
    xolphin_ca_city = Attribute('Xolphin CA:City')
    xolphin_ca_company = Attribute('Xolphin CA:Company')
    xolphin_ca_country_code = Attribute('Xolphin CA:Country Code')
    xolphin_ca_department = Attribute('Xolphin CA:Department')
    xolphin_ca_effective_polling_interval = Attribute('Xolphin CA:Effective Polling Interval')
    xolphin_ca_kvk_number = Attribute('Xolphin CA:KvK Number')
    xolphin_ca_postbox = Attribute('Xolphin CA:Postbox')
    xolphin_ca_reference_number = Attribute('Xolphin CA:Reference Number')
    xolphin_ca_zip_code = Attribute('Xolphin CA:Zip Code')
