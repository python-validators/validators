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
import re
from typing import Optional, Union

# local
from .utils import validator


def _check_private_ip(
    addr: Union[IPv4Address, IPv6Address, IPv4Network, IPv6Network], is_private: Optional[bool]
):
    """Check if the given IP address is private or public."""
    if is_private is None:
        return True

    if (
        addr.is_private
        or addr.is_loopback
        or addr.is_link_local
        or addr.is_multicast
        or addr.is_reserved
        or addr.is_unspecified
    ):
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
            addr = IPv4Network(value, strict=not host_bit)
            return addr and _check_private_ip(addr, private)
        addr = IPv4Address(value)
        return addr and _check_private_ip(addr, private)
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

    Args:
        value:
            IP address string to validate.
        cidr:
            IP address string may contain CIDR annotation.
        strict:
            IP address string is strictly in CIDR notation.
        private:
            IP address is public if `False`, private/local/loopback/multicast if `True`.
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
            addr = IPv6Network(value, strict=not host_bit)
            return addr and _check_private_ip(addr, private)
        addr = IPv6Address(value)
        return addr and _check_private_ip(addr, private)
    except (ValueError, AddressValueError, NetmaskValueError):
        return False
