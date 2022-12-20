import re

from .utils import validator

"""
sources:
https://regexr.com/3dt4r
"""
hostname_re = re.compile(
    r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(([a-zA-Z0-9]|["
    r"a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)+([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$",
    re.IGNORECASE)


def to_unicode(obj, charset='utf-8', errors='strict'):
    if obj is None:
        return None
    if not isinstance(obj, bytes):
        return str(obj)
    return obj.decode(charset, errors)


@validator
def hostname(value: str):
    """
    Return whether a given value is a valid hostname.
    If the value is valid hostname this function returns ``True``, otherwise
    :class:`~validators.utils.ValidationFailure`.
    Examples::
        >>>
        True
    :param value: hostname string to validate
    to the end if the procided value and validation retried)
    """
    try:
        return hostname_re.match(to_unicode(value).encode('idna').decode('ascii'))
    except (UnicodeError, AttributeError):
        return False
