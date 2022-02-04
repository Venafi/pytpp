from pytpp.properties.response_objects.dataclasses import rights


class Rights:
    @staticmethod
    def Rights(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return rights.Rights(
            checksum=response_object.get('Checksum'),
            is_container=response_object.get('IsContainer'),
            is_group=response_object.get('IsGroup'),
            object=response_object.get('Object'),
            principal=response_object.get('Principal'),
            rights=response_object.get('Rights'),
            sub_system=response_object.get('SubSystem'),
        )
