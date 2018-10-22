from hestia.exceptions import HestiaException

try:
    from rest_framework import HTTP_HEADER_ENCODING
except ImportError:
    raise HestiaException('This module depends on django-rest-framework.')


def get_header(request, header_service):
    """Return request's 'X_POLYAXON_...:' header, as a bytestring.

    Hide some test client ickyness where the header can be unicode.
    """
    service = request.META.get('HTTP_{}'.format(header_service), b'')
    if isinstance(service, str):
        # Work around django test client oddness
        service = service.encode(HTTP_HEADER_ENCODING)
    return service
