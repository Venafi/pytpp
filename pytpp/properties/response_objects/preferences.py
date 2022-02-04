from pytpp.properties.response_objects.dataclasses import preferences


class Preferences:
    @staticmethod
    def Preference(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return preferences.Preference(
            id=response_object.get('Id'),
            universal=response_object.get('Universal'),
            product=response_object.get('Product'),
            category=response_object.get('Category'),
            name=response_object.get('Name'),
            value=response_object.get('Value'),
            locked=response_object.get('Locked'),
        )
