.. _workflow_usage:

Workflows And Tickets
=====================

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

.. note::
    Refer to :ref:`applying_workflows` for applying workflows.

Creating, Applying, & Deleting A Standard Workflow
--------------------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    #### CREATE AND APPLY ####
    workflow = features.workflow.standard.create(
        name='|WfName|',
        parent_folder=r'|WfDn|',
        stage=300,
        injection_command="/bin/bash /run/something.sh",
        application_class_name=Attributes.application.apache.__config_class__,
        approvers=['|LocalUser|', '|DomainUser|'],
        macro='$Config[$Config[$WorkflowtargetDN$,"Owner Object"]$,"Contact"|"Approver"]$',
        reason_code=100
    )
    features.folder.apply_workflow(
        folder=r'|CertDn|',
        workflow=workflow
    )

    #### DELETE ####
    features.workflow.standard.delete(workflow=r'|WfDn|\|WfName|')

Creating, Applying, & Deleting An Adaptable Workflow
----------------------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Read in the file stream as bytes.
    with open('SuperAwesomeScript.ps1', 'rb') as f:
        script_content_in_bytes = f.read()

    #### CREATE ####
    workflow = features.workflow.adaptable.create(
        name='|WfName|',
        parent_folder=r'|WfDn|',
        stage=300,
        approvers=['|LocalUser|', '|DomainUser|'],
        reason_code=100,
        powershell_script_name='SuperAwesomeScript',  # Name of the script minus the extension.
        powershell_script_content=script_content_in_bytes,
        use_approvers_from_powershell_script=True
    )

    #### APPLY ####
    features.folder.apply_workflow(
        folder=r'|CertDn|',
        workflow=workflow
    )

    #### DELETE ####
    features.workflow.adaptable.delete(workflow=workflow)

Managing Workflow Tickets
-------------------------

Creating, Getting, & Deleting A Workflow Ticket
***********************************************

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####
    features.workflow.ticket.create(
        obj=r'|CertDn|\|CertName|',
        workflow=r'|WfDn|\|WfName|',
        approvers=['|LocalUser|', '|DomainUser|'],
        reason=42
    )

    #### GET ####
    # Multiple tickets can possibly exist on an object.
    tickets = features.workflow.ticket.get(obj=r'|CertDn|\|CertName|')

    #### DELETE ####
    # This neither approves nor rejects the ticket.
    features.workflow.ticket.delete(ticket_name=ticket)

Getting All Workflow Tickets Pending My Approval
************************************************

.. code-block:: python

    from pytpp import Authenticate, Features, AttributeValues

    api = Authenticate(...)
    features = Features(api)

    # Get all tickets pending my approval.
    tickets = [
        features.workflow.ticket.details(ticket)
        for ticket in features.workflow.ticket.get()
    ]
    pending_my_approval = [
        ticket for ticket in tickets
        if ticket.status == AttributeValues.Workflow.Status.pending
    ]


Approving And Rejecting Workflow Tickets
****************************************

.. code-block:: python

    from pytpp import Authenticate, Features, AttributeValues

    api = Authenticate(...)
    features = Features(api)

    # Get all tickets assigned to me. This includes all tickets of all statuses
    # and not just pending tickets.
    tickets = features.workflow.ticket.get()

    # Decide whether to approve/reject each ticket based on a minimum RSA key size of 2048.
    for ticket in tickets:
        details = features.workflow.ticket.details(ticket_name=ticket)
        certificate = features.certificate.details(details.issued_due_to)

        if details.status == AttributeValues.Workflow.Status.pending:
            if certificate.key_algorithm == AttributeValues.Certificate.KeyAlgorithm.rsa and \
                    certificate.key_size >= 2048:
                features.workflow.ticket.update_status(
                    ticket_name=ticket, status=AttributeValues.Workflow.Status.approved,
                    explanation="I trust this certificate request."
                )
            else:
                features.workflow.ticket.update_status(
                    ticket_name=ticket, status=AttributeValues.Workflow.Status.rejected,
                    explanation="This certificate does not meet the key size requirements.",
                )

Creating & Deleting Reason Codes
--------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####
    reason_code = features.workflow.reason_code.create(
        code=42,
        description='The answer to everything.',
        name='Awesome Reason Code'
    )

    #### DELETE ####
    features.workflow.reason_code.delete(
        code=42,
        name='Awesome Reason Code'
    )
