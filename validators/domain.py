import re

from .utils import validator

pattern = re.compile(
    r'^(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.)'
    r'{1,126}(?!\d+)[a-zA-Z\d]{1,63}$'
)


@validator
def domain(value):
    """
    Return whether or not given value is a valid domain.

    If the value is valid domain name this function returns ``True``, otherwise
    :class:`~validators.utils.ValidationFailure`.

    Examples::

        >>> domain('example.com')
        True

        >>> domain('example.com/')
        ValidationFailure(func=domain, ...)

    :param value: domain string to validate
    """
    return pattern.match(value)
