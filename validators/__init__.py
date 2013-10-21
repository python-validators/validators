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
