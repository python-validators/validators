"""IP Address."""

# standard
from ipaddress import (
    AddressValueError,
    IPv4Address,
    IPv4Network,
    IPv6Address,
    IPv6Network,
    NetmaskValueError,
)

# local
from .utils import validator


@validator
def ipv4(value: str, /, *, cidr: bool = True, strict: bool = False):
    """Returns whether a given value is a valid IPv4 address.

    From Python version 3.9.5 leading zeros are no longer tolerated
    and are treated as an error. The initial version of ipv4 validator
    was inspired from [WTForms IPAddress validator][1].

    [1]: https://github.com/wtforms/wtforms/blob/master/src/wtforms/validators.py

    Examples:
        >>> ipv4('123.0.0.7')
        # Output: True
        >>> ipv4('1.1.1.1/8')
        # Output: True
        >>> ipv4('900.80.70.11')
        # Output: ValidationError(func=ipv4, args={'value': '900.80.70.11'})

    Args:
        value:
            IP address string to validate.
        cidr:
            IP address string may contain CIDR annotation
        strict:
            If strict is True and host bits are set in the supplied address.
            Otherwise, the host bits are masked out to determine the
            appropriate network address. ref [IPv4Network][2].
            [2]: https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network

    Returns:
        (Literal[True]):
            If `value` is a valid IPv4 address.
        (ValidationError):
            If `value` is an invalid IPv4 address.

    Note:
        - *In version 0.14.0*:
            - Add supports for CIDR notation

    > *New in version 0.2.0*
    """
    if not value:
        return False
    try:
        if cidr and value.count("/") == 1:
            return IPv4Network(value, strict=strict)
        return IPv4Address(value)
    except (AddressValueError, NetmaskValueError):
        return False


@validator
def ipv6(value: str, /, *, cidr: bool = True, strict: bool = False):
    """Returns if a given value is a valid IPv6 address.

    Including IPv4-mapped IPv6 addresses. The initial version of ipv6 validator
    was inspired from [WTForms IPAddress validator][1].

    [1]: https://github.com/wtforms/wtforms/blob/master/src/wtforms/validators.py

    Examples:
        >>> ipv6('::ffff:192.0.2.128')
        # Output: True
        >>> ipv6('::1/128')
        # Output: True
        >>> ipv6('abc.0.0.1')
        # Output: ValidationError(func=ipv6, args={'value': 'abc.0.0.1'})

    Args:
        value:
            IP address string to validate.
        cidr:
            IP address string may contain CIDR annotation
        strict:
            If strict is True and host bits are set in the supplied address.
            Otherwise, the host bits are masked out to determine the
            appropriate network address. ref [IPv6Network][2].
            [2]: https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network

    Returns:
        (Literal[True]):
            If `value` is a valid IPv6 address.
        (ValidationError):
            If `value` is an invalid IPv6 address.

    Note:
        - *In version 0.14.0*:
            - Add supports for CIDR notation

    > *New in version 0.2.0*
    """
    if not value:
        return False
    try:
        if cidr and value.count("/") == 1:
            return IPv6Network(value, strict=strict)
        return IPv6Address(value)
    except (AddressValueError, NetmaskValueError):
        return False
