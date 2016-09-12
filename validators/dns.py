import re

from .utils import validator


pattern = re.compile(
    r'^((?![0-9]{1,63}[.])(?![0-9]+$)'
    r'(?!-)([a-zA-Z0-9-_]{0,63}(?<!-)([.])?)){1,32}$'
)


@validator
def hostname(value):
    """
    Return whether or not given value is a valid hostname (label)
    for DNS records.
    For more details https://www.ietf.org/rfc/rfc1912.txt

    If the value is valid label this function returns ``True``, otherwise
    :class:`~validators.utils.ValidationFailure`.

    Examples::

        >>> hostname('example')
        True

        >>> hostname('example-label')
        True

        >>> hostname('-host')
        ValidationFailure(func=hostname, ...)


    Supports IDN labels as well::

        >>> hostname('xn----gtbspbbmkef')
        True

    :param value: hostname string to validate
    """
    return pattern.match(value)
