# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

try:
    import numpy as np
except ImportError:
    np = None


def sanitize_np_types(value):
    if isinstance(value, (int, float, complex, type(None))):
        return value
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    return value
