# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from hestia.exceptions import HestiaException

try:
    import requests
except ImportError:
    raise HestiaException('This module depends on requests.')


def safe_request(
    url,
    method=None,
    params=None,
    data=None,
    json=None,
    headers=None,
    allow_redirects=False,
    timeout=30,
    verify_ssl=True,
):
    """A slightly safer version of `request`."""

    session = requests.Session()

    kwargs = {}

    if json:
        kwargs['json'] = json
        if not headers:
            headers = {}
        headers.setdefault('Content-Type', 'application/json')

    if data:
        kwargs['data'] = data

    if params:
        kwargs['params'] = params

    if headers:
        kwargs['headers'] = headers

    if method is None:
        method = 'POST' if (data or json) else 'GET'

    response = session.request(
        method=method,
        url=url,
        allow_redirects=allow_redirects,
        timeout=timeout,
        verify=verify_ssl,
        **kwargs
    )

    return response
