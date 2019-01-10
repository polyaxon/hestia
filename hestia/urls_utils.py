from hestia.exceptions import HestiaException

try:
    from urllib.parse import urlparse  # pylint:disable=import-error
except ImportError:
    raise HestiaException('This module depends on python3.')


def validate_url(url):
    if not url.startswith(('http://', 'https://')):
        return False
    parsed = urlparse(url)
    if not parsed.hostname:
        return False
    return True
