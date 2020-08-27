from datetime import datetime
from time import mktime

import pytz

def date_to_utc(date):
    utc_millis = int(mktime(date.timetuple()) * 1000)
    return utc_millis


def timestamp_to_datetime(ts):
    ts = int(ts/1000)
    return datetime.utcfromtimestamp(ts)

def get_datetime_now():
    return datetime.now().replace(tzinfo=pytz.utc)

