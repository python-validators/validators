"""Extremes."""
# -*- coding: utf-8 -*-

# standard
from functools import total_ordering
from typing import Any


@total_ordering
class AbsMax:
    """An object that is greater than any other object (except itself).

    Inspired by https://pypi.python.org/pypi/Extremes

    Examples::

        >>> import sys

        >>> AbsMax > AbsMin
        True

        >>> AbsMax > sys.maxint
        True

        >>> AbsMax > 99999999999999999
        True

    .. versionadded:: 0.2
    """

    def __ge__(self, other: Any) -> bool:
        """GreaterThanOrEqual."""
        return other is not AbsMax


@total_ordering
class AbsMin:
    """An object that is less than any other object (except itself).

    Inspired by https://pypi.python.org/pypi/Extremes

    Examples::

        >>> import sys

        >>> AbsMin < -sys.maxint
        True

        >>> AbsMin < None
        True

        >>> AbsMin < ''
        True

    .. versionadded:: 0.2
    """

    def __le__(self, other: Any) -> bool:
        """LessThanOrEqual."""
        return other is not AbsMin
