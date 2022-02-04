.. _application_usage:

Application
===========

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.

Application Types
-----------------

Refer to :ref:`application_feature_list` for the available application feature types.

Creating & Deleting Applications
--------------------------------

.. code-block:: python

    from pytpp import AttributeValues, Attributes, Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### CREATE ####

    application = features.application.apache.create(
        name='|AppName|',
        device=r'|AppDn|',
        contacts=['|LocalUser|', '|DomainUser|']
        private_key_file='/etc/example/private_key.p12',
        certificate_file='/etc/example/cert.crt',
    )

    #### DELETE ####

    features.application.apache.delete(application=application)

Enabling & Disabling Applications
---------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    #### ENABLE ####
    features.application.apache.enable(application=r'|AppDn|\|AppName|')

    #### DISABLE ####
    features.application.apache.disable(application=r'|AppDn|\|AppName|')

Getting Application Certificate
-------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    certificate = features.application.apache.get_associated_certificate(application=r'|AppDn|\|AppName|')

Getting Processing Stage & Status
---------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    stage = features.application.apache.get_stage(application=r'|AppDn|\|AppName|')
    status = features.application.apache.get_status(application=r'|AppDn|\|AppName|')

Installing A Certificate To An Application
------------------------------------------

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api)

    # Push an existing certificate to the application.
    certificate = features.application.apache.get_associated_certificate(application=r'|AppDn|\|AppName|')
    features.certificate.push_to_applications(
        certificate=certificate,
        applications=[r'|AppDn|\|AppName|']
    )

    # Wait 2 minutes for the installation to complete.
    features.application.apache.wait_for_installation_to_complete(application=r'|AppDn|\|AppName|', timeout=120)
