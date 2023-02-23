"""Between."""
# -*- coding: utf-8 -*-

# standard
from typing import TypeVar, Union
from datetime import datetime

# local
from ._extremes import AbsMax, AbsMin
from .utils import validator

T = TypeVar("T", int, float, str, datetime)


@validator
def between(
    value: T,
    /,
    *,
    min_val: Union[T, AbsMin, None] = None,
    max_val: Union[T, AbsMax, None] = None,
):
    """Validate that a number is between minimum and/or maximum value.

    This will work with any comparable type, such as floats, decimals and dates
    not just integers. This validator is originally based on `WTForms-NumberRange-Validator`_

    .. _WTForms-NumberRange-Validator:
        https://github.com/wtforms/wtforms/blob/master/src/wtforms/validators.py#L166-L220

    Examples::

        >>> from datetime import datetime

        >>> between(5, min_val=2)
        # Output: True

        >>> between(13.2, min_val=13, max_val=14)
        # Output: True

        >>> between(500, max_val=400)
        # Output: ValidationFailure(func=between, args=...)

        >>> between(
        ...     datetime(2000, 11, 11),
        ...     min_val=datetime(1999, 11, 11)
        ... )
        # True

    Args:
        `value`:
            [Required] Value which is to be compared.
        `min_val`:
            [Optional] The minimum required value of the number.
            If not provided, minimum value will not be checked.
        `max_val`:
            [Optional] The maximum value of the number.
            If not provided, maximum value will not be checked.
        Either one of `min_val` or `max_val` must be provided.

    Returns:
        A `boolean` if `value` is greater than `min_val` and
        less than `max_val`.

    Raises:
        `AssertionError`:
        - If both `min_val` and `max_val` are `None`.
        - If `min_val` is greater than `max_val`.

        `TypeError`:
        - If there's a type mismatch before comparison

    .. versionadded:: 0.2
    """
    if min_val is None and max_val is None:
        raise AssertionError("At least one of either `min_val` or `max_val` must be specified")

    if max_val is None:
        max_val = AbsMax()
    if min_val is None:
        min_val = AbsMin()

    if isinstance(min_val, AbsMin):
        if type(value) is not type(max_val):
            raise TypeError("`value` and `max_val` must be of same type")
        return min_val <= value <= max_val

    if isinstance(max_val, AbsMax):
        if type(value) is not type(min_val):
            raise TypeError("`value` and `min_val` must be of same type")
        return min_val <= value <= max_val

    if type(min_val) is type(max_val):
        if min_val > max_val:
            raise AssertionError("`min_val` cannot be more than `max_val`")
        if type(value) is not type(min_val):  # or type(max_val):
            raise TypeError("`value` and (`min_val` or `max_val`) must be of same type")
        return min_val <= value <= max_val

    raise TypeError("`value` and `min_val` and `max_val` must be of same type")
