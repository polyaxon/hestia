# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import pytz

from datetime import datetime

try:
    from django.utils.timezone import now as dj_now
except Exception:
    dj_now = None


utc = pytz.utc


def now(tzinfo=True):
    """
    Return an aware or naive datetime.datetime, depending on settings.USE_TZ.
    """
    if dj_now:
        return dj_now()

    if tzinfo:
        # timeit shows that datetime.now(tz=utc) is 24% slower
        return datetime.utcnow().replace(tzinfo=utc)
    else:
        return datetime.now()
