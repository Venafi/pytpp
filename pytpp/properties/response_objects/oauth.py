from pytpp.properties.response_objects.dataclasses import oauth


class OAuth:
    @staticmethod
    def Permissions(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return oauth.Permissions(
            delete=response_object.get('delete'),
            discover=response_object.get('discover'),
            manage=response_object.get('manage'),
            read=response_object.get('read'),
            revoke=response_object.get('revoke'),
        )
