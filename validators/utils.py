try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict
import inspect
import itertools
from functools import wraps


class FailedValidation(object):
    def __init__(self, func, args):
        self.func = func
        self.__dict__.update(args)

    def __bool__(self):
        return False

    def __nonzero__(self):
        return False


def func_args_as_dict(func, args, kwargs):
    arg_names = list(
        OrderedDict.fromkeys(
            inspect.getargspec(func)[0] +
            kwargs.keys()
        )
    )
    return OrderedDict(
        list(itertools.izip(arg_names, args)) +
        list(kwargs.iteritems())
    )


def validator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if not value:
            return FailedValidation(
                func, func_args_as_dict(func, args, kwargs)
            )
        return value
    return wrapper
