"""Extremes."""

# standard
from functools import total_ordering
from typing import Any


@total_ordering
class AbsMax:
    """An object that is greater than any other object (except itself).

    Inspired by https://pypi.python.org/pypi/Extremes.

    Examples:
        >>> from sys import maxint
        >>> AbsMax > AbsMin
        # Output: True
        >>> AbsMax > maxint
        # Output: True
        >>> AbsMax > 99999999999999999
        # Output: True

    > *New in version 0.2.0*.
    """

    def __ge__(self, other: Any):
        """GreaterThanOrEqual."""
        return other is not AbsMax


@total_ordering
class AbsMin:
    """An object that is less than any other object (except itself).

    Inspired by https://pypi.python.org/pypi/Extremes.

    Examples:
        >>> from sys import maxint
        >>> AbsMin < -maxint
        # Output: True
        >>> AbsMin < None
        # Output: True
        >>> AbsMin < ''
        # Output: True

    > *New in version 0.2.0*.
    """

    def __le__(self, other: Any):
        """LessThanOrEqual."""
        return other is not AbsMin
