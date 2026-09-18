"""Cron."""

# local
from .utils import validator


def _validate_cron_item(item: str, min_val: int, max_val: int):
    # An item may carry a step, e.g. "*/5", "1-30/2" or "5/10".
    if "/" in item:
        base, _, step = item.partition("/")
        if not step.isdecimal() or int(step) < 1:
            return False
    else:
        base = item

    if base == "*":
        return True

    if "-" in base:
        parts = base.split("-")
        if len(parts) != 2 or not parts[0].isdecimal() or not parts[1].isdecimal():
            return False
        start, end = int(parts[0]), int(parts[1])
        return min_val <= start <= max_val and min_val <= end <= max_val and start <= end

    if base.isdecimal():
        return min_val <= int(base) <= max_val

    return False


def _validate_cron_component(component: str, min_val: int, max_val: int):
    # A field is a comma-separated list of items, each optionally stepped.
    return all(_validate_cron_item(item, min_val, max_val) for item in component.split(","))


@validator
def cron(value: str, /):
    """Return whether or not given value is a valid cron string.

    Examples:
        >>> cron('*/5 * * * *')
        True
        >>> cron('30-20 * * * *')
        ValidationError(func=cron, args={'value': '30-20 * * * *'})

    Args:
        value:
            Cron string to validate.

    Returns:
        (Literal[True]): If `value` is a valid cron string.
        (ValidationError): If `value` is an invalid cron string.
    """
    if not value:
        return False

    try:
        minutes, hours, days, months, weekdays = value.strip().split()
    except ValueError as err:
        raise ValueError("Badly formatted cron string") from err

    if not _validate_cron_component(minutes, 0, 59):
        return False
    if not _validate_cron_component(hours, 0, 23):
        return False
    if not _validate_cron_component(days, 1, 31):
        return False
    if not _validate_cron_component(months, 1, 12):
        return False
    if not _validate_cron_component(weekdays, 0, 7):
        return False

    return True
