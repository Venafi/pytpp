.. _certificate_authority_usage:

Certificate Authority
=====================

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Certificate Authority Types
---------------------------

The certificate authority feature is still under development and further Certificate Authority types will be implemented
as needed. See :ref:`certificate_authorities_feature_list` for a list of supported Certificate Authority types.


Creating & Deleting A Certificate Authority
-------------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Create the CA.
     msca = features.certificate_authority.msca.create(
        name='|CaName|',
        parent_folder=r'|CaDn|',
        contacts=['|LocalUser|', '|DomainUser|']
        hostname='awesomeca.my-company.com',
        service_name='AwesomeCA',
        template='AwesomeTemplate',
        credential=r'|CredDn|\|CredName|'
    )

    # Delete the CA.
    features.certificate_authority.msca.delete(certificate_authority=msca)
