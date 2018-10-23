# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function


def to_unit_memory(number):
    """Creates a string representation of memory size given `number`."""
    kb = 1024

    number /= kb

    if number < 100:
        return '{} Kb'.format(round(number, 2))

    number /= kb
    if number < 300:
        return '{} Mb'.format(round(number, 2))

    number /= kb

    return '{} Gb'.format(round(number, 2))


def to_percentage(number, rounding=2):
    """Creates a percentage string representation from the given `number`. The
    number is multiplied by 100 before adding a '%' character.

    Raises `ValueError` if `number` cannot be converted to a number.
    """
    number = float(number) * 100
    number_as_int = int(number)
    rounded = round(number, rounding)

    return '{}%'.format(number_as_int if number_as_int == rounded else rounded)
