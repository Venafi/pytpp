import base64
import hashlib
from dataclasses import dataclass
from typing import List, Union
from datetime import datetime
from pytpp.tools.vtypes import Config, Identity
from pytpp.features.bases.feature_base import FeatureBase, feature
from pytpp.features.definitions.exceptions import InvalidResultCode
from pytpp.properties.secret_store import KeyNames, Namespaces, VaultTypes
from pytpp.attributes.workflow import WorkflowAttributes
from pytpp.attributes.adaptable_workflow import AdaptableWorkflowAttributes
from pytpp.attributes.workflow_ticket import WorkflowTicketAttributes


class _WorkflowBase(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

    def delete(self, workflow: 'Union[Config.Object, str]'):
        """
        Deletes a workflow.

        Args:
            workflow: :ref:`config_object` or :ref:`dn` of the workflow object.
        """
        workflow_dn = self._get_dn(workflow)
        self._secret_store_delete(object_dn=workflow_dn)
        self._config_delete(object_dn=workflow_dn)

    def get(self, workflow_dn: str, raise_error_if_not_exists: bool = True):
        """
        Returns the config object of the folder DN.

        Args:
            workflow_dn: :ref:`dn` of the workflow.
            raise_error_if_not_exists: Raise an exception if the object :ref:`dn` does not exist.

        Returns:
            :ref:`config_object` of the workflow object.
        """
        return self._get_config_object(
            object_dn=workflow_dn,
            raise_error_if_not_exists=raise_error_if_not_exists
        )

    def _create(self, name: str, parent_folder: 'Union[Config.Object, str]', is_adaptable: bool, stage: int, injection_command: str = None,
                application_class_name: str = None, approvers: str = None, reason_code: int = None, attributes: dict = None,
                get_if_already_exists: bool = True):    
        workflow = self._config_create(
            name=name,
            parent_folder_dn=self._get_dn(parent_folder),
            config_class=WorkflowAttributes.__config_class__ if not is_adaptable else AdaptableWorkflowAttributes.__config_class__,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

        if is_adaptable:
            driver_str = '037Venafi.Drivers.AdaptableWFApplication'
        else:
            driver_str = '028Venafi.Drivers.WFApplication'
        if application_class_name:
            application_class_name = str(application_class_name)
            stage_str = f'B&{len(str(stage)):03d}{stage}D-{len(application_class_name):03d}{application_class_name}'
        else:
            stage_str = f'B-{len(str(stage)):03d}{stage}'

        injection_command_str = f'B&{len(injection_command):03d}{injection_command}' if injection_command else ''
        approvers_str = f'C-{"0" * (3 - len(str(len(approvers))))}{str(len(approvers))}{approvers}'
        reason_code_str = f'{"0" * (3 - len(str(reason_code)))}{reason_code}'

        rule = f'{driver_str}{stage_str}{injection_command_str}{approvers_str}{reason_code_str}'.encode('utf-8')
        rule = base64.b64encode(rule)

        vault_id = self._api.websdk.SecretStore.Add.post(
            base_64_data=rule.decode('utf-8'),
            vault_type=VaultTypes.blob,
            owner=workflow.dn,
            keyname=KeyNames.software_default,
            namespace=Namespaces.config
        ).vault_id

        self._api.websdk.Config.AddValue.post(
            object_dn=workflow.dn,
            attribute_name=WorkflowAttributes.rule_vault_id,
            value=vault_id
        )

        return workflow


@feature('Adapatable Workflow')
class AdaptableWorkflow(_WorkflowBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder: 'Union[Config.Object, str]', stage: int, powershell_script_name: str,
               powershell_script_content: bytes, approvers: 'List[Union[Identity.Identity, str]]' = None, reason_code: int = None,
               use_approvers_from_powershell_script: bool = False, attributes: dict = None, get_if_already_exists: bool = True):
        """
        .. note::
            If a list of approver identity objects is provided, they will be added directly to the workflow as approvers of the 
            workflow. If the approvers should come from the PowerShell script, do not supply this parameter. Instead, set 
            ``use_approvers_from_powershell_script = True``. If the approvers should come from the object requiring the workflow, 
            such as the certificate object, then do not supply ``approvers`` or ``use_approvers_from_powershell_script``.

        Args:
            name: Name of the workflow object.
            parent_folder: :ref:`config_object` or :ref:`dn` of the parent folder.
            stage: One of the valid stages that represent the certificate lifecycle.
            powershell_script_name: Name (not path) of the actual PowerShell script on the TPP server.
            powershell_script_content: Contents of the PowerShell script as bytes.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` for each approver.
            reason_code: Integer reason code.
            use_approvers_from_powershell_script: If ``True`` and no ``approvers`` is supplied, then set the
                workflow to use the approvers defined by the script.
            attributes: Additional attributes to apply to the workflow object.
            get_if_already_exists: If the objects already exists, it is modified according to these parameters. Else
                and exception is raised..
        Returns:
            :ref:`config_object` of the workflow object.
        """
        if approvers:
            wf_approvers = ','.join([a.prefixed_universal for a in approvers])
        elif use_approvers_from_powershell_script:
            wf_approvers = "$CONFIG[$SELFDN$,'Adaptable Workflow Approvers']$"
        else:
            wf_approvers = ''

        workflow = self._create(
            name=name,
            parent_folder=parent_folder,
            is_adaptable=True,
            stage=stage,
            approvers=wf_approvers,
            reason_code=reason_code,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

        self._api.websdk.Config.AddValue.post(
            object_dn=workflow.dn,
            attribute_name=AdaptableWorkflowAttributes.powershell_script,
            value=powershell_script_name
        ).assert_valid_response()

        vault_id = self._api.websdk.SecretStore.Add.post(
            base_64_data=self._calculate_hash(powershell_script_content),
            keyname=KeyNames.software_default,
            vault_type=VaultTypes.blob,
            namespace=Namespaces.config,
            owner=workflow.dn
        ).vault_id

        self._api.websdk.Config.WriteDn.post(
            object_dn=workflow.dn,
            attribute_name=AdaptableWorkflowAttributes.powershell_script_hash_vault_id,
            values=[vault_id]
        ).assert_valid_response()

        return workflow

    @staticmethod
    def _calculate_hash(script_content: bytes):
        return base64.b64encode(
            hashlib.sha256(
                script_content.decode().encode('utf-32-le')
            ).hexdigest().encode()
        ).decode()


@dataclass
class RC:
    code: int 
    name: str 
    description: str


@feature('Reason Code')
class ReasonCode(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)

        self._workflow_dn = r'\VED\Workflow Tickets'

    def create(self, code: int, name: str, description: str):
        """
        Args:
            code: An integer code.
            name: Name of the result code.
            description: Purpose of the result code.

        Returns:
            A ``ReasonCode`` object with these properties
            
            * **code** *(int)* - An integer code.
            * **name** *(str)* - Name of the result code.
            * **description** *(str)* - Purpose of the result code.
        """
        result = self._api.websdk.Config.AddValue.post(
            object_dn=self._workflow_dn,
            attribute_name=WorkflowTicketAttributes.approval_reason,
            value=f'{code},{name},{description}'
        )
        result.assert_valid_response()

        return RC(name=name, code=code, description=description)

    def delete(self, code: int, name: str = None):
        """
        Deletes a result code. ``name`` is not required, but when supplied, in the
        event that multiple codes exist with the same integer value, only the ones
        having ``name`` will be deleted.

        Args:
            code: An integer code.
            name: Name of the result code.
        """
        result_codes = self._api.websdk.Config.ReadDn.post(
            object_dn=self._workflow_dn,
            attribute_name=WorkflowTicketAttributes.approval_reason
        ).values

        if not result_codes:
            return

        search_string = f'{code},{name}' if name else f'{code}'
        for rc in result_codes:
            if search_string in rc:
                result = self._api.websdk.Config.RemoveDnValue.post(
                    object_dn=self._workflow_dn,
                    attribute_name=WorkflowTicketAttributes.approval_reason,
                    value=rc
                )
                result.assert_valid_response()


@feature('Standard Workflow')
class StandardWorkflow(_WorkflowBase):
    def __init__(self, api):
        super().__init__(api=api)

    def create(self, name: str, parent_folder: 'Union[Config.Object, str]', stage: int, injection_command: str = None,
               application_class_name: str = None, approvers: 'List[Union[Identity.Identity, str]]' = None, macro: str = None,
               reason_code: int = None, attributes: dict = None, get_if_already_exists: bool = True):
        """
        One of ``injection_command`` or ``approvers`` must be given.

        If a list of approver identity objects is provided, they will be added directly to the workflow as approvers of the
        workflow. If the approvers should come from the object requiring the workflow, such as the certificate object, then
        do not supply ``approvers``. If the approvers come from a TPP Macro, then supply ``macro`` with the desired macro.

        Args:
            name: Name of the workflow object.
            parent_folder: :ref:`config_object` or :ref:`dn` of the parent folder.
            stage: Workflow stage.
            injection_command: Command to be invoked on the target application.
            application_class_name: Application class name to trigger this workflow.
            approvers: List of :ref:`identity_object` or :ref:`prefixed_name` for each approver.
            macro: TPP approver macro.
            reason_code: Integer reason code.
            attributes: Additional attributes to apply to the workflow object.
            get_if_already_exists: If the objects already exists, it is modified according to these parameters. Else
                an exception is raised.

        Returns:
            :ref:`config_object` of the workflow object.
        """
        if approvers:
            wf_approvers = ','.join([a.prefixed_universal for a in approvers])
        elif macro:
            wf_approvers = macro
        else:
            wf_approvers = ''

        workflow = self._create(
            name=name,
            parent_folder=parent_folder,
            is_adaptable=False,
            stage=stage,
            injection_command=injection_command,
            application_class_name=str(application_class_name),
            approvers=wf_approvers,
            reason_code=reason_code,
            attributes=attributes,
            get_if_already_exists=get_if_already_exists
        )

        return workflow


@feature('Ticket')
class Ticket(FeatureBase):
    def __init__(self, api):
        super().__init__(api=api)
        self._workflow_ticket_dn = r'\VED\Workflow Tickets'

    @staticmethod
    def _validate_result_code(result):
        if result.code != 1:
            raise InvalidResultCode(code=result.code, code_description=result.workflow_result)

    def create(self, obj: 'Union[Config.Object, str]', workflow: 'Union[Config.Object, str]',
               approvers: Union['List[Identity.Identity]', List[str]], reason: Union[RC, int, str],
               user_data: str = None):
        """
        Creates a workflow ticket on ``obj`` only if the object is in a state to received a workflow ticket.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object requiring a workflow ticket.
            workflow: :ref:`config_object` or :ref:`dn` of the workflow object.
            approvers:  List of :ref:`identity_object` or :ref:`prefixed_name` for each approver.
            reason: ``RC`` or integer reason code.
            user_data: User data.

        Returns:
            str: Workflow ticket name.
        """
        obj_dn = self._get_dn(obj)
        workflow_dn = self._get_dn(workflow)
        approver_prefixed_names = [
            {'PrefixedName': self._get_prefixed_name(a)} for a in approvers
        ]
        if isinstance(reason, RC):
            reason = reason.code
        response = self._api.websdk.Workflow.Ticket.Create.post(
            object_dn=obj_dn,
            workflow_dn=workflow_dn,
            approvers=approver_prefixed_names,
            reason=int(reason),
            user_data=user_data
        )
        self._validate_result_code(response.result)
        return response.guid

    def delete(self, ticket_name: str):
        """
        Deletes a workflow ticket.

        Args:
            ticket_name: Name of the workflow ticket.
        """
        result = self._api.websdk.Workflow.Ticket.Delete.post(guid=ticket_name).result
        self._validate_result_code(result)

    def details(self, ticket_name: str):
        """
        Returns the details of a ticket request.

        Args:
            ticket_name: Name of the workflow ticket.

        Returns:
            :class:`~.dataclasses.workflow.Details` of the workflow ticket.
        """
        response = self._api.websdk.Workflow.Ticket.Details.post(guid=ticket_name)
        self._validate_result_code(result=response.result)
        return response.details

    def exists(self, ticket_name: str):
        """
        Args:
            ticket_name: Name of the workflow ticket.

        Returns:
            bool: ``True`` when a particular workflow exists, otherwise ``False``.
        """
        result = self._api.websdk.Workflow.Ticket.Exists.post(guid=ticket_name).result
        return result.code == 1

    def get(self, obj: 'Union[Config.Object, str]' = None, user_data: str = None, expected_num_tickets: int = 1, timeout: int = 10):
        """
        Gets all tickets associated to ``obj``. If the minimum expected number of tickets do not
        appear on the ``obj``, then a warning is logged and whatever was found is returned and no
        error is raised.

        Args:
            obj: :ref:`config_object` or :ref:`dn` of the object with a workflow ticket issued to it. If not given, only
                 ``user_data`` has effect.
            user_data: The string to filter results using the User Data attribute of the workflow ticket.
            expected_num_tickets: Minimum number of tickets expected to be written for the certificate.
            timeout: Time in seconds to wait for a ticket to be issued. Default is 10 seconds.

        Returns:
            List of :ref:`guid` for each ticket found.
        """
        if not obj:
            return self._api.websdk.Workflow.Ticket.Enumerate.post(
                user_data=user_data
            ).guids

        obj_dn = self._get_dn(obj)
        def get_tickets():
            return self._api.websdk.Workflow.Ticket.Enumerate.post(
                object_dn=obj_dn,
                user_data=user_data
            ).guids

        if timeout:
            tickets = []
            with self._Timeout(timeout=timeout) as to:
                while not to.is_expired():
                    tickets = get_tickets()
                    if len(tickets) >= expected_num_tickets:
                        return tickets

            self._log_warning_message(
                msg=f'The expected number of tickets on {obj_dn} was '
                    f'{expected_num_tickets}, but {len(tickets)} tickets were '
                    f'found instead.'
            )
            return tickets
        else:
            tickets = get_tickets()
            if len(tickets) < expected_num_tickets:
                self._log_warning_message(
                    msg=f'The expected number of tickets on {obj_dn} was '
                        f'{expected_num_tickets}, but {len(tickets)} tickets were '
                        f'found instead.'
                )
            return tickets

    def status(self, ticket_name: str):
        """
        Args:
            ticket_name: Name of the workflow ticket.

        Returns:
            str: The current status of a workflow ticket.
        """
        response = self._api.websdk.Workflow.Ticket.Status.post(guid=ticket_name)
        self._validate_result_code(result=response.result)
        return response.status

    def update_status(self, ticket_name: str, status: str, explanation: str = None, scheduled_start: datetime = None,
                      scheduled_stop: datetime = None):
        """
        Updates the status of a workflow ticket with the optional explanations and scheduled approvals. Marking a
        ticket as "Approved" will automatically delete the ticket.

        Args:
            ticket_name: Name of the workflow ticket.
            status: The new status of the workflow ticket.
            explanation: Reason for the new status.
            scheduled_start: Datetime to continue the approval process.
            scheduled_stop:  Datetime to expire the approval process.
        """
        result = self._api.websdk.Workflow.Ticket.UpdateStatus.post(
            guid=ticket_name,
            status=status,
            explanation=explanation,
            scheduled_start=scheduled_start.isoformat() if scheduled_start else None,
            scheduled_stop=scheduled_stop.isoformat() if scheduled_stop else None
        ).result
        self._validate_result_code(result)
