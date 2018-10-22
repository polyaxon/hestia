import pytz

from datetime import datetime

try:
    from django.utils.timezone import now
except ImportError:
    now = None


utc = pytz.utc


def now(tzinfo=None):
    """
    Return an aware or naive datetime.datetime, depending on settings.USE_TZ.
    """
    if now:
        return now

    if tzinfo:
        # timeit shows that datetime.now(tz=utc) is 24% slower
        return datetime.utcnow().replace(tzinfo=utc)
    else:
        return datetime.now()
