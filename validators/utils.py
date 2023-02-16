"""Utils."""
# -*- coding: utf-8 -*-

# standard
from typing import Any, Callable, Dict, Literal, Union
from inspect import getfullargspec
from itertools import chain


class ValidationFailure(Exception):
    """Exception class when validation failure occurs."""

    def __init__(self, function: Callable[..., Any], arg_dict: Dict[str, Any]):
        """Initialize Validation Failure."""
        self.func = function
        self.__dict__.update(arg_dict)

    def __repr__(self) -> str:
        """Repr Validation Failure."""
        return (
            f"ValidationFailure(func={self.func.__name__}, "
            + f"args={({k: v for (k, v) in self.__dict__.items() if k != 'func'})})"
        )

    def __str__(self) -> str:
        """Str Validation Failure."""
        return repr(self)

    def __bool__(self) -> Literal[False]:
        """Bool Validation Failure."""
        return False


def _func_args_as_dict(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Dict[str, Any]:
    """Return function's positional and key value arguments as an ordered dictionary."""
    # TODO: find more efficient way to do it
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(func)[0], kwargs.keys())), args))
        + list(kwargs.items())
    )


def validator(func: Callable[..., Any]) -> Callable[..., Union[Literal[True], ValidationFailure]]:
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

    def wrapper(*args: Any, **kwargs: Any) -> Union[Literal[True], ValidationFailure]:
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
