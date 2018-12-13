# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

try:
    import numpy as np
except ImportError:
    np = None


def to_list(value, check_none=False):
    if check_none and value is None:
        return None
    if isinstance(value, (list, tuple, set)):
        return list(value)
    if np and isinstance(value, np.ndarray):
        return value.tolist()
    return [value]
