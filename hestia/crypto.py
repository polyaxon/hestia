from hestia.exceptions import HestiaException

try:
    from django.utils.crypto import salted_hmac
except ImportError:
    raise HestiaException('This module depends on django.')


def get_hmac(key_salt, value):
    return salted_hmac(key_salt, value).hexdigest()
