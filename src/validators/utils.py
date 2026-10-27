"""Utils."""

# standard
from contextvars import ContextVar
from dataclasses import dataclass
from functools import wraps
from inspect import getfullargspec
from itertools import chain
from os import environ
from sys import modules
from threading import get_ident
from typing import Any, Callable, Dict


@dataclass
class _ValidationScope:
    """Track the lifetime, thread and task of an outermost validation call."""

    thread_id: int
    task_id: int | None
    active: bool = True


_validation_scope: ContextVar[_ValidationScope | None] = ContextVar(
    "_validation_scope", default=None
)


def _current_task_id() -> int | None:
    """Identify an active task without loading asyncio for synchronous callers."""
    if "asyncio" not in modules:
        return None

    from asyncio import current_task

    try:
        task = current_task()
    except RuntimeError:
        return None
    return id(task) if task is not None else None


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
    return dict(
        list(zip(dict.fromkeys(chain(getfullargspec(func)[0], kwargs.keys())), args))
        + list(kwargs.items())
    )


def validator(func: Callable[..., Any]):
    """A decorator that makes given function validator.

    Whenever the given `func` returns `False` this
    decorator returns `ValidationError` object.

    The environment option raises at the outermost validation call so nested
    validators can try alternatives. An explicit `r_ve=True` always raises.

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
        scope = _validation_scope.get()
        thread_id = get_ident()
        task_id = _current_task_id()
        if (
            scope is None
            or not scope.active
            or scope.thread_id != thread_id
            or scope.task_id != task_id
        ):
            if environ.get("RAISE_VALIDATION_ERROR", "False") == "True":
                raise_validation_error = True
            scope = _ValidationScope(thread_id, task_id)
            token = _validation_scope.set(scope)
        else:
            token = None

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
        finally:
            if token is not None:
                scope.active = False
                _validation_scope.reset(token)

    return wrapper
