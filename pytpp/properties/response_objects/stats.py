from pytpp.properties.response_objects.dataclasses import stats
from pytpp.tools.helpers.date_converter import from_date_string


class Stats:
    @staticmethod
    def Counter(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return stats.Counter(
            a_name=response_object.get('AName'),
            b_name=response_object.get('BName'),
            c_name=response_object.get('CName'),
            description=response_object.get('Description'),
            name=response_object.get('Name'),
            stats_type=response_object.get('StatsType'),
        )

    @staticmethod
    def Result(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return stats.Result(
            key=Stats.Key(response_object.get('Key')),
            value=[Stats.Value(value) for value in response_object.get('Value')],
        )

    @staticmethod
    def Key(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return stats.Key(
            m_item1=response_object.get('m_Item1'),
            m_item2=response_object.get('m_Item2'),
            m_item3=response_object.get('m_Item3'),
        )

    @staticmethod
    def Value(response_object: dict):
        if not isinstance(response_object, dict):
            response_object = {}
        return stats.Value(
            count=response_object.get('Count', 0),
            sum_value=response_object.get('SumValue', 0),
            tag_a=response_object.get('TagA'),
            tag_b=response_object.get('TagB'),
            tag_c=response_object.get('TagC'),
            time_frame=from_date_string(response_object.get('TimeFrame')),
            type=response_object.get('Type'),
        )
