Usage Guide
============

Authentication
--------------

.. note::
    Be sure to check out the :ref:`pytpp-requirements` and :ref:`oauth_setup` to configure your API Application
    Integration in Aperture. Only OAuth authentication is supported. Be sure to use the appropriate OAuth scope.

Here are a few different ways to authenticate to TPP:

    * :ref:`username_password_auth`
    * :ref:`certificate_auth`
    * :ref:`reuse_oauth_token_auth`
    * :ref:`proxy_auth`

The API Layer
-------------

.. note::
    The API layer is the interface to the TPP WebSDK API and is updated to the latest released version of TPP. Be
    sure that the API calls you make are compatible with your version of TPP. You can reference the Venafi
    |Doc Home Page| for details of using the WebSDK API.

The API layer is responsible for making API requests and serializing the response from TPP.

.. rubric:: Calling API Methods

The path of the URL for the WebSDK API is translated to Python by following this format:

.. code-block::

    Given: POST Config/IsValid
    BODY:
        {
            'ObjectDN': '\\VED\\Policy'
        }
    RESULT:
        {
           "Object":{
              "AbsoluteGUID":"{1aed731d-3db6-4f61-b186-9c05ea486df8} \
                 {981c0b88-bbf7-4a87-b5ee-b328dce41b75} \
                 {112adf57-07b7-41fe-9d3a-5f342e421c68}",
              "DN":"\\VED\\Policy",
              "GUID":"{112adf57-07b7-41fe-9d3a-5f342e421c68}",
              "Id":3,
              "Name":"Policy",
              "Parent":"\\VED",
              "Revision":1640,
              "TypeName":"Policy"
           },
           "Result":1
        }

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)

    # The response is not validated until either a property of the return object is called
    # or the response is explicitly validated.
    response = api.websdk.Config.IsValid.post(object_dn=r'\VED\Policy')

    # The response can be explicitly validated.
    response.assert_valid_response()
    # -- OR --
    if not response.is_valid_response():
        raise AssertionError()

    # The response can be automatically validate by calling one of the returned properties.
    # In this case it is ".object".
    policy = response.object
    print(policy.dn)  # Print the Policy DN.

Note that the response body returned by TPP is also serialized to a Python object. For example:

.. code-block::

    Given: POST Config/IsValid -> {"Object": {"DN": "...", ...}}
    Then: Access the DN -> response.object.dn

The Features Layer
------------------

Features are abstractions of WebSDK APIs to give a higher-level logical interface to TPP, such as creating discovery
jobs and managing permissions.

.. rubric:: API vs Features: Creating A Certificate
.. code-block:: python

    from pytpp import Authenticate, Features, Attributes, AttributeValues

    api = Authenticate(...)
    features = Features(api)

    # Using the API layer
    response = api.websdk.Config.Create.post(
        object_dn=r'\VED\Policy\Certificates\my-site.com',
        class_name=Attributes.certificate,
        name_attribute_list=[
            {"Name": Attributes.certificate.description, "Value": "Description Here."},
            {"Name": Attributes.certificate.contact, "Value": ['local:{bc628602-36fc-4116-a0b4-2a3d5e92c776}']},
            {"Name": Attributes.certificate.approver, "Value": ['local:{bc628602-36fc-4116-a0b4-2a3d5e92c776}']},
            {"Name": Attributes.certificate.management_type, "Value": AttributeValues.Certificate.ManagementType.enrollment},
            {"Name": Attributes.certificate.manual_csr, "Value": "1"},
            {"Name": Attributes.certificate.generate_keypair_on_application, "Value": "0"},
            {"Name": Attributes.certificate.pkcs10_hash_algorithm, "Value": AttributeValues.Certificate.HashAlgorithm.sha256},
            {"Name": Attributes.certificate.x509_subject, "Value": "my-site.com"},
            {"Name": Attributes.certificate.organization, "Value": "My Organization"},
            {"Name": Attributes.certificate.organizational_unit, "Value": ["OU1", "OU2"]},
            {"Name": Attributes.certificate.city, "Value": "Salt Lake City"},
            {"Name": Attributes.certificate.state, "Value": "UT"},
            {"Name": Attributes.certificate.country, "Value": "US"},
            {"Name": Attributes.certificate.driver_name, "Value": 'appx509certificate'},
            {"Name": Attributes.certificate.x509_subjectaltname_dns, "Value": "my-site.com"},
            {"Name": Attributes.certificate.x509_subjectaltname_ipaddress, "Value": "10.10.10.10"},
            {"Name": Attributes.certificate.key_algorithm, "Value": AttributeValues.Certificate.KeyAlgorithm.rsa},
            {"Name": Attributes.certificate.key_bit_strength, "Value": 2048},
            {"Name": Attributes.certificate.certificate_authority, "Value": r'\VED\Policy\Administration\CA\MyCA'},
            {"Name": Attributes.certificate.disable_automatic_renewal, "Value": "0"},
            {"Name": Attributes.certificate.renewal_window, "Value": 30}
        ]
    )
    certificate = response.object

    # Using the Features layer
    features_certificate = features.certificate.create(
        name='my-site.com', parent_folder=r'\VED\Policy\Certificates',
        description="Description Here.",
        contacts=['local:user123'],
        approvers=['local:user123'],
        management_type=AttributeValues.Certificate.ManagementType.enrollment,
        service_generated_csr=True,
        generate_key_on_application=False,
        hash_algorithm=AttributeValues.Certificate.HashAlgorithm.sha256,
        common_name="my-site.com",
        organization="My Organization",
        organization_unit=["OU1", "OU2"],
        city="Salt Lake City",
        state="UT",
        country="US",
        san_dns=["my-site.com"],
        san_ip=["10.10.10.10"],
        key_algorithm=AttributeValues.Certificate.KeyAlgorithm.rsa,
        key_strength=2048,
        ca_template=r'\VED\Policy\Administration\CA\MyCA',
        disable_automatic_renewal=False,
        renewal_window=30
    )

Common Terminology
------------------

.. _dn:
.. rubric:: Distinguished Name (DN)

A **Distinguished Name (DN)** is the path to an object relative to ``\\VED``, the root of the tree.
Policies are most commonly found under ``\VED\Policy`` and because that is so the Features layer can
interpret paths relative to *\\VED\\Policy*. For example:

``\VED\Policy\Certificates = \Policy\Certificates``.

.. _guid:
.. rubric:: GUID

A **GUID** typically refers to the GUID of the object referenced. This usually isn't as readily used
as a DN, but is commonly used in the WebSDK API and is part of the Config Object described below.

.. _prefixed_name:
.. rubric:: Prefixed Name

A **Prefixed Name** refers to an identity's friendly name prepended by its identity provider's prefix
stored in TPP. For example, for user *user123* the prefixed universal for the

    * local identity is ``local:user123``.
    * one of the active directory identities is ``AD+MyAd:user123``.

Config And Identity Objects
---------------------------

.. _config_object:
.. rubric:: Config Object

.. note::
    All feature-level inputs accepting ``Config.Object`` also accept :ref:`dn` and :ref:`guid` values.

Config Objects are the basic definition of every object that can be created in TPP. Every feature with a
``create()``, ``get()``, or ``update()`` method will return a ``Config.Object``, which is defined below.

.. csv-table:: Config.Object
    :widths: auto
    :stub-columns: 1
    :align: center
    :header: "Property", "Description"

    "absolute_guid", "The absolute GUID of the object."
    "dn", "The distinguished name (DN), or absolute path, of the object."
    "guid", "The GUID of the object."
    "config_id", "The Config ID of the object."
    "name", "The name of the object."
    "parent", "The parent DN of the object."
    "revision", "The revision of the object."
    "type_name", "The class name of the object."

Many features have parameters typed as ``Union[Config.Object, str]``. In these instances the parameter is
requiring a ``Config.Object`` or a :ref:`dn` value.

**Example Usage**

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    certificate_folder = features.folder.get(object_dn=r'\VED\Policy\Certificates') # This is a Config.Object
    print(f'Absolute GUID : {certificate_folder.absolute_guid}')
    print(f'DN            : {certificate_folder.dn}')
    print(f'GUID          : {certificate_folder.guid}')
    print(f'Config ID     : {certificate_folder.config_id}')
    print(f'Name          : {certificate_folder.name}')
    print(f'Parent        : {certificate_folder.parent}')
    print(f'Revision      : {certificate_folder.revision}')
    print(f'Class Name    : {certificate_folder.type_name}')

    certificate = features.certificate.create(
        name='my-cert.com',
        parent_folder=certificate_folder,
        # OR parent_folder=certificate_folder.dn
        # OR parent_folder=r'\VED\Policy\Certificates'
    )

.. _identity_object:
.. rubric:: Identity Object

.. note::
    All feature-level inputs accepting ``Identity.Identity`` also accept :ref:`prefixed_name` values.

The ``Identity`` object is much like the *Confg.Object* except that it applies to users and groups, or identities.
All identities in TPP share common properties that make up this class.

.. csv-table:: Identiy (Identity.Identity)
    :widths: auto
    :stub-columns: 1
    :align: center
    :header: "Property", "Description"

    "full_name", "The full name of the user or group."
    "is_group", "True if the identity is a group, otherwise False."
    "name", "The name of the user or group."
    "prefix", "The identity provider prefix that manages the user or group."
    "prefixed_name", "The concatenation of the prefix and identity name."
    "prefixed_universal", "The concatenation of the prefix and identity universal ID."
    "type", "The integer identifier that describes the identity type."
    "universal", "The Universal Unique ID that identifies a user or group identity."

Many features have parameters typed as ``Union[Identity.Identity, str]``. In these instances the parameter is
requiring an ``Identity.Identity`` or a :ref:`prefixed_name` value.

**Example Usage**

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    user = features.identity.user.get(prefixed_name='local:special-user')
    print(f'Full Name          : {user.full_name}')
    print(f'Is A Group         : {user.is_group}')
    print(f'Name               : {user.name}')
    print(f'Prefix             : {user.prefix}')
    print(f'Prefixed Name      : {user.prefixed_name}')
    print(f'Prefixed Universal : {user.prefixed_universal}')
    print(f'Type               : {user.type}')
    print(f'Universal          : {user.universal}')

    features.permissions.get_effective(
        obj=r'\VED\Poilcy',
        identity=user,
        # OR identity='local:special-user'
    )

Attribute, AttributeValues, and Class Names
-------------------------------------------

.. rubric:: Attributes and AttributeValues

Every object in TPP has attributes that define that object. We create all of the attributes dynamically every
quarter by pulling them from the product XML definitions so that you can know its value and version
compatibility.

.. code-block:: python

    from pytpp import Attributes

    # This will show that the Certificate attribute on the Apache Application Group is TPP 19.4.
    # This means that the attribute has no effect on versions prior to then.
    print(Attributes.application_group.apache.certificate.min_version)

In rare cases you may need to access attributes that are not available using ``Attributes`` whose design is to
make it easy to find and use the common attributes for each feature. In order to access other attributes you
will need to import the attribute class directly. Use this naming convention to find the particular class and
attribute:

.. code-block:: python

    #from pytpp.attributes.<object class> import <object class>Attributes
    from pytpp.attributes.apache import ApacheAttributes

    # That is the equivalent to this:
    from pytpp import Attributes

    print(Attributes.application.apache == ApacheAttributes)  # prints "True"

Some attributes expect one of a few permitted values, and for those cases you can benefit from ``AttributeValues``.
The attribute values are collected manually through options made available in Web Admin and Aperture and for this
reason we have this naming convention:

.. code-block:: python

    from pytpp import AttributeValues

    # AttributeValues.<object class>.<attribute name in the UI>.<attribute value in the UI>
    print(AttributeValues.Certificate.ManagementType.enrollment)

Please be forgiving because there is currently no way to automatically retireve all possible values from attributes
that only interpret a limited list of values.

.. code-block:: python

    from pytpp import Attributes, AttributeValues

    # This pair references the OS Type of a Device object. This will print:
    # Remote Server Type = OS_WINDOWS
    print(f'{Attributes.device.remote_server_type} = {AttributeValues.Device.OSType.windows}')

.. rubric:: Class Names

Every object in TPP has a class name. It is sometimes necessary to use the class name when searching, creating,
or setting policy values. There are two ways to get a class name:

.. code-block:: python

    from pytpp import Attributes, ClassNames

    print(ClassNames.x509_certificate == Attributes.certificate.__config_class__)

Notice that in the example above that ``ClassNames.x509_certificate`` is the actual class name of a certificate object
and that ``Attributes.certificate.__config_class__`` uses a friendly name approach. Here the ``__config_class__`` is
a special property of the class name for all attribute classes.

Type Hinting
------------

Programming in Python is much easier when the code uses type hints. |Product| was made to autocomplete everything in an
IDE, and we highly value autocompleting features. For this reason we have ``Types``. Here's how to use it:

.. code-block:: python

    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from pytpp import Types

    def do_something(certificate: 'Types.Config.Object') -> 'Types.Identity.Identity':
        ...

Logging
-------

.. warning::

    Only enable logging for debugging purposes. It is not recommended to enable logging in Production. Logging can
    potentially log sensitive information, such as private keys or credentials.

|Product| uses `logboss <https://pypi.org/project/logboss>`_ to log the inputs and outputs to each API and Feature
call. By default, the logger is turned off. To use the logger:

.. code-block:: python

    from pytpp import logger

    # Log to the console only.
    logger.start()

    # ---- OR ----
    # Redirect the log output to a text file. The path doesn't need to exist.
    logger.redirect = '/path/to/log.txt'
    logger.start()

    # ---- OR ----
    # Generate an HTML file output. Only use this option if you know what is being logged as the
    # HTML file could get too large to be usable.
    with logger.generate('html', log_file='/path/to/log.html', include_code=False):
        ...

Visit the LogBoss documentation for more usage information.

Parameter Interchangeability
----------------------------

**Config Objects**

:ref:`config_object`, :ref:`dn`, and :ref:`guid` are interchangeable. The object's name is included in these cases:

* Client Groups
* Client Work
* Custom Fields
* Discoveries
* Platforms
* Reason Codes
* Workflows Tickets

**Identity Objects**

:ref:`identity_object` and :ref:`prefixed_name` are always interchangeable.
