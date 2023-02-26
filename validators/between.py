"""Between."""
# -*- coding: utf-8 -*-

# standard
from typing import TypeVar, Union
from datetime import datetime

# local
from ._extremes import AbsMax, AbsMin
from .utils import validator

PossibleValueTypes = TypeVar("PossibleValueTypes", int, float, str, datetime)


@validator
def between(
    value: PossibleValueTypes,
    /,
    *,
    min_val: Union[PossibleValueTypes, AbsMin, None] = None,
    max_val: Union[PossibleValueTypes, AbsMax, None] = None,
):
    """Validate that a number is between minimum and/or maximum value.

    This will work with any comparable type, such as floats, decimals and dates
    not just integers. This validator is originally based on [WTForms-NumberRange-Validator][1].

    [1]: https://github.com/wtforms/wtforms/blob/master/src/wtforms/validators.py#L166-L220

    Examples:
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
        # Output: True

    Args:
        value:
            Value which is to be compared.
        min_val:
            The minimum required value of the number.
            If not provided, minimum value will not be checked.
        max_val:
            The maximum value of the number.
            If not provided, maximum value will not be checked.

    Returns:
        (Literal[True]):
            If `value` is in between the given conditions.
        (ValidationFailure):
            If `value` is not in between the given conditions.

    Raises:
        AssertionError: If both `min_val` and `max_val` are `None`,
            or if `min_val` is greater than `max_val`.
        TypeError: If there's a type mismatch before comparison.

    Note:
        - `PossibleValueTypes` = `TypeVar("PossibleValueTypes", int, float, str, datetime)`
        - Either one of `min_val` or `max_val` must be provided.

    > *New in version 0.2.0*.
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
