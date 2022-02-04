from typing import List, Dict
from pytpp.features.bases.feature_base import FeatureBase, feature


# region Platform Components
class _PlatformComponentBase(FeatureBase):
    def __init__(self, api, module: str):
        super().__init__(api=api)
        self._engines_dn = r'\VED\Engines'
        self._module = module

    def _module_dn(self, engine_name: str):
        return f'{self._engines_dn}\\{engine_name}\\{self._module}'

    def _engine_has_module_enabled(self, engine_name: str):
        engines = self._api.websdk.SystemStatus.get().engines
        for engine in engines:
            if engine.engine_name.lower() == engine_name.lower():
                if self._module in engine.services.vplatform.modules:
                    return True
        return False

    def update_engines(self, attributes: Dict[str, List[str]], engine_names: List[str] = None):
        """
        Updates a Platform's module attributes. Each engine in ``engine_names`` will be updated
        to have the given ``attributes``.

        Args:
            attributes: Dictionary of attributes and attribute values to update.
            engine_names: List of engine names.
        """
        engine_names = engine_names or [engine.engine_name for engine in self._api.websdk.ProcessingEngines.get().engines]
        for engine_name in engine_names:
            response = self._api.websdk.Config.Write.post(
                object_dn=self._module_dn(engine_name=engine_name),
                attribute_data=self._name_value_list(attributes, keep_list_values=True)
            )
            response.assert_valid_response()

@feature('Auto Layout Manager')
class AutoLayoutManager(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='Auto Layout Manager')


@feature('Bulk Provisioning Manager')
class BulkProvisioningManager(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='Bulk Provisioning Manager')


@feature('CA Import Manager')
class CAImportManager(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='CA Import Manager')


@feature('Certificate Manager')
class CertificateManager(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='Certificate Manager')


@feature('Certificate Pre-Enrollment')
class CertificatePreEnrollment(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='Certificate Pre-Enrollment')


@feature('Certificate Revocation')
class CertificateRevocation(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='Certificate Revocation')


@feature('Cloud Instance Monitor')
class CloudInstanceMonitor(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='Cloud Instance Monitor')


@feature('Discovery Manager')
class DiscoveryManager(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='Discovery')


@feature('Monitor')
class Monitor(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='Monitor')


@feature('Onboard Discovery Manager')
class OnboardDiscoveryManager(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='Onboard Discovery Manager')


@feature('Reporting')
class Reporting(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='Reporting')


@feature('SSH Manager')
class SSHManager(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='SSH Manager')


@feature('TrustNet Manager')
class TrustNetManager(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='TrustNet Manager')


@feature('Validation Manager')
class ValidationManager(_PlatformComponentBase):
    def __init__(self, api):
        super().__init__(api=api, module='Validation Manager')
# endregion Platform Components

# region Platform Root
@feature('Platforms')
class Platforms(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._engines_dn = r'\VED\Engines'

        self._auto_layout_manager = None
        self._bulk_provisioning_manager = None
        self._ca_import_manager = None
        self._certificate_manager = None
        self._certificate_pre_enrollment = None
        self._certificate_revocation = None
        self._cloud_instance_monitor = None
        self._discovery_manager = None
        self._monitor = None
        self._onboard_discovery_manager = None
        self._reporting = None
        self._ssh_manager = None
        self._trustnet_manager = None
        self._validation_manager = None

    # region Component Properties
    @property
    def auto_layout_manager(self) -> AutoLayoutManager:
        self._auto_layout_manager = self._auto_layout_manager or AutoLayoutManager(self._api)
        return self._auto_layout_manager

    @property
    def bulk_provisioning_manager(self) -> BulkProvisioningManager:
        self._bulk_provisioning_manager = self._bulk_provisioning_manager or BulkProvisioningManager(self._api)
        return self._bulk_provisioning_manager

    @property
    def ca_import_manager(self) -> CAImportManager:
        self._ca_import_manager = self._ca_import_manager or CAImportManager(self._api)
        return self._ca_import_manager

    @property
    def certificate_manager(self) -> CertificateManager:
        self._certificate_manager = self._certificate_manager or CertificateManager(self._api)
        return self._certificate_manager

    @property
    def certificate_pre_enrollment(self) -> CertificatePreEnrollment:
        self._certificate_pre_enrollment = self._certificate_pre_enrollment or CertificatePreEnrollment(self._api)
        return self._certificate_pre_enrollment

    @property
    def certificate_revocation(self) -> CertificateRevocation:
        self._certificate_revocation = self._certificate_revocation or CertificateRevocation(self._api)
        return self._certificate_revocation

    @property
    def cloud_instance_monitor(self) -> CloudInstanceMonitor:
        self._cloud_instance_monitor = self._cloud_instance_monitor or CloudInstanceMonitor(self._api)
        return self._cloud_instance_monitor

    @property
    def discovery_manager(self) -> DiscoveryManager:
        self._discovery_manager = self._discovery_manager or DiscoveryManager(self._api)
        return self._discovery_manager

    @property
    def monitor(self) -> Monitor:
        self._monitor = self._monitor or Monitor(self._api)
        return self._monitor

    @property
    def onboard_discovery_manager(self) -> OnboardDiscoveryManager:
        self._onboard_discovery_manager = self._onboard_discovery_manager or OnboardDiscoveryManager(self._api)
        return self._onboard_discovery_manager

    @property
    def reporting(self) -> Reporting:
        self._reporting = self._reporting or Reporting(self._api)
        return self._reporting

    @property
    def ssh_manager(self) -> SSHManager:
        self._ssh_manager = self._ssh_manager or SSHManager(self._api)
        return self._ssh_manager

    @property
    def trustnet_manager(self) -> TrustNetManager:
        self._trustnet_manager = self._trustnet_manager or TrustNetManager(self._api)
        return self._trustnet_manager

    @property
    def validation_manager(self) -> ValidationManager:
        self._validation_manager = self._validation_manager or ValidationManager(self._api)
        return self._validation_manager
    # endregion Component Properties

    def get(self):
        """
        Returns:
            :ref:`config_object` of the Engines root.
        """
        return self._get_config_object(object_dn=self._engines_dn)
# endregion Platform Root
