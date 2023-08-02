"""Utils."""

# standard
from functools import wraps
from inspect import getfullargspec
from itertools import chain
from typing import Any, Callable, Dict


class ValidationError(Exception):
    """Exception class when validation failure occurs."""

    def __init__(self, function: Callable[..., Any], arg_dict: Dict[str, Any], message: str = ""):
        """Initialize Validation Failure."""
        if message:
            self.reason = message
        self.func = function
        self.__dict__.update(arg_dict)

    def __repr__(self):
        """Repr Validation Failure."""
        return (
            f"ValidationError(func={self.func.__name__}, "
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
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(func)[0], kwargs.keys())), args))
        + list(kwargs.items())
    )


def validator(func: Callable[..., Any]):
    """A decorator that makes given function validator.

    Whenever the given `func` returns `False` this
    decorator returns `ValidationError` object.

    Examples:
        >>> @validator
        ... def even(value):
        ...     return not (value % 2)
        >>> even(4)
        # Output: True
        >>> even(5)
        # Output: ValidationError(func=even, args={'value': 5})

    Args:
        func:
            Function which is to be decorated.

    Returns:
        (Callable[..., ValidationError | Literal[True]]):
            A decorator which returns either `ValidationError`
            or `Literal[True]`.

    > *New in version 2013.10.21*.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        try:
            return (
                True
                if func(*args, **kwargs)
                else ValidationError(func, _func_args_as_dict(func, *args, **kwargs))
            )
        except Exception as exp:
            return ValidationError(func, _func_args_as_dict(func, *args, **kwargs), str(exp))

    return wrapper
