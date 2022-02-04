.. _object_usage:

Object Management
=================

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Getting & Validating Config Objects
-----------------------------------

.. note::
    Most features have their own ``get()`` method. Using ``features.objects.get()`` is simply another way
    of getting the :ref:`config_object` of an object's :ref:`dn`.

.. rubric:: Getting Config Objects By DN
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### GET AN OBJECT ####
    certificate = features.objects.get(object_dn=r'|CertDn|\|CertName|')
    print(certificate.dn)

.. rubric:: Handling Objects That May Not Exist
.. code-block:: python

    from pytpp import Authenticate, Features
    from pytpp.features.definitions.exceptions import ObjectDoesNotExist

    api = Authenticate(...)
    features = Features(api)

    credential_dn = r'|CredDn|\|CredName|'

    #### VALIDATE EXISTENCE WITH TRY/EXCEPT ####
    try:
        credential = features.objects.get(object_dn=credential_dn)
    except ObjectDoesNotExist:
        print(f'Cannot find {credential_dn}.')

    #### VALIDATE EXISTENCE USING DN PROPERTY ####
    credential = features.objects.get(
        object_dn=credential_dn,
        raise_error_if_not_exists=False  # The default is True
    )
    if not credential.dn:
        print(f'Cannot find {credential_dn}.')

    #### VALIDATE EXISTENCE USING EXISTS() ####
    if not features.objects.exists(object_dn=credential_dn):
        print(f'Cannot find {credential_dn}.')

.. _read_attributes:

Reading Attributes
------------------

.. note::
    To read policy attributes for a particular class use :ref:`read_policy_attributes`.

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    #### READ A SINGLE ATTRIBUTE ####
    certiifcate_authority = features.objects.read(
        obj=r'|CertDn|\|CertName|',
        attribute_name=Attributes.certificate.certificate_authority,
        include_policy_values=True  # If False, only the explicit attribute on this object is read.
    )

    #### READ ALL ATTRIBUTES ####
    attributes = features.objects.read_all(obj=r'|CertDn|\|CertName|')
    certificate_authority = [attr.values[0] for attr in attributes if attr.name == Attributes.certificate.certificate_authority]

Writing Attributes
------------------

.. note::
    To write policy attributes for a particular class use :ref:`write_policy_attributes`.

.. warning::
    Writing attributes will override the existing value(s) for that particular attribute. To append to a list of
    attributes that may already exist, first read those values and then append the new values.

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes, AttributeValues

    api = Authenticate(...)
    features = Features(api)

    features.objects.write(
        obj=r'|CertDn|\|CertName|',
        attributes={
            Attributes.certificate.consumers: [r'|AppDn|\|AppName|'],
            Attributes.certificate.management_type: AttributeValues.Certificate.ManagementType.provisioning
        }
    )

Waiting For Attribute Values
----------------------------

.. note::
    Sometimes an operation is occurring that will create or update an attribute value on an object. For example, renewing a
    certificate will cause the *Stage* and *Status* attributes to populate. This is useful when you are expecting a value
    to be assigned to an attribute in some interval of time.

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    # Do some operation here.

    # Well, there is a certificate feature for this, but this is how it does it!
    features.objects.wait_for(
        obj=r'|CertDn|\|CertName|',
        attribute_name=Attributes.certificate.stage,
        attribute_value='500'
    )

Renaming Objects
----------------

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes

    api = Authenticate(...)
    features = Features(api)

    # This is used for renaming and/or moving objects.
    features.objects.rename(
        obj=r'|CertDn|\|CertName|',
        new_object_dn=obj=r'|CertDn|\|FolderName|\|CertName|',
    )
