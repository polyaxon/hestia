# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import os
import shutil


def move_recursively(src, dst):
    files = os.listdir(src)

    for f in files:
        shutil.move(os.path.join(src, f), dst)
