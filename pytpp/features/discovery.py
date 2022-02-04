from typing import List, Dict, Union
from pytpp.tools.vtypes import Config, Identity
from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.features.definitions.exceptions import UnexpectedValue
from pytpp.attributes.discovery import DiscoveryAttributes


@feature('Network Discovery')
class NetworkDiscovery(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._discovery_dn = r'\VED\Discovery'

    def create(self, name: str, hosts: List[str], default_certificate_location: 'Union[Config.Object, str]',
               attributes: dict = None, automatically_import: bool = False, blackout: Dict[str, List] = None,
               contacts: 'List[Union[Identity, str]]' = None, days_of_week: List[str] = None, days_of_month: List[str] = None,
               days_of_year: List[str] = None, description: str = None,
               exclusion_locations: 'Union[Config.Object, str]' = None, hour: int = None,
               placement_rules: 'List[Union[Config.Object, str]]' = None,
               ports: List[Union[str, int]] = None, priority: int = None, reschedule: bool = True,
               resolve_host: bool = True, utc: str = '1', get_if_already_exists: bool = True):
        """
        Args:
            name: Name of the discovery job.
            hosts: A list of hosts. If specific hosts should scan different ports, then specify by appending the
                   port to the IP address or hostname (i.e. 192.168.0.10:80). If no port is specified, then the
                   `ports` parameter will be appended to those hosts.
            default_certificate_location: :ref:`config_object` or :ref:`dn` of the folder to place results not 
                                          matching a placement rule.
            attributes: Additional attributes.
            automatically_import: If `True`, the job will terminate by placing the certificate objects, device
                                  objects, and application objects according to the placement rules.
            blackout: Period of time that TPP will not perform discovery operations. The format of this value
                      should be as follows: `[{<day>:[<hour>, <hour>, ...]}, {...}]` where `day` is the
                      zero-based index day of the week (i.e. Sunday = '0', etc.) and `hour` is the 24-hour
                      hour of the day (i.e. 1, 2, 3, ..., 23). For example:
            contacts: List of :ref:`identity_object` or :ref:`prefixed_name` as contacts.
            days_of_week: Zero-based index value of the days of the week to run the job.
            days_of_month: Day value(s) of the month to run the job.
            days_of_year: Days of the year to run the job in the format "MM/DD" where leading zeros can be ignored
                          (i.e. 1/23, 10/3).
            description: Description of the job.
            exclusion_locations: List of :ref:`config_object` or :ref:`dn` of exclusion folders.
            hour: 24-hour UTC hour format of the day (i.e. 20 = 8 PM UTC).
            placement_rules: List of :ref:`config_object` or :ref:`dn` for the placement rules. The order of the list matters
                             as the rules are prioritized accordingly.
            ports: List of ports to scan.
            priority: Priority of the job.
            reschedule: When ``True``, the job will run again on the next scheduled interval.
            resolve_host: Resolve the hostname when ``True``.
            utc: UTC offset.
            get_if_already_exists: If the objects already exists, just return it as is.

        Returns:
            :ref:`config_object` of the discovery job.

        """
        placement_rule_guids = None
        if placement_rules:
            placement_rule_guids = [f'{e}:{self._get_guid(pr)}' for e, pr in enumerate(placement_rules)]
        ports = ','.join(list(map(str, ports))) if ports else \
            "22,80,443-449,465,563,636,695,981-995,1311,1920,2083,2087,2096,2211,2484,2949,3268,3269,3414," \
            "4712,4843,5223,5358,6619,6679,6697,7002,8080,8222,8243,8333,8443,8878,8881,8882,9043,9090," \
            "9091,9443,18072,18080-18085,18090-18094,28080"
        address_range = [f'{h}:{ports}' if ':' not in h else h for h in hosts]

        if blackout:
            blackout = [f'{k}:{",".join(v)}' for k, v in blackout.items()]

        attributes = attributes or {}
        attributes.update({
            DiscoveryAttributes.address_range          : address_range,
            DiscoveryAttributes.automatically_import   : "1" if automatically_import else "0",
            DiscoveryAttributes.blackout               : blackout,
            DiscoveryAttributes.certificate_location_dn: self._get_dn(default_certificate_location)
                                                         if default_certificate_location else None,
            DiscoveryAttributes.contact                : [self._get_prefixed_universal(c) for c in contacts] if contacts else None,
            DiscoveryAttributes.description            : description,
            DiscoveryAttributes.discovery_exclusion_dn : [self._get_dn(el) for el in exclusion_locations]
                                                         if exclusion_locations else None,
            DiscoveryAttributes.placement_rule         : placement_rule_guids,
            DiscoveryAttributes.priority               : priority,
            DiscoveryAttributes.reschedule             : "1" if hour and reschedule else "0",
            DiscoveryAttributes.resolve_host           : "1" if resolve_host else "0",
            DiscoveryAttributes.utc                    : utc
        })

        if hour:
            attributes[DiscoveryAttributes.hour] = hour
            if days_of_week:
                attributes[DiscoveryAttributes.days_of_week] = days_of_week
            elif days_of_month:
                attributes[DiscoveryAttributes.days_of_month] = days_of_month
            elif days_of_year:
                attributes[DiscoveryAttributes.days_of_year] = days_of_year

        return self._config_create(
            name=name,
            parent_folder_dn=self._discovery_dn,
            config_class=DiscoveryAttributes.__config_class__,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

    def delete(self, job: 'Union[Config.Object, str]'):
        """
        Deletes the discovery job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_guid = self._get_guid(job, parent_dn=self._discovery_dn)
        response = self._api.websdk.Discovery.Guid(guid=job_guid).delete()
        response.assert_valid_response()

    def get(self, name: str, raise_error_if_not_exists: bool = True):
        """
        Args:
            name: Name of the discovery job.
            raise_error_if_not_exists: Raise an exception if the discovery job does not exist.

        Returns:
            :ref:`config_object` of the discovery job.
        """
        return self._get_config_object(
            object_dn=f'{self._discovery_dn}\\{name}',
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def is_in_progress(self, job: 'Union[Config.Object, str]'):
        """
        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.

        Returns:
            bool: ``True`` if the job is in progress or ``False`` if it is not.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        response = self._api.websdk.Config.Read.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status
        )
        in_progress_states = ['Pending Execution', 'Running']
        if response.is_valid_response():
            if len(response.values) > 0:
                status = response.values[0]
                return status in in_progress_states
        return False

    def schedule(self, job: 'Union[Config.Object, str]', hour: Union[str, int], days_of_week: List[Union[int, str]] = None,
                 days_of_month: List[Union[int, str]] = None, days_of_year: List[str] = None):
        """
        Schedules an existing job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
            hour: 24-hour UTC hour format (i.e. 20 = 8PM UTC).
            days_of_week: Zero-based index of the days of the week (i.e. Sunday = '0').
            days_of_month: Days of the month without leading zeros.
            days_of_year: Days of the year in "MM/DD" format without leading zeros (i.e. 1/23, 10/3).
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        hour = str(hour)
        if not isinstance(hour, list):
            hour = [hour]

        attributes = {
            DiscoveryAttributes.reschedule: "1",
            DiscoveryAttributes.hour      : hour
        }
        if days_of_week:
            attributes[DiscoveryAttributes.days_of_week] = map(str, days_of_week)
        elif days_of_month:
            attributes[DiscoveryAttributes.days_of_month] = map(str, days_of_month)
        elif days_of_year:
            attributes[DiscoveryAttributes.days_of_year] = days_of_year

        response = self._api.websdk.Config.Write.post(
            object_dn=job_dn,
            attribute_data=self._name_value_list(attributes, keep_list_values=True)
        )
        response.assert_valid_response()

    def unschedule(self, job: 'Union[Config.Object, str]'):
        """
        Removes a schedule from a job. This does not delete the job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        for attribute_name in {
            DiscoveryAttributes.hour,
            DiscoveryAttributes.days_of_year,
            DiscoveryAttributes.days_of_month,
            DiscoveryAttributes.days_of_week,
            DiscoveryAttributes.reschedule
        }:
            self._api.websdk.Config.ClearAttribute.post(
                object_dn=job_dn,
                attribute_name=attribute_name
            ).assert_valid_response()

    def blackout_schedule(self, job: 'Union[Config.Object, str]', sunday: List[Union[str, int]] = None,
                          monday: List[Union[str, int]] = None, tuesday: List[Union[str, int]] = None,
                          wednesday: List[Union[str, int]] = None, thursday: List[Union[str, int]] = None,
                          friday: List[Union[str, int]] = None, saturday: List[Union[str, int]] = None):
        """
        Times of the week to restrict a discovery job from processing.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
            sunday: List of hours without leading zeros to restrict processing on Sunday.
            monday: List of hours without leading zeros to restrict processing on Monday.
            tuesday: List of hours without leading zeros to restrict processing on Tuesday.
            wednesday: List of hours without leading zeros to restrict processing on Wednesday.
            thursday: List of hours without leading zeros to restrict processing on Thursday.
            friday: List of hours without leading zeros to restrict processing on Friday.
            saturday: List of hours without leading zeros to restrict processing on Saturday.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        blackout = []
        for e, day in enumerate([sunday, monday, tuesday, wednesday, thursday, friday, saturday]):
            if day:
                hours = ','.join(map(str, day))
                blackout.append(f'{e}:{hours}')
        attributes = {
            DiscoveryAttributes.blackout: blackout
        }
        response = self._api.websdk.Config.Write.post(
            object_dn=job_dn,
            attribute_data=self._name_value_list(attributes, keep_list_values=True)
        )
        response.assert_valid_response()

    def run_now(self, job: 'Union[Config.Object, str]', timeout: int = 60):
        """
        Runs a job despite any scheduling. This does not return until the job is processing,
        or has a *Processing* Attribute.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
            timeout: Timeout in seconds within which the job should start.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        response = self._api.websdk.Config.Write.post(
            object_dn=job_dn,
            attribute_data=self._name_value_list({
                "Start Now": ['1']  # Secret config-bridge attribute name.
            })
        )
        response.assert_valid_response()

        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired():
                if self.is_in_progress(job=job):
                    return

        raise UnexpectedValue(
            f'Expected the job "{job_dn}" to start progress, but it did not.'
        )

    def cancel(self, job: 'Union[Config.Object, str]'):
        """
        Cancels a currently running job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        response = self._api.websdk.Config.WriteDn.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status,
            values=['Canceled']
        )
        response.assert_valid_response()

    def pause(self, job: 'Union[Config.Object, str]'):
        """
        Pauses a currently running job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        response = self._api.websdk.Config.WriteDn.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status,
            values=['Paused']
        )
        response.assert_valid_response()

    def resume(self, job: 'Union[Config.Object, str]'):
        """
        Resumes a currently paused job.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        response = self._api.websdk.Config.WriteDn.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status,
            values=['Pending']
        )
        response.assert_valid_response()

    def place_results(self, job: 'Union[Config.Object, str]'):
        """
        .. warning::
            This functionality has been deprecated in TPP 21.1 and will have no effect
            from this version forward.

        Places the results of the discovery job according to the placement rules.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
        """
        if self._is_version_compatible(maximum="20.4"):
            job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
            response = self._api.websdk.Config.WriteDn.post(
                object_dn=job_dn,
                attribute_name="Import Results Now",  # Secret config-bridge attribute name.
                values=['1']
            )
            response.assert_valid_response()

    def get_all_jobs(self):
        """
        Returns:
            List of :ref:`config_object` of all network discovery jobs.
        """
        jobs = self._api.websdk.Config.FindObjectsOfClass.post(
            class_name='Discovery',
            object_dn=self._discovery_dn
        )

        return jobs.objects

    def wait_for_job_to_finish(self, job: 'Union[Config.Object, str]', check_interval: int = 5, timeout: int = 300):
        """
        Waits for the  *Status* attribute to have a value other than *Pending Execution* and *Running*
        on the discovery job. An error is raised if the timeout is exceeded.

        Args:
            job: :ref:`config_object` or :ref:`dn` of the discovery job.
            check_interval: Poll interval in seconds to validate that the job finished.
            timeout: Timeout in seconds to wait for the job to finish.
        """
        job_dn = self._get_dn(job, parent_dn=self._discovery_dn)
        with self._Timeout(timeout=timeout) as to:
            while not to.is_expired(poll=check_interval):
                if not self.is_in_progress(job=job):
                    return

        status = self._api.websdk.Config.Read.post(
            object_dn=job_dn,
            attribute_name=DiscoveryAttributes.status
        ).values[0]
        raise TimeoutError(
            f'Expected Network Discovery Job "{job_dn}" to finish within {timeout} seconds, but it is still '
            f'running. It has a status of "{status}."'
        )
