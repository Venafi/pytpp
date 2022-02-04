from typing import Union
from datetime import datetime, timezone, timedelta
from dateutil.parser import parse
import isodate


def from_date_string(date_string: str, duration_format: bool = False) -> Union[None, datetime]:
    if not date_string:
        return None

    if duration_format:
        return isodate.parse_duration(datestring=date_string)

    if 'Date' in date_string:
        date_as_num = ''.join([c for c in date_string if c.isnumeric() or c in ('+', '-')])
        if '+' in date_as_num:
            dt, tz = date_as_num.split('+')
            tz = timezone(timedelta(hours=int(tz) / 100))
        elif '-' in date_as_num:
            dt, tz = date_as_num.split('-')
            tz = timezone(timedelta(hours=int(tz)/100))
        else:
            dt, tz = date_as_num, None
        date_as_float = float(int(dt) / 1000)
        return datetime.fromtimestamp(date_as_float, tz=tz)

    else:
        return parse(date_string)
