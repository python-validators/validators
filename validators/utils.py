"""Utils."""
# -*- coding: utf-8 -*-

# standard
from inspect import getfullargspec
from typing import TYPE_CHECKING
from itertools import chain

if TYPE_CHECKING:
    # standard
    from typing import Any, Callable, Dict


class ValidationFailure(Exception):
    """Exception class when validation failure occurs."""

    def __init__(self, function: Callable[..., Any], arg_dict: Dict[str, Any]):
        """Initialize Validation Failure."""
        self.func = function
        self.__dict__.update(arg_dict)

    def __repr__(self):
        """Repr Validation Failure."""
        return (
            f"ValidationFailure(func={self.func.__name__}, "
            + f"args={({k: v for (k, v) in self.__dict__.items() if k != 'func'})})"
        )

    def __str__(self):
        """Str Validation Failure."""
        return repr(self)

    def __bool__(self):
        """Bool Validation Failure."""
        return False


def _func_args_as_dict(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    # TODO: find more efficient way to do it
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(func)[0], kwargs.keys())), args))
        + list(kwargs.items())
    )


def validator(func: Callable[..., Any]):
    """A decorator that makes given function validator.

    Whenever the given function is called and returns ``False`` value
    this decorator returns :class:`ValidationFailure` object.

    Example::

        >>> @validator
        ... def even(value):
        ...     return not (value % 2)

        >>> even(4)
        # Output: True

        >>> even(5)
        # Output: ValidationFailure(func=even, args={'value': 5})

    Args:
        `func`: function which is to be decorated.

    Returns:
        Wrapper function as a decorator.
    """

    def wrapper(*args: Any, **kwargs: Any):
        return (
            True
            if func(*args, **kwargs)
            else ValidationFailure(func, _func_args_as_dict(func, *args, **kwargs))
        )
        # try:
        #     return (
        #         True
        #         if func(*args, **kwargs)
        #         else ValidationFailure(func, _func_args_as_dict(func, *args, **kwargs))
        #     )
        # except (AssertionError, TypeError) as err:
        #     print(err)
        # finally:
        #     return ValidationFailure(func, _func_args_as_dict(func, *args, **kwargs))

    return wrapper
