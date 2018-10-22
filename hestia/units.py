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
