# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import re

from dateutil import parser

from hestia.tz_utils import now

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S %Z"
ISO_DATETIME_REGEX = re.compile(
    '([0-9]+)-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])[Tt]'
    '([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\\.[0-9]+)?'
    '(([Zz])|([\\+|\\-]([01][0-9]|2[0-3]):[0-5][0-9]))\s')
DATETIME_REGEX = re.compile(r'\d{2}(?:\d{2})?-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}\s\w+\s')


def timestamp_search_regex(regex, log_line, convert=False):
    log_search = regex.search(log_line)
    if not log_search:
        return log_line, None

    ts = log_search.group()
    if convert:
        ts = parser.parse(ts).strftime(DATETIME_FORMAT)

    return re.sub(regex, '', log_line), ts


def log_spec(log_line, name='', timestamp=None, log_level=None, check_timestamp=True):
    if not timestamp and check_timestamp:
        log_line, timestamp = timestamp_search_regex(ISO_DATETIME_REGEX, log_line, convert=True)
        if not timestamp:
            log_line, timestamp = timestamp_search_regex(DATETIME_REGEX, log_line, convert=False)

    return '{timestamp}{log_level}{name} -- {log_line}'.format(
        log_line=log_line,
        name=' {}'.format(name) if name else '',
        timestamp=timestamp.strip() if timestamp else now(tzinfo=True).strftime(DATETIME_FORMAT),
        log_level=' {}'.format(log_level) if log_level else '')


LogSpec = log_spec
