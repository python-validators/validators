from .extremes import Min, Max
from .utils import validator


@validator
def between(value, min=None, max=None):
    """
    Validates that a number is between minimum and/or maximum value.
    This will work with any comparable type, such as floats, decimals and dates
    not just integers.

    This validator is originally based on `WTForms NumberRange validator`_.

    .. _WTForms NumberRange validator:
       https://github.com/wtforms/wtforms/blob/master/wtforms/validators.py

    Examples::

        >>> import validators

        >>> assert validators.between(5, min=2)

        >>> assert validators.between(13.2, min=13, max=14)

        >>> assert not validators.between(500, max=400)

        >>> from datetime import datetime

        >>> assert validator.between(
        ...     datetime(2000, 11, 11),
        ...     min=datetime(1999, 11, 11)
        ... )


    :param min:
        The minimum required value of the number. If not provided, minimum
        value will not be checked.
    :param max:
        The maximum value of the number. If not provided, maximum value
        will not be checked.

    .. versionadded:: 0.2
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
