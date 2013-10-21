from .email import is_email
from .extremes import Min, Max
from .utils import FailedValidation, validator


__all__ = (
    is_email,
    validator,
    FailedValidation,
    Min,
    Max,
)


@validator
def range(value, min=None, max=None):
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
    if min < 0 and max < 0:
        raise AssertionError('`min` and `max` need to be greater than zero.')
    return range(len(value), min=min, max=max)


@validator
def ipv4(value):
    """
    Returns whether or not given value is a valid IP version 4 address.

    This validator is based on `WTForms IPAddress validator`_

    .. _WTForms IPAddress validator:
       https://github.com/wtforms/wtforms/blob/master/wtforms/validators.py


    Examples::
        >>> import validators

        >>> validators.ipv4('123.0.0.7')
        True
        >>> validators.ipv4('900.80.70.11')
        False

    :param value: IP address string to validate
    """
    parts = value.split('.')
    if len(parts) == 4 and all(x.isdigit() for x in parts):
        numbers = list(int(x) for x in parts)
        return all(num >= 0 and num < 256 for num in numbers)
    return False


@validator
def ipv6(value):
    """
    Returns whether or not given value is a valid IP version 6 address.

    This validator is based on `WTForms IPAddress validator`_

    .. _WTForms IPAddress validator:
       https://github.com/wtforms/wtforms/blob/master/wtforms/validators.py


    Examples::
        >>> import validators

        >>> validators.ipv6('abcd:ef::42:1')
        True
        >>> validators.ipv6('abc.0.0.1')
        False

    :param value: IP address string to validate
    """
    parts = value.split(':')
    if len(parts) > 8:
        return False

    num_blank = 0
    for part in parts:
        if not part:
            num_blank += 1
        else:
            try:
                value = int(part, 16)
            except ValueError:
                return False
            else:
                if value < 0 or value >= 65536:
                    return False

    if num_blank < 2:
        return True
    elif num_blank == 2 and not parts[0] and not parts[1]:
        return True
    return False
