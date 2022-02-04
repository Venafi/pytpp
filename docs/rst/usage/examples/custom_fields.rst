.. _custom_field_usage:

Custom Field
============

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Creating Custom Fields
----------------------

.. note::
    There are many options when creating custom fields. Refer to the *POST Metadata/DefineItem* API in the |Doc Home Page|
    to get more info on possible inputs.

.. code-block:: python

    from pytpp import Authenticate, Features, Attributes, AttributeValues

    api = Authenticate(...)
    features = Features(api)

    ### CREATE ####
    custom_field = features.custom_fields.create(
        label='|CustomFieldName|',
        name='|CustomFieldName|',
        classes=[Attributes.certificate.__config_class__],
        data_type=AttributeValues.CustomField.Type.text_string,
        allowed_values=[
            'Option 1',
            'Option 2'
        ],
        default_values=['Option 1'],
        error_message='You can only choose from these valid options: "Option 1", "Option 2".',
        help_text='Choose from "Option 1" or "Option 2".',
        mandatory=True,
        policyable=True,
        regular_expression='^[a-zA-Z0-9\s]*$',
        render_hidden=False,
        render_read_only=False,
        single=True
    )

    #### DELETE ####
    features.custom_fields.delete(custom_field='|CustomFieldName|', remove_data=True)

Reading Custom Fields
---------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### READ OBJECT ATTRIBUTES ####
    result_on_object = features.custom_fields.read(
        obj=r'|CertDn|\|CertDn|',
        custom_field='Team Name'
    )
    print(f'VALUES: {result_on_object.values}')
    print(f'LOCKED: {result_on_object.locked}')
    print(f'POLICY: {result_on_object.policy_dn}')

    #### READ POLICY ATTRIBUTES ####
    result_on_policy = features.custom_fields.read_policy(
        folder=r'|CertDn|',
        custom_field='Team Name',
        class_name=Attributes.device.__config_class__
    )
    print(f'POLICY VALUES: {result_on_policy.values}')
    print(f'LOCKED: {result_on_policy.locked}')

Writing Custom Fields
---------------------

.. rubric:: Write Custom Field To An Object

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### WRITE CUSTOM FIELD VALUE TO OBJECT ####
    features.custom_fields.write(
        obj=r'|CertDn|\|CertName|',
        custom_field='Team Name',
        values=['Awesome Team']
    )

    #### WRITE CUSTOM FIELD VALUE TO POLICY ####
    features.custom_fields.write_policy(
        folder=r'|CertDn|',
        custom_field='Team Name',
        class_name=Attributes.device.__config_class__,
        values=['Awesome Team'],
        locked=True
    )
