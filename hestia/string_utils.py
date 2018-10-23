# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function


def strip_spaces(value, sep=None, join=True):
    """Cleans trailing whitespaces and replaces also multiple whitespaces with a single space."""
    value = value.strip()
    value = [v.strip() for v in value.split(sep)]
    join_sep = sep or ' '
    return join_sep.join(value) if join else value
