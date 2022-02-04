from pytpp.properties.response_objects.dataclasses import identity


class Identity:
    @staticmethod
    def Identity(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return identity.Identity(
            full_name=response_object.get('FullName'),
            is_container=response_object.get('IsContainer'),
            is_group=response_object.get('IsGroup'),
            name=response_object.get('Name'),
            prefix=response_object.get('Prefix'),
            prefixed_name=response_object.get('PrefixedName'),
            prefixed_universal=response_object.get('PrefixedUniversal'),
            type=response_object.get('Type'),
            universal=response_object.get('Universal'),
        )

    @staticmethod
    def InvalidIdentity(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return identity.InvalidIdentity(
            prefix=response_object.get('Prefix'),
            prefixed_name=response_object.get('PrefixedName'),
            prefixed_universal=response_object.get('PrefixedUniversal'),
            universal=response_object.get('Universal'),
        )
