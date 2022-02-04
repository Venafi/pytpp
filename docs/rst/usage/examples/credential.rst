.. _credential_usage:

Credential
==========

.. note::
    Refer to :ref:`authentication` for ways to authenticate to the TPP WebSDK.


Credential Types
----------------

Refer to :ref:`credentials_feature_list` for the available credential feature types. Please note that, though the
available feature type may not be listed, it doesn not mean that it cannot be used with the API layer, which is a
pure interface with the |Websdk|.

Creating & Deleting A Credential
--------------------------------
.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api=api)

    #### CREATE ####
    credential = features.credential.username_password.create(
        name='|CredName|',
        parent_folder=r'|CredDn|',
        username=r'|DomainUser|',
        password=r'SomePasword123!!!'
    )

    #### DELETE ####
    features.credential.username_password.delete(credential=credential)

Creating A Google Credential
----------------------------

.. code-block:: text
    :name: google_credential.json

    {
        "type"                       : "service_account",
        "project_id"                 : "********",
        "private_key_id"             : "********",
        "private_key"                : "-----BEGIN PRIVATE KEY-----\n********-----END PRIVATE KEY-----\n",
        "client_email"               : "service@********.iam.gserviceaccount.com",
        "client_id"                  : "********",
        "auth_uri"                   : "https://accounts.google.com/o/oauth2/auth",
        "token_uri"                  : "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url"       : "https://www.googleapis.com/robot/v1/metadata/x509/********.iam.gserviceaccount.com"
    }

.. code-block:: python

    from pytpp import Authenticate, Features

    api = Authenticate(...)
    features = Features(api=api)

    with open('google_credential.json', 'r') as f:
        json_content = f.read()

    credential = features.credential.google.create(
        name='|CredName|',
        parent_folder=r'|CredDn|',
        description='Google credential description.',
        contacts=['|LocalUser|', '|DomainUser|'],
        json_content=json_content
    )
