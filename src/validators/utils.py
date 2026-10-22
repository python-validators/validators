"""Utils."""

# standard
from functools import wraps
from inspect import signature
from os import environ
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
        func_name = getattr(self.func, "__name__", type(self.func).__name__)
        return (
            f"ValidationError(func={func_name}, "
            + f"args={ ({k: v for (k, v) in self.__dict__.items() if k != 'func'}) })"
        )

    def __str__(self):
        """Str Validation Failure."""
        return repr(self)

    def __bool__(self):
        """Bool Validation Failure."""
        return False


def _func_args_as_dict(func: Callable[..., Any], *args: Any, **kwargs: Any):
    """Return function's positional and key value arguments as an ordered dictionary."""
    try:
        return dict(signature(func).bind_partial(*args, **kwargs).arguments)
    except (TypeError, ValueError):
        # Some builtins have no inspectable signature. Retain the raw call
        # instead of letting error reporting raise another exception.
        return {"positional_args": args, "keyword_args": kwargs}


def validator(func: Callable[..., Any]):
    """A decorator that makes given function validator.

    Whenever the given `func` returns `False` this
    decorator returns `ValidationError` object.

    Examples:
        >>> @validator
        ... def even(value):
        ...     return not (value % 2)
        >>> even(4)
        True
        >>> even(5)
        ValidationError(func=even, args={'value': 5})

    Args:
        func:
            Function which is to be decorated.

    Returns:
        (Callable[..., ValidationError | Literal[True]]):
            A decorator which returns either `ValidationError`
            or `Literal[True]`.

    Raises:
        (ValidationError): If `r_ve` or `RAISE_VALIDATION_ERROR` is `True`
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        raise_validation_error = bool(kwargs.pop("r_ve", False))
        if environ.get("RAISE_VALIDATION_ERROR", "False") == "True":
            raise_validation_error = True

        try:
            if raise_validation_error:
                if func(*args, **kwargs):
                    return True
                else:
                    raise ValidationError(func, _func_args_as_dict(func, *args, **kwargs))
            else:
                return (
                    True
                    if func(*args, **kwargs)
                    else ValidationError(func, _func_args_as_dict(func, *args, **kwargs))
                )
        except (ValueError, TypeError, UnicodeError) as exp:
            if raise_validation_error:
                raise ValidationError(
                    func, _func_args_as_dict(func, *args, **kwargs), str(exp)
                ) from exp
            else:
                return ValidationError(func, _func_args_as_dict(func, *args, **kwargs), str(exp))

    return wrapper
