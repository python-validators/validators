from .email import is_email
from .extremes import Min, Max
from .ip_address import ipv4, ipv6
from .mac_address import mac_address
from .utils import FailedValidation, validator
from .url import url
from .uuid import uuid


__all__ = (
    ipv4,
    ipv6,
    is_email,
    mac_address,
    url,
    uuid,
    validator,
    FailedValidation,
    Min,
    Max,
)


@validator
def number_range(value, min=None, max=None):
    """
    Validates that a number is of a minimum and/or maximum value, inclusive.
    This will work with any comparable number type, such as floats and
    decimals, not just integers.

    This validator is based on `WTForms NumberRange validator`_.

    .. _WTForms NumberRange validator:
       https://github.com/wtforms/wtforms/blob/master/wtforms/validators.py

    Examples::


        >>> number_range(5, min=2)
        True
        >>> number_range(13.2, min=13, max=14)
        True
        >>> number_range(500, max=400)
        False

    :param min:
        The minimum required value of the number. If not provided, minimum
        value will not be checked.
    :param max:
        The maximum value of the number. If not provided, maximum value
        will not be checked.

    .. versionadded: 0.2
    """
    if min is None and max is None:
        raise AssertionError(
            'At least one of `min` or `max` must be specified.'
        )
    if min is None:
        min = Min
    if max is None:
        max = Max
    if min > max:
        raise AssertionError('`min` cannot be more than `max`.')

    return min <= value <= max


@validator
def length(value, min=None, max=None):
    """
    Returns whether or not the length of given string is within a specified
    range.

    Examples::


        >>> length('something', min=2)
        True
        >>> length('something', min=9, max=9)
        True
        >>> length('something', max=5)
        False

    :param value:
        The string to validate.
    :param min:
        The minimum required length of the string. If not provided, minimum
        length will not be checked.
    :param max:
        The maximum length of the string. If not provided, maximum length
        will not be checked.

    .. versionadded: 0.2
    """
    if min < 0 and max < 0:
        raise AssertionError(
            'One of `min` and `max` need to be greater than zero.'
        )
    return number_range(len(value), min=min, max=max)
