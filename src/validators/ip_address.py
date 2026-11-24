"""IP Address."""

# standard
from ipaddress import (
    AddressValueError,
    IPv4Address,
    IPv4Network,
    IPv6Address,
    IPv6Interface,
    IPv6Network,
    NetmaskValueError,
)
import re
from typing import Optional

# local
from .utils import validator


def _check_private_ip(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    if (
        any(
            value.startswith(l_bit)
            for l_bit in {
                "10.",  # private
                "192.168.",  # private
                "169.254.",  # link-local
                "127.",  # localhost
                "0.0.0.0",  # loopback #nosec
            }
        )
        or re.match(r"^172\.(?:1[6-9]|2\d|3[0-1])\.", value)  # private
        or re.match(r"^(?:22[4-9]|23[0-9]|24[0-9]|25[0-5])\.", value)  # broadcast
    ):
        return is_private

    return not is_private


# IPv6 counterparts of the IPv4 ranges that `_check_private_ip` treats as private
_PRIVATE_IPV6_NETWORKS = (
    IPv6Network("::/128"),  # unspecified
    IPv6Network("::1/128"),  # loopback
    IPv6Network("fc00::/7"),  # unique local (private)
    IPv6Network("fe80::/10"),  # link-local
    IPv6Network("fec0::/10"),  # site-local (deprecated)
    IPv6Network("ff00::/8"),  # multicast
)


def _check_private_ipv6(value: str, is_private: Optional[bool]):
    if is_private is None:
        return True
    # an interface accepts a bare address as well as CIDR notation
    address = IPv6Interface(value).ip
    if address.ipv4_mapped is not None:
        # ::ffff:a.b.c.d reaches the IPv4 host a.b.c.d
        return _check_private_ip(str(address.ipv4_mapped), is_private)
    # compare without the zone identifier
    address = IPv6Address(int(address))
    if any(address in network for network in _PRIVATE_IPV6_NETWORKS):
        return is_private

    return not is_private


@validator
def ipv4(
    value: str,
    /,
    *,
    cidr: bool = True,
    strict: bool = False,
    private: Optional[bool] = None,
    host_bit: bool = True,
):
    """Returns whether a given value is a valid IPv4 address.

    From Python version 3.9.5 leading zeros are no longer tolerated
    and are treated as an error. The initial version of ipv4 validator
    was inspired from [WTForms IPAddress validator][1].

    [1]: https://github.com/wtforms/wtforms/blob/master/src/wtforms/validators.py

    Examples:
        >>> ipv4('123.0.0.7')
        True
        >>> ipv4('1.1.1.1/8')
        True
        >>> ipv4('900.80.70.11')
        ValidationError(func=ipv4, args={'value': '900.80.70.11'})

    Args:
        value:
            IP address string to validate.
        cidr:
            IP address string may contain CIDR notation.
        strict:
            IP address string is strictly in CIDR notation.
        private:
            IP address is public if `False`, private/local/loopback/broadcast if `True`.
        host_bit:
            If `False` and host bits (along with network bits) _are_ set in the supplied
            address, this function raises a validation error. ref [IPv4Network][2].
            [2]: https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network

    Returns:
        (Literal[True]): If `value` is a valid IPv4 address.
        (ValidationError): If `value` is an invalid IPv4 address.
    """
    if not value:
        return False
    try:
        if cidr:
            if strict and value.count("/") != 1:
                raise ValueError("IPv4 address was expected in CIDR notation")
            return IPv4Network(value, strict=not host_bit) and _check_private_ip(value, private)
        return IPv4Address(value) and _check_private_ip(value, private)
    except (ValueError, AddressValueError, NetmaskValueError):
        return False


@validator
def ipv6(
    value: str,
    /,
    *,
    cidr: bool = True,
    strict: bool = False,
    private: Optional[bool] = None,
    host_bit: bool = True,
):
    """Returns if a given value is a valid IPv6 address.

    Including IPv4-mapped IPv6 addresses. The initial version of ipv6 validator
    was inspired from [WTForms IPAddress validator][1].

    [1]: https://github.com/wtforms/wtforms/blob/master/src/wtforms/validators.py

    Examples:
        >>> ipv6('::ffff:192.0.2.128')
        True
        >>> ipv6('::1/128')
        True
        >>> ipv6('abc.0.0.1')
        ValidationError(func=ipv6, args={'value': 'abc.0.0.1'})
        >>> ipv6('::1', private=False)
        ValidationError(func=ipv6, args={'value': '::1', 'private': False})

    Args:
        value:
            IP address string to validate.
        cidr:
            IP address string may contain CIDR annotation.
        strict:
            IP address string is strictly in CIDR notation.
        private:
            IP address is public if `False`, private/local/loopback/multicast if `True`.
            An IPv4-mapped address is judged by the IPv4 address it embeds.
        host_bit:
            If `False` and host bits (along with network bits) _are_ set in the supplied
            address, this function raises a validation error. ref [IPv6Network][2].
            [2]: https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network

    Returns:
        (Literal[True]): If `value` is a valid IPv6 address.
        (ValidationError): If `value` is an invalid IPv6 address.
    """
    if not value:
        return False
    try:
        if cidr:
            if strict and value.count("/") != 1:
                raise ValueError("IPv6 address was expected in CIDR notation")
            return IPv6Network(value, strict=not host_bit) and _check_private_ipv6(value, private)
        return IPv6Address(value) and _check_private_ipv6(value, private)
    except (ValueError, AddressValueError, NetmaskValueError):
        return False
