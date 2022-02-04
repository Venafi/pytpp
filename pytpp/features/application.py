from base64 import b64encode
from hashlib import sha256
from pytpp.properties.config import ApplicationAttributeValues
from pytpp.attributes.adaptable_app import AdaptableAppAttributes
from pytpp.attributes.amazon_app import AmazonAppAttributes
from pytpp.attributes.apache import ApacheAttributes
from pytpp.attributes.azure_key_vault import AzureKeyVaultAttributes
from pytpp.attributes.bluecoat_sslva import BlueCoatSSLVAAttributes
from pytpp.attributes.capi import CAPIAttributes
from pytpp.attributes.netscaler import NetScalerAttributes
from pytpp.attributes.connectdirect import ConnectDirectAttributes
from pytpp.attributes.f5_authentication_bundle import F5AuthenticationBundleAttributes
from pytpp.attributes.f5_ltm_advanced import F5LTMAdvancedAttributes
from pytpp.attributes.google_cloud_app import GoogleCloudAppAttributes
from pytpp.attributes.datapower import DataPowerAttributes
from pytpp.attributes.gsk import GSKAttributes
from pytpp.attributes.imperva_mx import ImpervaMXAttributes
from pytpp.attributes.jks import JKSAttributes
from pytpp.attributes.iplanet import iPlanetAttributes
from pytpp.attributes.palo_alto_network_fw import PaloAltoNetworkFWAttributes
from pytpp.attributes.pkcs_12 import PKCS12Attributes
from pytpp.attributes.pkcs11 import PKCS11Attributes
from pytpp.attributes.riverbed_steelhead import RiverbedSteelHeadAttributes
from pytpp.attributes.tealeaf_pca import TealeafPCAAttributes
from pytpp.attributes.vam_nshield import VAMnShieldAttributes
from pytpp.attributes.application_base import ApplicationBaseAttributes
from pytpp.attributes.application_group import ApplicationGroupAttributes
from pytpp.attributes.apache_application_group import ApacheApplicationGroupAttributes
from pytpp.attributes.pkcs11_application_group import PKCS11ApplicationGroupAttributes
from pytpp.attributes.x509_certificate import X509CertificateAttributes
from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.features.definitions.exceptions import InvalidResultCode, UnexpectedValue, FeatureException
from pytpp.features.definitions.classes import Classes
from pytpp.properties.secret_store import KeyNames, Namespaces, VaultTypes
from pytpp.tools.helpers.date_converter import from_date_string
from typing import Union, List, TYPE_CHECKING
if TYPE_CHECKING:
    from pytpp.tools.vtypes import Config, Identity


# region Applications
class _ApplicationBase(FeatureBase):
    def __init__(self, api, class_name: str):
        super().__init__(api=api)
        self._class_name = str(class_name)

    def delete(self, application: 'Union[Config.Object, str]'):
        """
        Deletes an application object.

        Args:
            application: :ref:`config_object` or :ref:`dn` of the application object.
        """
        application_dn = self._get_dn(application)
        self._secret_store_delete(object_dn=application_dn)
        self._config_delete(object_dn=application_dn)

    def disable(self, application: 'Union[Config.Object, str]'):
        """
        Disables all processing and provisioning of the application.

        Args:
            application: :ref:`config_object` or :ref:`dn` of the application object.
        """
        application_dn = self._get_dn(application)
        result = self._api.websdk.Config.Write.post(
            object_dn=application_dn,
            attribute_data=self._name_value_list({
                ApplicationBaseAttributes.disabled: ["1"]
            }, keep_list_values=True)
        ).result

        if result.code != 1:
            raise InvalidResultCode(code=result.code, code_description=result.config_result)

    def enable(self, application: 'Union[Config.Object, str]'):
        """
        Enables all processing and provisioning of the application.

        Args:
            application: :ref:`config_object` or :ref:`dn` of the application object.
        """
        application_dn = self._get_dn(application)
        result = self._api.websdk.Config.ClearAttribute.post(
            object_dn=application_dn,
            attribute_name=ApplicationBaseAttributes.disabled
        ).result

        if result.code != 1:
            raise InvalidResultCode(code=result.code, code_description=result.config_result)

    def get(self, application_dn: str, raise_error_if_not_exists: bool = True):
        """
        Args:
            application_dn: :ref:`dn` of the application object.
            raise_error_if_not_exists: Raise an exception if the application :ref:`dn` does not exist.

        Returns:
            :ref:`config_object` of the application
        """
        return self._get_config_object(
            object_dn=application_dn,
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def get_associated_certificate(self, application: 'Union[Config.Object, str]'):
        """
        Args:
            application: :ref:`config_object` or :ref:`dn` of the application object.

        Returns:
            :ref:`config_object` of the certificate object associated to the application object.
        """
        application_dn = self._get_dn(application)
        response = self._api.websdk.Config.Read.post(
            object_dn=application_dn,
            attribute_name=ApplicationBaseAttributes.certificate
        )

        if not response.values:
            return None

        certificate_dn = response.values[0]
        return self._api.websdk.Config.IsValid.post(object_dn=certificate_dn).object

    def _create(self, name: 'str', device: 'Union[Config.Object, str]', description: 'str' = None,
                contacts: 'List[Union[Identity.Identity, str]]' = None,
                approvers: 'List[Union[Identity.Identity, str]]' = None,
                attributes: dict = None, get_if_already_exists: bool = True):
        device_dn = self._get_dn(obj=device)
        if approvers is not None:
            attributes.update({
                ApplicationBaseAttributes.approver: [self._get_prefixed_universal(a) for a in approvers]
            })
        if contacts is not None:
            attributes.update({
                ApplicationBaseAttributes.contact: [self._get_prefixed_universal(c) for c in contacts]
            })
        if description is not None:
            attributes.update({
                ApplicationBaseAttributes.description: description
            })

        return self._config_create(
            name=name,
            parent_folder_dn=device_dn,
            config_class=self._class_name,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

    def _get_stage(self, application: 'Union[Config.Object, str]'):
        application_dn = self._get_dn(application)
        response = self._api.websdk.Config.Read.post(
            object_dn=application_dn,
            attribute_name=ApplicationBaseAttributes.stage
        )

        return int(response.values[0]) if response.values else None

    def get_stage(self, application: 'Union[Config.Object, str]'):
        """
        Args:
            application: :ref:`config_object` or :ref:`dn` of the application object.

        Returns:
            int: The current stage if it exists. Otherwise, returns ``None``.
        """
        self._get_stage(application=application)

    def get_status(self, application: 'Union[Config.Object, str]'):
        """
        Args:
            application: :ref:`config_object` or :ref:`dn` of the application object.

        Returns:
            str: The current processing status of the application object or ``None`` if a status does not exist.
        """
        application_dn = self._get_dn(application)
        response = self._api.websdk.Config.Read.post(
            object_dn=application_dn,
            attribute_name=ApplicationBaseAttributes.status
        )

        return response.values[0] if response.values else None

    def _is_in_error(self, application: 'Union[Config.Object, str]'):
        application_dn = self._get_dn(application)
        response = self._api.websdk.Config.Read.post(
            object_dn=application_dn,
            attribute_name=ApplicationBaseAttributes.in_error
        )

        return bool(response.values[0]) if response.values else False

    def wait_for_installation_to_complete(self, application: 'Union[Config.Object, str]', timeout: int = 60):
        """
        Waits for the application object's "Last Pushed On" attribute to be a date greater than
        or equal to the "Last Renewed On" date on the associated certificate. If the certificate
        has not been recently renewed and is simply being associated to the certificate, either
        clear the "Last Pushed On" date from the application object or use
        :meth:`pytpp.pytpp.features.certificate.Certificate.associate_application` with
        ``push_to_new=True``.

        Args:
            application: :ref:`config_object` or :ref:`dn` of the application object.
            timeout: Timeout in seconds.
        """
        application_dn = self._get_dn(application)
        certificate_dn = self._api.websdk.Config.Read.post(
            object_dn=application_dn,
            attribute_name=ApplicationBaseAttributes.certificate
        )
        if not certificate_dn.values:
            raise UnexpectedValue(
                f'There is no certificate associated to "{application_dn}" in TPP.'
            )
        response = self._api.websdk.Config.Read.post(
            object_dn=certificate_dn.values[0],
            attribute_name=X509CertificateAttributes.last_renewed_on
        )

        if not response.values:
            raise UnexpectedValue(
                f'Cannot validate that the certificate "{certificate_dn}" is installed on the application '
                f'"{application_dn}" as it seems that the certificate has never been renewed.'
            )
        certificate_last_renewed_time = from_date_string(response.values[0])

        def _certificate_is_installed():
            resp = self._api.websdk.Config.Read.post(
                object_dn=application_dn,
                attribute_name=ApplicationBaseAttributes.last_pushed_on
            )

            if not resp.values:
                return False
            application_last_pushed_on = from_date_string(resp.values[0])
            return application_last_pushed_on >= certificate_last_renewed_time

        stage = self._get_stage(application=application)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                if self._is_in_error(application=application):
                    break
                elif not stage:
                    if not _certificate_is_installed():
                        raise UnexpectedValue(
                            f'Expected a certificate to be installed on "{application_dn}", '
                            f'but the application is not in a processing status.'
                        )
                    return
                stage = self._get_stage(application=application)

        raise TimeoutError(
            f'Certificate installation failed on "{application_dn}".\n'
            f'Stage: {stage}\n'
            f'Status: {self.get_status(application=application)}'
        )


@feature('Adaptable Application')
class Adaptable(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.adaptable_app)

    @staticmethod
    def _calculate_hash(script_content: bytes):
        return b64encode(sha256(
            script_content.decode().encode('utf-32-le')
        ).hexdigest().encode()).decode()

    def create(self, name: 'str', device: 'Union[Config.Object, str]', policy_folder: 'Union[Config.Object, str]',
               powershell_script_name: 'str', powershell_script_content: 'bytes', locked: 'bool' = False,
               retry_after_scipt_hash_mismatch: 'bool' = None, description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None,
               secondary_credential: 'Union[Config.Object, str]' = None,
               port: 'int' = None, private_key_credential: 'str' = None, log_debug: 'bool' = None,
               attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            policy_folder: :ref:`config_object` or :ref:`dn` of the folder to write the Adapatble PowerShell script policy.
            powershell_script_name: Name of the PowerShell script.
            powershell_script_content: Content of the PowerShell script in bytes. Use ``open(ps_script, 'rb')``.
            locked: Lock this script on the ``policy_folder``.
            retry_after_scipt_hash_mismatch: When the script is updated fix the related provisioning and discovery errors.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential object.
            secondary_credential: :ref:`config_object` or :ref:`dn` of the supplemental application credential to pass to PowerShell script.
            port: Port number.
            private_key_credential: Optional private key credential.
            log_debug: Enable log debug.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """

        # region Create The Policy Attributes
        policy_folder_dn = self._get_dn(obj=policy_folder)
        if retry_after_scipt_hash_mismatch is True:
            self._api.websdk.Config.WritePolicy.post(
                object_dn=policy_folder_dn,
                class_name=Classes.adaptable_app,
                attribute_name=AdaptableAppAttributes.script_hash_mismatch_error,
                values=[retry_after_scipt_hash_mismatch],
                locked=locked
            ).assert_valid_response()
        self._api.websdk.Config.WritePolicy.post(
            object_dn=policy_folder_dn,
            class_name=Classes.adaptable_app,
            attribute_name=AdaptableAppAttributes.powershell_script,
            values=[powershell_script_name],
            locked=locked
        ).assert_valid_response()
        vault_id = self._api.websdk.SecretStore.Add.post(
            base_64_data=self._calculate_hash(powershell_script_content),
            keyname=KeyNames.software_default,
            vault_type=VaultTypes.blob,
            namespace=Namespaces.config,
            owner=policy_folder_dn
        ).vault_id

        self._api.websdk.Config.WritePolicy.post(
            object_dn=policy_folder_dn,
            class_name=Classes.adaptable_app,
            attribute_name=AdaptableAppAttributes.powershell_script_hash_vault_id,
            values=[vault_id],
            locked=locked
        ).assert_valid_response()
        # endregion Create The Policy Attributes

        app_attrs = {
            ApplicationBaseAttributes.driver_name      : 'appadaptable',
            AdaptableAppAttributes.credential          : self._get_dn(
                application_credential) if application_credential else None,
            AdaptableAppAttributes.log_debug           : int(log_debug),
            AdaptableAppAttributes.pk_credential       : self._get_dn(
                private_key_credential) if private_key_credential else None,
            AdaptableAppAttributes.port                : port,
            AdaptableAppAttributes.secondary_credential: self._get_dn(
                secondary_credential) if secondary_credential else None,
        }
        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name, device=device, contacts=contacts, approvers=approvers, description=description,
            attributes=app_attrs, get_if_already_exists=get_if_already_exists
        )


@feature('Amazon AWS')
class AmazonAWS(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.amazon_app)

    def create(self, name: str, device: 'Union[Config.Object, str]', aws_credential: 'Union[Config.Object, str]',
               description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               issued_by_aws: 'bool' = None, provision_to: 'int' = None, region: 'str' = None,
               iam_install_path: 'str' = None, replace_existing: 'bool' = None, binding_taget: 'Union[str, int]' = None,
               load_balancer_name: 'str' = None, load_balancer_port: 'int' = None, target_group: 'str' = None,
               create_listener: 'bool' = None, cloudfront_distribution_id: 'str' = None, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            aws_credential: :ref:`config_object` or :ref:`dn` of the AWS credential object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            issued_by_aws: The certificate should be issued by AWS Certificate Manager.
            provision_to: ACM or IAM.
            region: AWS region.
            iam_install_path: IAM path for certificate upload.
            replace_existing: Replace the existing store.
            binding_taget: Binding target.
            load_balancer_name: Name of the load balancer.
            load_balancer_port: Port of the load balancer.
            target_group: Default target group.
            create_listener: Create listener.
            cloudfront_distribution_id: CloudFront Distribution ID.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name         : 'appamazon',
            AmazonAppAttributes.aws_credential_dn         : self._get_dn(aws_credential),
            AmazonAppAttributes.issued_by_aws             : {True: "1", False: "0"}.get(issued_by_aws),
            AmazonAppAttributes.provisioning_to           : provision_to,
            AmazonAppAttributes.load_balancer_region_code : region,
            AmazonAppAttributes.install_path              : iam_install_path,
            AmazonAppAttributes.replace_store             : {True: "1", False: "0"}.get(replace_existing),
            AmazonAppAttributes.binding_target            : binding_taget,
            AmazonAppAttributes.load_balancer_name        : load_balancer_name,
            AmazonAppAttributes.load_balancer_port        : load_balancer_port,
            AmazonAppAttributes.create_binding            : {True: "1", False: "0"}.get(create_listener),
            AmazonAppAttributes.target_group              : target_group,
            AmazonAppAttributes.cloudfront_distribution_id: cloudfront_distribution_id
        }
        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('Apache')
class Apache(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.apache)

    def create(self, name: str, device: 'Union[Config.Object, str]', private_key_file: 'str', certificate_file: 'str',
               description: 'str' = None, contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, port: 'int' = None,
               private_key_location: 'str' = None, client_tools_path: 'str' = None,
               protection_type: 'str' = None, softcard_identifier: 'str' = None, ocs_identifier: 'str' = None,
               partition_password_credential: 'Union[Config.Object, str]' = None,
               private_key_credential: 'Union[Config.Object, str]' = None,
               certificate_chain_file: 'str' = None, overwrite_existing_chain: 'bool' = None, owner: 'str' = None,
               owner_permissions: 'str' = None, group: 'str' = None, group_permissions: 'str' = None,
               attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            private_key_file: File location to place the private key file.
            certificate_file: File location to place the certificate file.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port.
            private_key_location: Remote generation setting.
            client_tools_path: HSM client tools path.
            protection_type: HSM protection type.
            softcard_identifier: Softcard label.
            ocs_identifier: OCS label.
            partition_password_credential: :ref:`config_object` or :ref:`dn` of OCS pin or softcard passphrase credential.
            private_key_credential: :ref:`config_object` or :ref:`dn` of private key credential.
            certificate_chain_file: File location to place the certificate chain file.
            overwrite_existing_chain: Overwirte the existing chain.
            owner: File user owner.
            owner_permissions: File permissions assigned to the user owner.
            group: File group owner.
            group_permissions: File permissions assigned to the group owner.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name           : 'appapache',
            ApacheAttributes.credential                     : self._get_dn(
                application_credential) if application_credential else None,
            ApacheAttributes.port                           : port,
            ApacheAttributes.private_key_location           : private_key_location,
            ApacheAttributes.client_tools_path              : client_tools_path,
            ApacheAttributes.protection_type                : protection_type,
            ApacheAttributes.softcard_identifier            : softcard_identifier,
            ApacheAttributes.ocs_identifier                 : ocs_identifier,
            ApacheAttributes.partition_password_credential  : self._get_dn(
                partition_password_credential) if partition_password_credential else None,
            ApacheAttributes.private_key_file               : private_key_file,
            ApacheAttributes.private_key_password_credential: self._get_dn(
                private_key_credential) if private_key_credential else None,
            ApacheAttributes.certificate_file               : certificate_file,
            ApacheAttributes.certificate_chain_file         : certificate_chain_file,
            ApacheAttributes.overwrite_existing_chain       : {True: "1", False: "0"}.get(overwrite_existing_chain),
        }
        if owner or group:
            app_attrs.update({
                ApacheAttributes.file_permissions_enabled: "1",
                ApacheAttributes.file_owner_user         : owner,
                ApacheAttributes.file_permissions_user   : owner_permissions,
                ApacheAttributes.file_owner_group        : group,
                ApacheAttributes.file_permissions_group  : group_permissions,
            })

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('Azure Key Vault')
class AzureKeyVault(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.azure_key_vault)

    def create(self, name: str, device: 'Union[Config.Object, str]', application_id: 'str',
               certificate_credential: 'Union[Config.Object, str]', azure_key_vault_name: 'str',
               description: 'str' = None, contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None, certificate_name: 'str' = None,
               private_key_exportable: 'bool' = None, web_application_name: 'str' = None,
               create_new_binding: 'bool' = None, create_san_dns_bindings: 'bool' = None, ssl_type: 'int' = None,
               binding_hostnames: 'List[str]' = None, attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            application_id: Application ID.
            certificate_credential: :ref:`config_object` or :ref:`dn` of the certificate credential.
            azure_key_vault_name:  Azure Key Vault name.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            certificate_name: Certificate name.
            private_key_exportable: Mark the private key as exportable.
            web_application_name: Name of the web application.
            create_new_binding: Create new certificate binding.
            create_san_dns_bindings: Create SAN DNS binding.
            ssl_type: SNI or IP Based.
            binding_hostnames: Binding hostnames.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name         : 'appazurekeyvault',
            AzureKeyVaultAttributes.client_id             : application_id,
            AzureKeyVaultAttributes.certificate_credential: self._get_dn(certificate_credential),
            AzureKeyVaultAttributes.vault_name            : azure_key_vault_name,
            AzureKeyVaultAttributes.certificate_name      : certificate_name,
            AzureKeyVaultAttributes.non_exportable        : {True: "0", False: "1"}.get(private_key_exportable)
        }
        if web_application_name:
            app_attrs.update({
                AzureKeyVaultAttributes.update_web_app         : "0",
                AzureKeyVaultAttributes.web_app_name           : web_application_name,
                AzureKeyVaultAttributes.create_binding         : {True: "0", False: "1"}.get(create_new_binding),
                AzureKeyVaultAttributes.create_san_dns_bindings: {True: "0", False: "1"}.get(create_san_dns_bindings),
                AzureKeyVaultAttributes.binding_ssl_type       : ssl_type,
                AzureKeyVaultAttributes.binding_hostnames      : binding_hostnames
            })
        else:
            app_attrs.update({
                AzureKeyVaultAttributes.update_web_app: "1"
            })

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('Basic Application')
class Basic(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.basic)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name: 'appbasic'
        }
        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )

    def convert(self, basic_application: 'Union[Config.Object, str]', new_class_name: str, attributes: dict = None):
        """
        Converts the Basic application to another application class type. If attributes are given,
        then those attributes will apply to the new application once conversion is complete.

        Args:
            basic_application: :ref:`config_object` or :ref:`dn` of the Basic application.
            new_class_name: Application class name of the new application object.
            attributes: Attributes pertaining to the new application object.

        Returns:
            :ref:`config_object` of the application.
        """
        basic_application_dn = self._get_dn(basic_application)
        result = self._api.websdk.Config.MutateObject.post(
            object_dn=basic_application_dn,
            class_name=str(new_class_name)
        )
        result.assert_valid_response()

        if attributes:
            attributes = {k: ([str(v)] if not isinstance(v, list) else v) for k, v in attributes.items()}
            result = self._api.websdk.Config.Write.post(
                object_dn=basic_application_dn,
                attribute_data=self._name_value_list(attributes, keep_list_values=True)
            )
            result.assert_valid_response()

        new_object = self._api.websdk.Config.IsValid.post(object_dn=basic_application_dn).object
        if new_object.type_name != new_class_name:
            raise UnexpectedValue(
                f'Unable to convert Basic App "{basic_application_dn}" to {new_class_name}. '
                f'Its current class name is {new_object.type_name}.'
            )
        return new_object


@feature('Blue Coat SSLVA')
class BlueCoatSSLVA(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.bluecoat_sslva)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None,
               port: 'int' = None, device_certificate: 'bool' = None, replace_existing: 'bool' = None,
               install_chain: 'bool' = None,
               create_lists: 'bool' = None, known_certificates_with_keys_lists: 'List[str]' = None,
               attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port number.
            device_certificate: The key certificate is a device certificate.
            replace_existing: Replace existing certificate.
            install_chain: Install the certificate chain.
            create_lists: Create lists.
            known_certificates_with_keys_lists: Known certificates with keys list(s).
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name     : 'appBlueCoat',
            BlueCoatSSLVAAttributes.credential        : self._get_dn(application_credential) if application_credential else None,
            BlueCoatSSLVAAttributes.port              : port,
            BlueCoatSSLVAAttributes.device_certificate: {True: "1", False: "0"}.get(device_certificate),
            BlueCoatSSLVAAttributes.replace_store     : {True: "1", False: "0"}.get(replace_existing),
            BlueCoatSSLVAAttributes.certificate_only  : {True: "1", False: "0"}.get(install_chain),
            BlueCoatSSLVAAttributes.create_lists      : {True: "1", False: "0"}.get(create_lists),
            BlueCoatSSLVAAttributes.certificate_label : known_certificates_with_keys_lists
        }
        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('CAPI')
class CAPI(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.capi)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, winrm_port: 'int' = None,
               private_key_location: 'str' = None, key_label: 'str' = None, friendly_name: 'str' = None,
               exportable: 'bool' = None,
               private_key_trustee: 'str' = None, web_site_name: 'str' = None, binding_ip_address: 'str' = None,
               binding_port: 'int' = None,
               binding_hostname: 'str' = None, create_binding: 'bool' = None, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            winrm_port: WinRM connection port.
            private_key_location: Remote key generation setting for generating the private key.
            key_label: Private key label. Only applies if using remote key generation.
            friendly_name: Friendly name.
            exportable: Private key is exportable.
            private_key_trustee: Private key trustee.
            web_site_name: Name of the web site.
            binding_ip_address: Binding IP Address.
            binding_port: Binding port.
            binding_hostname: Binding hostname.
            create_binding: Create the binding.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name: 'appcapi',
            CAPIAttributes.credential            : self._get_dn(application_credential) if application_credential else None,
            CAPIAttributes.port                  : winrm_port,
            CAPIAttributes.private_key_location  : private_key_location,
            CAPIAttributes.private_key_label     : key_label,
            CAPIAttributes.friendly_name         : friendly_name,
            CAPIAttributes.non_exportable        : {True: "0", False: "1"}.get(exportable),
            CAPIAttributes.private_key_trustee   : private_key_trustee,
        }
        if web_site_name:
            app_attrs.update({
                CAPIAttributes.update_iis        : "1",
                CAPIAttributes.web_site_name     : web_site_name,
                CAPIAttributes.binding_ip_address: binding_ip_address,
                CAPIAttributes.binding_port      : binding_port,
                CAPIAttributes.hostname          : binding_hostname,
                CAPIAttributes.create_binding    : {True: "1", False: "0"}.get(create_binding),
            })
        else:
            app_attrs.update({
                CAPIAttributes.update_iis: "0"
            })

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('Citrix NetScaler')
class CitrixNetScaler(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.netscaler)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, port: 'int' = None,
               install_certificate_chain: 'bool' = None,
               use_fips: 'bool' = None, private_key_credential: 'Union[Config.Object, str]' = None,
               import_only: 'bool' = None,
               subfolder_relative_path: 'str' = None, certificate_binding: 'str' = None,
               virtual_server_name: 'str' = None,
               sni_certificate: 'bool' = None, attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port.
            install_certificate_chain: Install the certificate chain.
            use_fips: Use FIPS.
            private_key_credential: :ref:`config_object` or :ref:`dn` of the private key credential.
            import_only: Import only.
            subfolder_relative_path: Subfolder relative path.
            certificate_binding: Certificate binding.
            virtual_server_name: Virtual server name, service name, or service group name.
            sni_certificate: SNI certificate.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name              : 'appnetscaler',
            NetScalerAttributes.credential                     : self._get_dn(application_credential) if application_credential else None,
            NetScalerAttributes.port                           : port,
            NetScalerAttributes.chain_cert                     : {True: "1", False: "0"}.get(install_certificate_chain),
            NetScalerAttributes.fips_key                       : {True: "1", False: "0"}.get(use_fips),
            NetScalerAttributes.private_key_password_credential: self._get_dn(private_key_credential) if private_key_credential else None,
            NetScalerAttributes.import_only                    : {True: "1", False: "0"}.get(import_only),
            NetScalerAttributes.install_path                   : subfolder_relative_path,
            NetScalerAttributes.ssl_object_type                : certificate_binding,
            NetScalerAttributes.virtual_server_name            : virtual_server_name,
            NetScalerAttributes.sni_certificate                : {True: "1", False: "0"}.get(sni_certificate),
        }

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('Connect:Direct')
class ConnectDirect(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.connectdirect)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, api_protocol: 'str' = None,
               port: 'int' = None, node_name: 'str' = None, install_chain: 'bool' = None,
               key_certificate_alias: 'str' = None, attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            api_protocol: API protocol.
            port: Connection port.
            node_name: Node name.
            install_chain: Install certificate chain.
            key_certificate_alias: Key certificate alias.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name    : 'appConnectDirect',
            ConnectDirectAttributes.credential       : self._get_dn(application_credential) if application_credential else None,
            ConnectDirectAttributes.protocol         : api_protocol,
            ConnectDirectAttributes.port             : port,
            ConnectDirectAttributes.node_name        : node_name,
            ConnectDirectAttributes.certificate_only : {True: "1", False: "0"}.get(install_chain),
            ConnectDirectAttributes.certificate_label: key_certificate_alias
        }

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('F5 Authentication Bundle')
class F5AuthenticationBundle(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.f5_authentication_bundle)

    def create(self, name: str, device: 'Union[Config.Object, str]', bundle_file_name: str, description: 'str' = None,
               certifictes_to_use: 'List[Union[Config.Object, str]]' = None, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            bundle_file_name: Filename of the certificate bundle.
            description: Description for the application object.
            certifictes_to_use: List of  :ref:`config_object` or :ref:`dn` of the certificates to use.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            F5AuthenticationBundleAttributes.advanced_settings_bundle_name: bundle_file_name,
            F5AuthenticationBundleAttributes.description                  : description,
            F5AuthenticationBundleAttributes.certificates                 : [self._get_dn(c) for c in
                                                                             certifictes_to_use] if certifictes_to_use else None,
        }

        if attributes:
            app_attrs.update(attributes)

        return self._config_create(
            name=name,
            parent_folder_dn=self._get_dn(device),
            config_class=Classes.f5_authentication_bundle,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('F5 LTM Advanced')
class F5LTMAdvanced(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.f5_ltm_advanced)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, https_port: 'int' = None,
               ssh_port: 'int' = None,
               device_certificate: 'bool' = None, provisioning_mode: 'int' = None,
               certificate_and_key_file: 'str' = None,
               private_key_credential: 'Union[Config.Object, str]' = None, force_profile_update: 'bool' = None,
               install_chain: 'bool' = None, bundle_certificate: 'bool' = None, overwrite_chain_file: 'bool' = None,
               ca_chain_file: 'str' = None, use_fips: 'bool' = None, overwrite_certificate_and_key: 'bool' = None,
               delete_previous_cert_and_key: 'bool' = None, provisioning_target: 'str' = None,
               config_sync: 'bool' = None,
               ssl_profile: 'str' = None, ssl_profile_type: 'str' = None, parent_ssl_profile: 'str' = None,
               ssl_partition: 'str' = None, sni_server_name: 'str' = None, sni_default: 'bool' = None,
               virtual_server: 'str' = None,
               virtual_server_partition: 'str' = None, use_advanced_settings: 'bool' = None,
               client_certificate_requirement: 'str' = None,
               server_certificate_requirement: 'str' = None, frequency: 'str' = None,
               chain_traversal_depth: 'int' = None,
               certificate_bundle: 'Union[Config.Object, str]' = None, authentication_name: 'str' = None,
               attributes: dict = None, get_if_already_exists: bool = True):
        """
        Creates a F5 LTM Advanced application object.

        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            https_port: HTTPS port number.
            ssh_port: SSH port number.
            device_certificate: The certificate is a device certificate.
            provisioning_mode: Provisioning mode.
            certificate_and_key_file: Certificate and key file.
            private_key_credential: :ref:`config_object` or :ref:`dn` of the private key credential.
            force_profile_update: Force profile update.
            install_chain: Install the certificate chain.
            bundle_certificate: Bundle certificate.
            overwrite_chain_file: Overwrite the chain file.
            ca_chain_file: CA Chain file.
            use_fips: Use FIPS.
            overwrite_certificate_and_key: Overwrite certificate an key.
            delete_previous_cert_and_key: Delete old certificate and key.
            provisioning_target: Provisioning target for high availability.
            config_sync: Config sync.
            ssl_profile: SSL profile name.
            ssl_profile_type: SSL profile type.
            parent_ssl_profile: Parent SSL profile name.
            ssl_partition: SSL partition.
            sni_server_name: SNI server name.
            sni_default: SNI default.
            virtual_server: Virtual server name.
            virtual_server_partition: Virtual server partition.
            use_advanced_settings: Must be set if using advanced options.
            client_certificate_requirement: Require/request/ignore.
            server_certificate_requirement: Require/ignore.
            frequency: Once or Always.
            chain_traversal_depth: Chain traversal depth.
            certificate_bundle: :ref:`config_object` or :ref:`dn` of the certificate bundle.
            authentication_name: Authentication name.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name                    : 'appf5ltmadvanced',
            F5LTMAdvancedAttributes.credential                       : self._get_dn(application_credential) if application_credential else None,
            F5LTMAdvancedAttributes.port                             : https_port,
            F5LTMAdvancedAttributes.ssh_port                         : ssh_port,
            F5LTMAdvancedAttributes.device_certificate               : {True: "1", False: "0"}.get(device_certificate),
            F5LTMAdvancedAttributes.use_basic_provisioning           : provisioning_mode,
            F5LTMAdvancedAttributes.certificate_name                 : certificate_and_key_file,
            F5LTMAdvancedAttributes.private_key_password_credential  : self._get_dn(private_key_credential) if private_key_credential else None,
            F5LTMAdvancedAttributes.force_profile_update             : {True: "1", False: "0"}.get(force_profile_update),
            F5LTMAdvancedAttributes.install_chain_file               : {True: "1", False: "0"}.get(install_chain),
            F5LTMAdvancedAttributes.bundle_certificate               : {True: "1", False: "0"}.get(bundle_certificate),
            F5LTMAdvancedAttributes.overwrite_existing_chain         : {True: "1", False: "0"}.get(overwrite_chain_file),
            F5LTMAdvancedAttributes.certificate_chain_name           : ca_chain_file,
            F5LTMAdvancedAttributes.fips_key                         : {True: "1", False: "0"}.get(use_fips),
            F5LTMAdvancedAttributes.overwrite_certificate            : {True: "1", False: "0"}.get(overwrite_certificate_and_key),
            F5LTMAdvancedAttributes.delete_previous_cert_and_key     : {True: "1", False: "0"}.get(delete_previous_cert_and_key),
            F5LTMAdvancedAttributes.provisioning_to                  : provisioning_target,
            F5LTMAdvancedAttributes.config_sync                      : {True: "1", False: "0"}.get(config_sync),
            F5LTMAdvancedAttributes.ssl_profile_name                 : ssl_profile,
            F5LTMAdvancedAttributes.ssl_profile_type                 : ssl_profile_type,
            F5LTMAdvancedAttributes.parent_ssl_profile_name          : parent_ssl_profile,
            F5LTMAdvancedAttributes.partition                        : ssl_partition,
            F5LTMAdvancedAttributes.sni_server_name                  : sni_server_name,
            F5LTMAdvancedAttributes.sni_default                      : {True: "1", False: "0"}.get(sni_default),
            F5LTMAdvancedAttributes.virtual_server_name              : virtual_server,
            F5LTMAdvancedAttributes.virtual_server_partition         : virtual_server_partition,
            F5LTMAdvancedAttributes.use_advanced_settings            : {True: "1", False: "0"}.get(use_advanced_settings),
            F5LTMAdvancedAttributes.client_authentication_certificate: client_certificate_requirement,
            F5LTMAdvancedAttributes.server_authentication_certificate: server_certificate_requirement,
            F5LTMAdvancedAttributes.authentication_frequency         : frequency,
            F5LTMAdvancedAttributes.chain_traversal_depth            : chain_traversal_depth,
            F5LTMAdvancedAttributes.bundle_certificate_collection    : self._get_dn(certificate_bundle) if certificate_bundle else None,
            F5LTMAdvancedAttributes.server_authentication_name       : authentication_name,
        }

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('Google Cloud Load Balancer')
class GoogleCloudLoadBalancer(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.google_cloud_app)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               google_credential: 'Union[Config.Object, str]' = None, target_proxy_type: 'str' = None,
               target_proxy_name: 'str' = None, target_resource: 'str' = None, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            google_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            target_proxy_type: Target proxy type.
            target_proxy_name: Target proxy name.
            target_resource: Target resource.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name     : 'appgooglecloudloadbalancer',
            GoogleCloudAppAttributes.credential       : self._get_dn(google_credential) if google_credential else None,
            GoogleCloudAppAttributes.target_proxy_type: target_proxy_type,
            GoogleCloudAppAttributes.target_proxy_name: target_proxy_name,
            GoogleCloudAppAttributes.target_resource  : target_resource
        }

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('IBM DataPower')
class IBMDataPower(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.datapower)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, port: 'int' = None, xml_port: 'int' = None,
               basic_provisioning_mode: 'bool' = None, crypto_certificate: 'str' = None, crypto_key: 'str' = None,
               application_domain: 'str' = None, associate_to_profile: 'bool' = None, credential_type: 'str' = None,
               profile_type: 'str' = None, crypto_profile_name: 'str' = None, ssl_profile_name: 'str' = None,
               certificate_folder: 'str' = None, install_certificate_chain: 'bool' = None,
               private_key_password_credential: 'Union[Config.Object, str]' = None, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port.
            xml_port: XML connection port.
            basic_provisioning_mode: Use basic provisioning mode if ``True`` or advanced if ``False``.
            crypto_certificate: Crypto Certificate name.
            crypto_key: Crypto Private Key name.
            application_domain: Application domain.
            associate_to_profile: Associate to profile.
            credential_type: Credential type.
            profile_type: Profile type.
            crypto_profile_name: Crypto profile name.
            ssl_profile_name: SSL profile name.
            certificate_folder: Certificate folder.
            install_certificate_chain: Install the certficate chain.
            private_key_password_credential: :ref:`config_object` or :ref:`dn` of the private key password credential.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name              : 'appdatapower',
            DataPowerAttributes.credential                     : self._get_dn(
                application_credential) if application_credential else None,
            DataPowerAttributes.port                           : port,
            DataPowerAttributes.xml_port                       : xml_port,
            DataPowerAttributes.use_basic_provisioning         : {True: "2", False: "1"}.get(basic_provisioning_mode),
            DataPowerAttributes.certificate_name               : crypto_certificate,
            DataPowerAttributes.private_key_name               : crypto_key,
            DataPowerAttributes.application_domain             : application_domain,
            DataPowerAttributes.associate_to_cp                : {True: "1", False: "2"}.get(associate_to_profile),
            DataPowerAttributes.credential_type                : credential_type,
            DataPowerAttributes.ssl_profile_type               : profile_type,
            DataPowerAttributes.crypto_profile                 : crypto_profile_name,
            DataPowerAttributes.ssl_proxy_profile              : ssl_profile_name,
            DataPowerAttributes.folder                         : certificate_folder,
            DataPowerAttributes.chain_cert                     : {True: "1", False: "0"}.get(install_certificate_chain),
            DataPowerAttributes.private_key_password_credential: self._get_dn(
                private_key_password_credential) if private_key_password_credential else None,
        }

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('IBM GSK')
class IBMGSK(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.gsk)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, port: 'int' = None, version: 'str' = None,
               gsk_utility_path: 'str' = None, java_home_path: 'str' = None, key_store_path: 'str' = None,
               key_store_credential: 'Union[Config.Object, str]' = None, create: 'bool' = None,
               replace_existing: 'bool' = None,
               certificate_label: 'str' = None, reuse_label: 'bool' = None, use_fips: 'bool' = None,
               password_validity: 'int' = None,
               stash_password: 'bool' = None, default_certificate: 'bool' = None, owner: 'str' = None,
               owner_permissions: 'str' = None, group: 'str' = None, group_permissions: 'str' = None,
               attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port.
            version: GSK version.
            gsk_utility_path: GSK utility path.
            java_home_path: JAVA_HOME path.
            key_store_path: Key store path.
            key_store_credential: :ref:`config_object` or :ref:`dn` of the key store credential.
            create: Create store.
            replace_existing: Replace existing store.
            certificate_label: Certificate label.
            reuse_label: Reuse certificate label.
            use_fips: Use FIPS.
            password_validity: Password validity in number of days.
            stash_password: Stash password.
            default_certificate: Default certificate.
            owner: File user owner.
            owner_permissions: File permissions assigned to the user owner.
            group: File group owner.
            group_permissions: File permissions assigned to the group owner.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name: 'appgsk',
            GSKAttributes.credential             : self._get_dn(
                application_credential) if application_credential else None,
            GSKAttributes.port                   : port,
            GSKAttributes.version                : version,
            GSKAttributes.utility_path           : gsk_utility_path,
            GSKAttributes.java_home_path         : java_home_path,
            GSKAttributes.key_store              : key_store_path,
            GSKAttributes.key_store_credential   : self._get_dn(key_store_credential) if key_store_credential else None,
            GSKAttributes.create_store           : {True: "1", False: "0"}.get(create),
            GSKAttributes.replace_store          : {True: "1", False: "0"}.get(replace_existing),
            GSKAttributes.certificate_label      : certificate_label,
            GSKAttributes.recycle_alias          : {True: "1", False: "0"}.get(reuse_label),
            GSKAttributes.fips_key               : {True: "1", False: "0"}.get(use_fips),
            GSKAttributes.password_expire_days   : password_validity,
            GSKAttributes.stash_password         : {True: "1", False: "0"}.get(stash_password),
            GSKAttributes.default_cert           : {True: "1", False: "0"}.get(default_certificate),
        }
        if owner or group:
            app_attrs.update({
                GSKAttributes.file_permissions_enabled: "1",
                GSKAttributes.file_owner_user         : owner,
                GSKAttributes.file_permissions_user   : owner_permissions,
                GSKAttributes.file_owner_group        : group,
                GSKAttributes.file_permissions_group  : group_permissions
            })
        else:
            app_attrs.update({
                GSKAttributes.file_permissions_enabled: "0"
            })

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('Imperva MX')
class ImpervaMX(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.imperva_mx)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, port: 'int' = None,
               user_credential: 'Union[Config.Object, str]' = None, ssl_key_tool_path: 'str' = None, site: 'str' = None,
               server_group: 'str' = None, service: 'str' = None, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port.
            user_credential: :ref:`config_object` or :ref:`dn` of the user credential.
            ssl_key_tool_path: SSL key tool path.
            site: Site.
            server_group: Server group.
            service: Service.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name  : 'appimpervamx',
            ImpervaMXAttributes.credential         : self._get_dn(
                application_credential) if application_credential else None,
            ImpervaMXAttributes.port               : port,
            ImpervaMXAttributes.username_credential: self._get_dn(user_credential) if user_credential else None,
            ImpervaMXAttributes.utility_path       : ssl_key_tool_path,
            ImpervaMXAttributes.site               : site,
            ImpervaMXAttributes.server_group       : server_group,
            ImpervaMXAttributes.service            : service
        }

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('JKS')
class JKS(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.jks)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, port: 'int' = None,
               private_key_location: 'str' = None,
               slot_number: 'int' = None, java_vendor: 'str' = None, protection_type: 'str' = None,
               softcard_identifier: 'str' = None,
               keytool_path: 'str' = None, version: 'str' = None, store_type: 'str' = None, keystore_path: 'str' = None,
               keystore_credential: 'Union[Config.Object, str]' = None,
               private_key_credential: 'Union[Config.Object, str]' = None,
               create: 'bool' = None, replace_existing: 'bool' = None, certificate_alias: 'str' = None,
               reuse_alias: 'bool' = None,
               owner: 'str' = None, owner_permissions: 'str' = None, group: 'str' = None,
               group_permissions: 'str' = None,
               attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port.
            private_key_location: Remote generation setting.
            slot_number: Slot number.
            java_vendor: Java vendor.
            protection_type: Remote generation protection type.
            softcard_identifier: Softcard identifier.
            keytool_path: Keytool path.
            version: Java version.
            store_type: Store type.
            keystore_path: Key store path.
            keystore_credential: :ref:`config_object` or :ref:`dn` of the key store credential.
            private_key_credential: :ref:`config_object` or :ref:`dn` of the private key credential.
            create: Create store.
            replace_existing: Replace existing store.
            certificate_alias: Certificate alias.
            reuse_alias: Resuse certificate alias.
            owner: File user owner.
            owner_permissions: File permissions assigned to the user owner.
            group: File group owner.
            group_permissions: File permissions assigned to the group owner.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name        : 'appjks',
            JKSAttributes.credential                     : self._get_dn(
                application_credential) if application_credential else None,
            JKSAttributes.port                           : port,
            JKSAttributes.private_key_location           : private_key_location,
            JKSAttributes.slot_number                    : slot_number,
            JKSAttributes.java_vendor                    : java_vendor,
            JKSAttributes.protection_type                : protection_type,
            JKSAttributes.softcard_identifier            : softcard_identifier,
            JKSAttributes.keytool_path                   : keytool_path,
            JKSAttributes.version                        : version,
            JKSAttributes.store_type                     : store_type,
            JKSAttributes.key_store                      : keystore_path,
            JKSAttributes.key_store_credential           : self._get_dn(
                keystore_credential) if keystore_credential else None,
            JKSAttributes.private_key_password_credential: self._get_dn(
                private_key_credential) if private_key_credential else None,
            JKSAttributes.create_store                   : {True: "1", False: "0"}.get(create),
            JKSAttributes.replace_store                  : {True: "1", False: "0"}.get(replace_existing),
            JKSAttributes.certificate_label              : certificate_alias,
            JKSAttributes.recycle_alias                  : {True: "1", False: "0"}.get(reuse_alias)
        }
        if owner or group:
            app_attrs.update({
                JKSAttributes.file_permissions_enabled: "1",
                JKSAttributes.file_owner_user         : owner,
                JKSAttributes.file_permissions_user   : owner_permissions,
                JKSAttributes.file_owner_group        : group,
                JKSAttributes.file_permissions_group  : group_permissions
            })
        else:
            app_attrs.update({
                JKSAttributes.file_permissions_enabled: "0"
            })

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('Oracle iPlanet')
class OracleIPlanet(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.iplanet)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, port: 'int' = None,
               certificate_database_type: 'str' = None, certificate_database_path: 'str' = None,
               certificate_database_credential: 'Union[Config.Object, str]' = None,
               certificate_database_prefix: 'str' = None,
               create: 'bool' = None, replace_existing: 'bool' = None, certutil_path: 'str' = None,
               pk12util_path: 'str' = None,
               certificate_alias: 'str' = None, owner: 'str' = None, owner_permissions: 'str' = None,
               group: 'str' = None,
               group_permissions: 'str' = None, attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port.
            certificate_database_type: Certificate database type.
            certificate_database_path: Certificate database path.
            certificate_database_credential: :ref:`config_object` or :ref:`dn` of the ccertificate database credentiaL.
            certificate_database_prefix: Certificate database prefix.
            create: Create store.
            replace_existing: Replace existing store.
            certutil_path: Certutil path.
            pk12util_path: Pk12util path.
            certificate_alias: Certificate alias.
            owner: File user owner.
            owner_permissions: File permissions assigned to the user owner.
            group: File group owner.
            group_permissions: File permissions assigned to the group owner.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name : 'appiplanet',
            iPlanetAttributes.credential          : self._get_dn(
                application_credential) if application_credential else None,
            iPlanetAttributes.port                : port,
            iPlanetAttributes.database_type       : certificate_database_type,
            iPlanetAttributes.key_store           : certificate_database_path,
            iPlanetAttributes.key_store_credential: self._get_dn(
                certificate_database_credential) if certificate_database_credential else None,
            iPlanetAttributes.database_prefix     : certificate_database_prefix,
            iPlanetAttributes.create_store        : {True: "1", False: "0"}.get(create),
            iPlanetAttributes.replace_store       : {True: "1", False: "0"}.get(replace_existing),
            iPlanetAttributes.certutil_path       : certutil_path,
            iPlanetAttributes.pk12util_path       : pk12util_path,
            iPlanetAttributes.alias               : certificate_alias,
        }
        if owner or group:
            app_attrs.update({
                iPlanetAttributes.file_permissions_enabled: "1",
                iPlanetAttributes.file_owner_user         : owner,
                iPlanetAttributes.file_permissions_user   : owner_permissions,
                iPlanetAttributes.file_owner_group        : group,
                iPlanetAttributes.file_permissions_group  : group_permissions
            })
        else:
            app_attrs.update({
                iPlanetAttributes.file_permissions_enabled: "0"
            })

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('Palo Alto Network FW')
class PaloAltoNetworkFW(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.palo_alto_network_fw)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, port: 'int' = None,
               provision_certificate_only: 'bool' = None, private_key_password: 'Union[Config.Object, str]' = None,
               install_chain: 'bool' = None, replace_certificate: 'bool' = None,
               decryption_policy_rule_name: 'str' = None,
               create_decryption_policy_rule: 'bool' = None, decryption_profile_name: 'str' = None,
               destination_addresses: 'List[str]' = None, lock_config: 'bool' = None,
               attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port.
            provision_certificate_only: If ``False``, also provision the private key.
            private_key_password: :ref:`config_object` or :ref:`dn` of the private key password.
            install_chain: Insatll the certifcate chain.
            replace_certificate: Replace certificate.
            decryption_policy_rule_name: Decryption policy rule name.
            create_decryption_policy_rule: Create decryption policy rule.
            decryption_profile_name: Decryption profile name.
            destination_addresses: Destination addresses.
            lock_config: Lock config.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name                      : 'appPaloAlto',
            PaloAltoNetworkFWAttributes.credential                     : self._get_dn(
                application_credential) if application_credential else None,
            PaloAltoNetworkFWAttributes.port                           : port,
            PaloAltoNetworkFWAttributes.certificate_only               : {True: "1", False: "2"}.get(
                provision_certificate_only),
            PaloAltoNetworkFWAttributes.private_key_password_credential: self._get_dn(
                private_key_password) if private_key_password else None,
            PaloAltoNetworkFWAttributes.chain_cert                     : {True: "1", False: "0"}.get(install_chain),
            PaloAltoNetworkFWAttributes.replace_store                  : {True: "1", False: "0"}.get(
                replace_certificate),
            PaloAltoNetworkFWAttributes.decryption_policy              : decryption_policy_rule_name,
            PaloAltoNetworkFWAttributes.create_decryption_policy       : {True: "1", False: "0"}.get(
                create_decryption_policy_rule),
            PaloAltoNetworkFWAttributes.decryption_profile             : decryption_profile_name,
            PaloAltoNetworkFWAttributes.decryption_destinations        : destination_addresses,
            PaloAltoNetworkFWAttributes.lock_config                    : {True: "1", False: "0"}.get(lock_config)
        }

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('PEM')
class PEM(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.pem)

    def create(self, name: str, device: 'Union[Config.Object, str]', private_key_file: 'str', certificate_file: 'str',
               description: 'str' = None, contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, port: 'int' = None,
               private_key_credential: 'Union[Config.Object, str]' = None, certificate_chain_file: 'str' = None,
               overwrite_existing_chain: 'bool' = None, owner: 'str' = None, owner_permissions: 'str' = None,
               group: 'str' = None, group_permissions: 'str' = None, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            private_key_file: File location to place the private key file.
            certificate_file: File location to place the certificate file.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port.
            private_key_credential: :ref:`config_object` or :ref:`dn` of private key credential.
            certificate_chain_file: File location to place the certificate chain file.
            overwrite_existing_chain: Overwirte the existing chain.
            owner: File user owner.
            owner_permissions: File permissions assigned to the user owner.
            group: File group owner.
            group_permissions: File permissions assigned to the group owner.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name           : 'appPem',
            ApacheAttributes.credential                     : self._get_dn(
                application_credential) if application_credential else None,
            ApacheAttributes.port                           : port,
            ApacheAttributes.private_key_file               : private_key_file,
            ApacheAttributes.private_key_password_credential: self._get_dn(
                private_key_credential) if private_key_credential else None,
            ApacheAttributes.certificate_file               : certificate_file,
            ApacheAttributes.certificate_chain_file         : certificate_chain_file,
            ApacheAttributes.overwrite_existing_chain       : {True: "1", False: "0"}.get(overwrite_existing_chain),
        }
        if owner or group:
            app_attrs.update({
                ApacheAttributes.file_permissions_enabled: "1",
                ApacheAttributes.file_owner_user         : owner,
                ApacheAttributes.file_permissions_user   : owner_permissions,
                ApacheAttributes.file_owner_group        : group,
                ApacheAttributes.file_permissions_group  : group_permissions,
            })

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('PKCS11')
class PKCS11(_ApplicationBase):
    """
    .. note::
        The PKCS #11 VSE must be installed in order to use this driver.
    """
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.pkcs11)

    def create(self, name: str, device: 'Union[Config.Object, str]', connection_method: 'str', port: 'int',
               protection_type: 'str', token_identifier: 'str', token_pin: 'Union[Config.Object, str]',
               label_format: 'str',
               use_case: 'str', import_certificate_into_hsm: 'str', distribution_directory: 'str', cryptoki_file: 'str',
               openssl_config_file: 'str', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None,
               reverse_subject_dn: 'bool' = None, embed_sans_in_csr: 'bool' = None, requested_label: 'str' = None,
               client_tools_directory: 'str' = None, openssl_directory: 'str' = None, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            connection_method: WinRM or SSH.
            port: Connection port.
            protection_type: HSM protection type.
            token_identifier: Token/Slot identifier.
            token_pin: :ref:`config_object` or :ref:`dn` of the token/slot pin, or passphrase, credential.
            label_format: Label format.
            use_case: Use case.
            import_certificate_into_hsm: Where to import the certificate.
            distribution_directory: Distribution directory.
            cryptoki_file: Cryptoki file path.
            openssl_config_file: OpenSSL config file path.
            reverse_subject_dn: Reverse the subject :ref:`dn`.
            embed_sans_in_csr: Embed SANs in CSR.
            requested_label: Requested key label.
            client_tools_directory: Client tools directory.
            openssl_directory: OpenSSL directory.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name     : 'apppkcs11',
            PKCS11Attributes.credential               : self._get_dn(
                application_credential) if application_credential else None,
            PKCS11Attributes.connection_method        : connection_method,
            PKCS11Attributes.port                     : port,
            PKCS11Attributes.hsm_protection_type      : protection_type,
            PKCS11Attributes.hsm_token_label          : token_identifier,
            PKCS11Attributes.hsm_token_password       : self._get_dn(token_pin),
            PKCS11Attributes.hsm_cka_label_format     : label_format,
            PKCS11Attributes.hsm_requested_cka_label  : requested_label,
            PKCS11Attributes.hsm_requested_usecase    : use_case,
            PKCS11Attributes.hsm_import_certificate   : import_certificate_into_hsm,
            PKCS11Attributes.hsm_certificate_directory: distribution_directory,
            PKCS11Attributes.hsm_cryptoki_file        : cryptoki_file,
            PKCS11Attributes.hsm_client_tool_path     : client_tools_directory,
            PKCS11Attributes.hsm_openssl_config_file  : openssl_config_file,
            PKCS11Attributes.hsm_reverse_subject_dn   : {True: "Yes", False: "No"}.get(reverse_subject_dn),
            PKCS11Attributes.hsm_embed_sans_in_csr    : {True: "Yes", False: "No"}.get(embed_sans_in_csr),
        }
        if openssl_directory:
            app_attrs.update({
                PKCS11Attributes.hsm_openssl_type: "Custom OpenSSL Directory",
                PKCS11Attributes.hsm_openssl_path: openssl_directory
            })

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('PKCS #12')
class PKCS12(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.pkcs_12)

    def create(self, name: str, device: 'Union[Config.Object, str]', pkcs12_file: 'str', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, port: 'int' = None,
               private_key_credential: 'Union[Config.Object, str]' = None, friendly_name: 'str' = None,
               certificate_chain_file: 'str' = None, create: 'bool' = None, replace_existing: 'bool' = None,
               reuse_friendly_name: 'bool' = None, owner: 'str' = None,
               owner_permissions: 'str' = None, group: 'str' = None, group_permissions: 'str' = None,
               attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            pkcs12_file: PKCS #12 file.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port.
            private_key_credential: :ref:`config_object` or :ref:`dn` of the private key credential.
            friendly_name: Friendly name.
            certificate_chain_file: Certificate chain file.
            create: Create store.
            replace_existing: Replace existing store.
            reuse_friendly_name: Reuse the friendly name.
            owner: File user owner.
            owner_permissions: File permissions assigned to the user owner.
            group: File group owner.
            group_permissions: File permissions assigned to the group owner.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name           : 'apppkcs12',
            PKCS12Attributes.credential                     : self._get_dn(
                application_credential) if application_credential else None,
            PKCS12Attributes.port                           : port,
            PKCS12Attributes.certificate_file               : pkcs12_file,
            PKCS12Attributes.private_key_password_credential: self._get_dn(
                private_key_credential) if private_key_credential else None,
            PKCS12Attributes.friendly_name                  : friendly_name,
            PKCS12Attributes.create_store                   : {True: "1", False: "0"}.get(create),
            PKCS12Attributes.replace_store                  : {True: "1", False: "0"}.get(replace_existing),
            PKCS12Attributes.recycle_alias                  : {True: "1", False: "0"}.get(reuse_friendly_name)
        }

        if certificate_chain_file:
            app_attrs.update({
                PKCS12Attributes.bundle_certificate    : "0",
                PKCS12Attributes.certificate_chain_file: certificate_chain_file
            })
        else:
            app_attrs.update({
                PKCS12Attributes.bundle_certificate: "1"
            })

        if owner or group:
            app_attrs.update({
                ApacheAttributes.file_permissions_enabled: "1",
                ApacheAttributes.file_owner_user         : owner,
                ApacheAttributes.file_permissions_user   : owner_permissions,
                ApacheAttributes.file_owner_group        : group,
                ApacheAttributes.file_permissions_group  : group_permissions,
            })

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('Riverbed Steelhead')
class RiverbedSteelHead(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.riverbed_steelhead)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               certificate_type: 'str' = None, replace_existing: 'bool' = None,
               install_chain_certificates: 'bool' = None,
               attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            certificate_type: Certificate type.
            replace_existing: Replace existing certificate.
            install_chain_certificates: Install the chain certificates.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name       : 'appriverbedsteelhead',
            RiverbedSteelHeadAttributes.certificate_type: certificate_type,
            RiverbedSteelHeadAttributes.replace_existing: {True: "1", False: "0"}.get(replace_existing),
            RiverbedSteelHeadAttributes.install_chain   : {True: "1", False: "0"}.get(install_chain_certificates)
        }

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('Tealeaf PCA')
class TealeafPCA(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.tealeaf_pca)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, port: 'int' = None,
               passive_capture_setup_path: 'str' = None, attributes: dict = None, get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port.
            passive_capture_setup_path: Passive capture setup path.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name: 'apptealeafpca',
            TealeafPCAAttributes.credential      : self._get_dn(
                application_credential) if application_credential else None,
            TealeafPCAAttributes.port            : port,
            TealeafPCAAttributes.install_path    : passive_capture_setup_path
        }

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )


@feature('VAM nShield')
class VAMnShield(_ApplicationBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.vam_nshield)

    def create(self, name: str, device: 'Union[Config.Object, str]', description: 'str' = None,
               contacts: 'List[Union[Identity.Identity, str]]' = None,
               approvers: 'List[Union[Identity.Identity, str]]' = None,
               application_credential: 'Union[Config.Object, str]' = None, port: 'int' = None,
               nshield_setup_path: 'str' = None,
               module_id: 'int' = None, restart_device: 'bool' = None, attributes: dict = None,
               get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the application object.
            device: :ref:`config_object` or :ref:`dn` of the device object.
            description: Description for the application object.
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts for the application object.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` as approvers for the application object.
            application_credential: :ref:`config_object` or :ref:`dn` of the application credential.
            port: Connection port.
            nshield_setup_path: nShield setup path.
            module_id: Module ID.
            restart_device: Restart the device.
            attributes: Additional attributes pertaining to the application object.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the application.
        """
        app_attrs = {
            ApplicationBaseAttributes.driver_name   : 'appvamnshield',
            VAMnShieldAttributes.credential         : self._get_dn(
                application_credential) if application_credential else None,
            VAMnShieldAttributes.port               : port,
            VAMnShieldAttributes.install_path       : nshield_setup_path,
            VAMnShieldAttributes.module_id          : module_id,
            VAMnShieldAttributes.restart_application: restart_device
        }

        if attributes:
            app_attrs.update(attributes)

        return self._create(
            name=name,
            device=device,
            approvers=approvers,
            contacts=contacts,
            description=description,
            attributes=app_attrs,
            get_if_already_exists=get_if_already_exists
        )
# endregion Applications


# region Application Groups
class _ApplicationGroupBase(FeatureBase):
    def __init__(self, api, class_name):
        super().__init__(api=api)
        self.class_name = class_name
        self.certificate_suffix = f'{class_name.split(maxsplit=1)[0]} App Group'

    def delete(self, application_group: 'Union[Config.Object, str]', dissociate: bool = True):
        """
        Deletes an application group object.

        Args:
            application_group: :ref:`config_object` or :ref:`dn` of the application object.
            dissociate: If ``True``, dissociate all applications in the group from the certificate.
        """
        application_group_dn = self._get_dn(application_group)
        if dissociate:
            consumer_dns, certificate_dn = self._get_applications_in_group(application_group=application_group)
            result = self._api.websdk.Certificates.Dissociate.post(
                certificate_dn=certificate_dn,
                application_dn=consumer_dns,
                delete_orphans=False
            )
            if not result.success:
                raise FeatureException(
                    f'Unable to dissociate the applications in the application group "{application_group.dn}" '
                    f'from {certificate_dn}'
                )
        self._secret_store_delete(object_dn=application_group_dn)
        self._config_delete(object_dn=application_group_dn)

    def get(self, application_group_dn: str, raise_error_if_not_exists: bool = True):
        """
        Args:
            application_group_dn: :ref:`dn` of the application group object.
            raise_error_if_not_exists: Raise an exception if the application :ref:`dn` does not exist.

        Returns:
            :ref:`config_object` of the application.
        """
        return self._get_config_object(
            object_dn=application_group_dn,
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def get_applications_in_group(self, application_group: 'Union[Config.Object, str]'):
        """
        Args:
            application_group: :ref:`config_object` or :ref:`dn` of the application group.

        Returns:
            List of :ref:`dn`.
        """
        consumer_dns, certificate_dn = self._get_applications_in_group(application_group=application_group)
        return consumer_dns

    def _create(self, application_dns: List[str], certificate: 'Config.Object', attributes: dict = None):
        # Create the Application Group.
        app_group = self._config_create(
            name=f'{certificate.name} - {self.certificate_suffix}',
            parent_folder_dn=certificate.parent,
            config_class=self.class_name,
            attributes=attributes
        )
        # Associate the Application Group :ref:`dn`.
        result = self._api.websdk.Config.WriteDn.post(
            object_dn=certificate.dn,
            attribute_name=X509CertificateAttributes.application_group_dn,
            values=[app_group.dn]
        ).result
        if result.code != 1:
            raise InvalidResultCode(code=result.code, code_description=result.config_result)

        # Associate each individual application.
        result = self._api.websdk.Certificates.Associate.post(
            application_dn=application_dns,
            certificate_dn=certificate.dn,
            push_to_new=False
        )
        if not result.success:
            raise FeatureException(f'Unable to associate the given applications to the certificate "{certificate.dn}".')

        return app_group

    def _get_applications_in_group(self, application_group: 'Union[Config.Object, str]'):
        application_group_dn = self._get_dn(application_group)
        certificate_dn = self._api.websdk.Config.Read.post(
            object_dn=application_group_dn,
            attribute_name=ApplicationGroupAttributes.certificate
        ).values[0]
        consumer_dns = self._api.websdk.Config.Read.post(
            object_dn=certificate_dn,
            attribute_name=X509CertificateAttributes.consumers
        ).values
        return consumer_dns, certificate_dn


@feature('Apache Group')
class ApacheApplicationGroup(_ApplicationGroupBase):
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.apache_application_group)

    def create(self, applications: 'List[Union[Config.Object, str]]', certificate: 'Union[Config.Object, str]',
               common_data_location: str = None, attributes: dict = None):
        """
        Args:
            applications: List of :ref:`config_object` or :ref:`dn` that will belong to the application group.
            certificate: :ref:`config_object` or :ref:`dn` of the associated certificate.
            common_data_location: The common data location for the application group.
            attributes: Dictionary of attributes to apply to the group explicitly. If not given, then the
                        attributes belonging to the first application in the given list will be assumed to
                        be the shared attributes for the application group.

        Returns:
            :ref:`config_object` of the application.
        """
        application_dns = [self._get_dn(application) for application in applications]
        certificate = self._get_config_object(object_dn=certificate)
        default_attrs = self._api.websdk.Config.ReadAll.post(object_dn=application_dns[0]).name_values
        if not common_data_location:
            try:
                hsm = next(attr.values[0] for attr in default_attrs if
                           attr.name == ApacheApplicationGroupAttributes.private_key_location)
            except StopIteration:
                hsm = None
            if hsm == ApplicationAttributeValues.Apache.PrivateKeyLocation.thales_nshield_hsm:
                common_data_location = '/opt/nfast/bin'
            elif hsm == ApplicationAttributeValues.Apache.PrivateKeyLocation.gemalto_safe_net_hsm:
                common_data_location = '/usr/safenet/lunaclient/bin'

        group_attributes = {
            ApacheApplicationGroupAttributes.client_tools_path            : None,
            ApacheApplicationGroupAttributes.partition_password_credential: None,
            ApacheApplicationGroupAttributes.protection_type              : None,
            ApacheApplicationGroupAttributes.softcard_identifier          : None,
            ApacheApplicationGroupAttributes.private_key_label            : None,
            ApplicationGroupAttributes.common_data_location               : common_data_location,
            ApplicationGroupAttributes.certificate                        : certificate.dn,
            ApplicationGroupAttributes.enrollment_application_dn          : application_dns[0],
        }
        for attribute in default_attrs:
            if attribute.name in group_attributes.keys():
                group_attributes[attribute.name] = attribute.values

        if attributes:
            group_attributes.update(attributes)

        return self._create(application_dns=application_dns, certificate=certificate, attributes=group_attributes)


@feature('PKCS11 Group')
class PKCS11ApplicationGroup(_ApplicationGroupBase):
    """
    .. note::
        The PKCS #11 VSE must be installed in order to use this driver.
    """
    def __init__(self, api):
        super().__init__(api=api, class_name=Classes.pkcs11_application_group)

    def create(self, applications: 'List[Union[Config.Object, str]]', certificate: 'Union[Config.Object, str]',
               attributes: dict = None):
        """
        Args:
            applications: List of :ref:`config_object` or :ref:`dn` that will belong to the application group.
            certificate: :ref:`config_object` or :ref:`dn` of the associated certificate.
            attributes: Dictionary of attributes to apply to the group explicitly. If not given, then the
                        attributes belonging to the first application in the given list will be assumed to
                        be the shared attributes for the application group.

        Returns:
            :ref:`config_object` of the application.
        """
        application_dns = [self._get_dn(application) for application in applications]
        certificate = self._get_config_object(object_dn=certificate)
        default_attrs = self._api.websdk.Config.ReadAll.post(object_dn=application_dns[0]).name_values
        group_attributes = {
            PKCS11ApplicationGroupAttributes.hsm_cka_label_format   : None,
            PKCS11ApplicationGroupAttributes.hsm_requested_cka_label: None,
            PKCS11ApplicationGroupAttributes.hsm_embed_sans_in_csr  : None,
            PKCS11ApplicationGroupAttributes.hsm_import_certificate : None,
            PKCS11ApplicationGroupAttributes.hsm_protection_type    : None,
            PKCS11ApplicationGroupAttributes.hsm_requested_usecase  : None,
            PKCS11ApplicationGroupAttributes.hsm_reverse_subject_dn : None,
            PKCS11ApplicationGroupAttributes.hsm_token_label        : None,
            PKCS11ApplicationGroupAttributes.hsm_token_password     : None,
            ApplicationGroupAttributes.certificate                  : certificate.dn,
            ApplicationGroupAttributes.enrollment_application_dn    : application_dns[0],
        }
        for attribute in default_attrs:
            if attribute.name in group_attributes.keys():
                group_attributes[attribute.name] = attribute.values
        if attributes:
            group_attributes.update(attributes)

        return self._create(application_dns=application_dns, certificate=certificate, attributes=group_attributes)
# endregion Application Groups
