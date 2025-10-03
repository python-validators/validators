"""Extremes."""

# standard
from functools import total_ordering
from typing import Any


@total_ordering
class AbsMax:
    """An object that is greater than any other object (except itself).

    Inspired by https://pypi.python.org/pypi/Extremes.

    Examples:
        >>> from sys import maxsize
        >>> AbsMax() > AbsMin()
        True
        >>> AbsMax() > maxsize
        True
        >>> AbsMax() > 99999999999999999
        True
    """

    def __ge__(self, other: Any):
        """GreaterThanOrEqual."""
        return not isinstance(other, AbsMax)


@total_ordering
class AbsMin:
    """An object that is less than any other object (except itself).

    Inspired by https://pypi.python.org/pypi/Extremes.

    Examples:
        >>> from sys import maxsize
        >>> AbsMin() < -maxsize
        True
        >>> AbsMin() < None
        True
        >>> AbsMin() < ''
        True
    """

    def __le__(self, other: Any):
        """LessThanOrEqual."""
        return not isinstance(other, AbsMin)
