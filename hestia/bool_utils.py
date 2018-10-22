from distutils.util import strtobool  # pylint:disable=import-error


def to_bool(value, handle_none=False, exception=TypeError):
    if isinstance(value, str):
        value = strtobool(value)

    if value in (False, 0):
        return False

    if value in (True, 1):
        return True

    if handle_none and value is None:
        return False

    raise exception('The value `{}` cannot be interpreted as boolean'.format(value))
