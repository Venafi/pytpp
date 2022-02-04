.. _certificate_usage:

Certificate
===========

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Creating & Deleting Certiifcate Objects
---------------------------------------

.. code-block:: python

    from pytpp import Features, Authenticate, AttributeValues

    api = Authenticate(...)
    features = Features(api=api)

    ### CREATE ####
    certificate = features.certificate.create(
        name='|CertName|',
        parent_folder=r'|CertDn|',
        contacts=['|LocalUser|', '|DomainUser|'],
        approvers=['|LocalUser|', '|DomainUser|'],
        common_name='|CertName|',
        management_type=AttributeValues.Certificate.ManagementType.enrollment,
        ca_template=r'|CaDn|\|CaName|',
        hash_algorithm=AttributeValues.Certificate.HashAlgorithm.sha256,
        city='Salt Lake City',
        state='Utah',
        country='US',
        organization='Awesome Company',
        organization_unit=['Awesome Team'],
        disable_automatic_renewal=False,
        key_algorithm=AttributeValues.Certificate.KeyAlgorithm.rsa,
        key_strength=2048
    )

    #### DELETE ####
    features.certificate.delete(certificate=certificate)

Renewing & Downloading A Certificate
------------------------------------

.. code-block:: python

    from pytpp import Features, Authenticate, AttributeValues

    api = Authenticate(...)
    features = Features(api=api)

    certificate = features.certificate.get(certificate_dn=r'|CertDn|\|CertName|')

    #### RENEW IT ####
    current_thumbprint = features.certificate.renew(certificate=certificate)

    #### WAIT FOR IT TO RENEW ####
    features.certificate.wait_for_enrollment_to_complete(
        certificate=certificate,
        current_thumbprint=current_thumbprint
    )

    #### DOWNLOAD IT ####
    downloaded_cert = features.certificate.download(
        format=AttributeValues.Certificate.Format.base64,
        certificate=certificate,
        include_chain=True,
        root_first_order=True
    )

Revoking A Certificate
----------------------

.. code-block:: python

    from pytpp import Features, Authenticate
    from datetime import datetime

    api = Authenticate(...)
    features = Features(api=api)

    previous_versions = features.certificate.get_previous_versions(
        certificate=r'|CertDn|\|CertName|',
        exclude_revoked=True
    )
    # Revoke previous versions of a certificate if it is expired.
    for pv in previous_versions:
        if pv.certificate_details.valid_to < datetime.today():
            features.certificate.revoke(
                certificate=r'|CertDn|\|CertName|',
                thumbprint=pv.certificate_details.thumbprint
            ))

Resetting & Retrying Certificate Requests
-----------------------------------------

.. code-block:: python

    from pytpp import Features, Authenticate, AttributeValues

    api = Authenticate(...)
    features = Features(api=api)

    certificate_dn = r'|CertDn|\|CertName|'

    try:
        current_thumbprint = features.certificate.renew(certificate=certificate_dn)
        features.certificate.wait_for_enrollment_to_complete(certificate=certificate_dn, current_thumbprint=current_thumbprint)
    except:
        features.certificate.retry_from_current_stage(certificate=certificate_dn)
        # ---- OR ----
        features.certificate.reset(certificate=certificate_dn)

File & SSL Validation
---------------------

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(...)
    features = Features(api=api)

    #### VALIDATE A CERTIFICATE ####
    validated_certificates, warnings = features.certificate.validate(
        certificates=[r'|CertDn|\|CertName|']
    )
    if len(warnings) > 0:
        # Perhaps we should do something about these warnings...
        ...

    #### GET VALIDATION RESULTS ####
    file_validation_results, ssl_validation_results = features.certificate.get_validation_results(
        certificate=r'|CertDn|\|CertName|'
    )
    for result in file_validation_results:
        # Let's check the file validation results...
        ...
    for result in ssl_validation_results:
        # Let's check the SSL validation results...
        ...

Getting Certificate Data
------------------------

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(...)
    features = Features(api=api)

    details = features.certificate.details(
        certificate=r'|CertDn|\|CertName|'
    )
    print(f'Available attributes: {dir(details)}')

Associating/Dissociating A Certificate
--------------------------------------

.. code-block:: python

    from pytpp import Features, Authenticate

    api = Authenticate(...)
    features = Features(api=api)

    #### ASSOCIATE CERTIFICATE TO APPLICATION ####
    features.certificate.associate_application(
        certificate=r'|CertDn|\|CertName|',
        applications=[
            r'|AppDn|\|AppName| - 1',
            r'|AppDn|\|AppName| - 2'
        ],
        push_to_new=True
    )

    #### DISSOCIATE CERTIFICATE TO APPLICATION ####
    features.certificate.dissociate_application(
        certificate=r'|CertDn|\|CertName|',
        applications=[
            r'|AppDn|\|AppName| - 1',
            r'|AppDn|\|AppName| - 2'
        ],
        delete_orphans=True  # Orphaned applications will be deleted.
    )

Handling Workflows
------------------

.. note::
    See :ref:`workflow_usage` for more info on handling workflows and tickets.

.. code-block:: python

    from pytpp import Features, Authenticate, AttributeValues

    api = Authenticate(...)
    features = Features(api=api)

    certificate_dn = r'|CertDn|\|CertName|'

    current_thumbprint = features.certificate.renew(certificate=certificate_dn)

    #### Expect A Workflow Ticket ####
    certificate_details = features.certificate.wait_for_stage(
        certificate=certificate_dn,
        expect_workflow=True,
        stage=500
    ).certificate_details
    tickets = features.workflow.ticket.get(obj=certificate_dn)
    for ticket in tickets:
        ticket_info = features.workflow.ticket.details(ticket_name=ticket)
        if ticket_info.status == AttributeValues.Workflow.Status.pending:
            if certificate_details.key_algorithm != AttributeValues.Certificate.KeyAlgorithm.rsa:
                features.workflow.ticket.update_status(
                    ticket_name=ticket,
                    status=AttributeValues.Workflow.Status.rejected,
                    explanation='RSA is required.'
                )
            elif certificate_details.key_size < 2048:
                features.workflow.ticket.update_status(
                    ticket_name=ticket,
                    status=AttributeValues.Workflow.Status.rejected,
                    explanation='A minimum RSA key size of 2048 is required.'
                )
            else:
                features.workflow.ticket.update_status(
                    ticket_name=ticket,
                    status=AttributeValues.Workflow.Status.approved,
                    explanation='Looks good to me.'
                )

    #### Proceed To Wait For Renewal To Complete ####
    features.certificate.wait_for_enrollment_to_complete(certificate=certificate_dn, current_thumbprint=current_thumbprint)
