"""Test validation Failure."""

# standard
import asyncio
from concurrent.futures import ThreadPoolExecutor
from contextvars import Context, copy_context
import sys
from threading import Event
from typing import Any, Callable

# third-party
import pytest

# local
from validators import ValidationError, between, hostname, slug, url, uuid
from validators.utils import validator


@pytest.mark.parametrize("function,value", [(slug, "invalid_"), (uuid, "not-a-uuid")])
def test_false_raise_validation_error_flag(
    function: Callable[..., Any], value: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A false flag returns validation errors instead of raising them."""
    monkeypatch.delenv("RAISE_VALIDATION_ERROR", raising=False)
    result = function(value, r_ve=False)
    assert isinstance(result, ValidationError)
    assert not result


@pytest.mark.parametrize("function,value", [(slug, "invalid_"), (uuid, "not-a-uuid")])
def test_environment_still_enables_raise_validation_error(
    function: Callable[..., Any], value: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The environment option enables raising even when the call flag is false."""
    monkeypatch.setenv("RAISE_VALIDATION_ERROR", "True")
    with pytest.raises(ValidationError):
        function(value, r_ve=False)


@pytest.mark.parametrize("function,value", [(slug, "invalid_"), (uuid, "not-a-uuid")])
def test_true_raise_validation_error_flag(
    function: Callable[..., Any], value: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A true call flag continues to raise validation errors."""
    monkeypatch.delenv("RAISE_VALIDATION_ERROR", raising=False)
    with pytest.raises(ValidationError):
        function(value, r_ve=True)


@pytest.mark.parametrize("global_raise", [False, True])
@pytest.mark.parametrize(
    "function,value",
    [
        (hostname, "127.0.0.1"),
        (hostname, "::1"),
        (hostname, "127.0.0.1:8080"),
        (hostname, "[::1]:8080"),
        (url, "http://10.0.0.1"),
        (url, "http://[::1]"),
    ],
)
def test_raise_mode_accepts_valid_composite_values(
    function: Callable[..., Any],
    value: str,
    global_raise: bool,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Both raise modes allow failed alternatives inside a valid composite validator."""
    monkeypatch.setenv("RAISE_VALIDATION_ERROR", str(global_raise))
    assert function(value, r_ve=not global_raise) is True


@pytest.mark.parametrize("global_raise", [False, True])
@pytest.mark.parametrize(
    "function,value", [(hostname, "not a hostname"), (url, "http://not a hostname")]
)
def test_raise_mode_reports_invalid_composite_at_public_boundary(
    function: Callable[..., Any],
    value: str,
    global_raise: bool,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Invalid composite inputs raise an error for the validator the caller invoked."""
    monkeypatch.setenv("RAISE_VALIDATION_ERROR", str(global_raise))
    with pytest.raises(ValidationError) as exc_info:
        function(value, r_ve=not global_raise)
    assert exc_info.value.func.__name__ == function.__name__
    assert exc_info.value.__dict__["value"] == value


def test_nested_explicit_raise_flag_is_respected(monkeypatch: pytest.MonkeyPatch) -> None:
    """A nested caller can still explicitly request an exception."""
    monkeypatch.setenv("RAISE_VALIDATION_ERROR", "True")

    @validator
    def explicit_nested_raise(value: str):
        return slug(value, r_ve=True)

    with pytest.raises(ValidationError) as exc_info:
        explicit_nested_raise("invalid_")
    assert exc_info.value.func.__name__ == "slug"


@pytest.mark.parametrize("global_raise", [False, True])
def test_raise_mode_is_independent_between_threads(
    global_raise: bool, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A validation in another thread must not suppress this caller's raise mode."""
    monkeypatch.setenv("RAISE_VALIDATION_ERROR", str(global_raise))
    entered = Event()
    release = Event()

    @validator
    def waiting_validation():
        entered.set()
        assert release.wait(timeout=5)
        return True

    with ThreadPoolExecutor(max_workers=1) as executor:
        pending = executor.submit(waiting_validation, r_ve=not global_raise)
        try:
            assert entered.wait(timeout=5)
            with pytest.raises(ValidationError):
                slug("invalid_", r_ve=not global_raise)
        finally:
            release.set()
        assert pending.result(timeout=5) is True


def test_copied_context_is_independent_in_another_thread(monkeypatch: pytest.MonkeyPatch) -> None:
    """Copying an active context to another thread must not suppress its raise mode."""
    monkeypatch.setenv("RAISE_VALIDATION_ERROR", "True")

    def validate_on_worker() -> bool:
        try:
            slug("invalid_")
        except ValidationError:
            return True
        return False

    @validator
    def validation_with_worker():
        context = copy_context()
        with ThreadPoolExecutor(max_workers=1) as executor:
            pending = executor.submit(context.run, validate_on_worker)
            assert pending.result(timeout=5)
        return True

    assert validation_with_worker() is True


@pytest.mark.parametrize("eager", [False, True])
def test_inherited_task_context_does_not_suppress_independent_validation(
    eager: bool,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """An inherited task context must not suppress independent synchronous validation."""
    if eager and sys.version_info < (3, 12):
        pytest.skip("Eager task factories require Python 3.12 or newer")
    monkeypatch.setenv("RAISE_VALIDATION_ERROR", "True")

    async def validate_later() -> None:
        with pytest.raises(ValidationError):
            slug("invalid_")

    async def run_validation() -> None:
        if eager and sys.version_info >= (3, 12):
            asyncio.get_running_loop().set_task_factory(asyncio.eager_task_factory)
        tasks: list[asyncio.Task[None]] = []

        @validator
        def schedule_validation():
            assert hostname("127.0.0.1") is True
            assert isinstance(slug("invalid_"), ValidationError)
            tasks.append(asyncio.create_task(validate_later()))
            assert hostname("::1") is True
            return True

        assert schedule_validation() is True
        await tasks[0]

    asyncio.run(run_validation())


@pytest.mark.parametrize("outcome", ["valid", "invalid", "parse_error", "unexpected_error"])
def test_global_raise_mode_is_restored_after_validation(
    outcome: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Returning or raising from a validator must not suppress a later independent call."""
    monkeypatch.setenv("RAISE_VALIDATION_ERROR", "True")
    contexts: list[Context] = []

    @validator
    def capture_context():
        contexts.append(copy_context())
        return True

    @validator
    def sample_validation():
        assert capture_context() is True
        assert isinstance(contexts[0].run(slug, "invalid_"), ValidationError)
        if outcome == "unexpected_error":
            raise RuntimeError("unexpected")
        if outcome == "parse_error":
            raise ValueError("parse error")
        return outcome == "valid"

    if outcome == "valid":
        assert sample_validation() is True
    else:
        expected_error = RuntimeError if outcome == "unexpected_error" else ValidationError
        with pytest.raises(expected_error):
            sample_validation()
    with pytest.raises(ValidationError):
        slug("invalid_")
    with pytest.raises(ValidationError):
        contexts[0].run(slug, "invalid_")


failed_obj_repr = "ValidationError(func=between"


class TestValidationError:
    """Test validation Failure."""

    def setup_method(self):
        """Setup Method."""
        self.is_in_between = between(3, min_val=4, max_val=5)

    def test_boolean_coerce(self):
        """Test Boolean."""
        assert not bool(self.is_in_between)
        assert not self.is_in_between

    def test_repr(self):
        """Test Repr."""
        assert failed_obj_repr in repr(self.is_in_between)

    def test_string(self):
        """Test Repr."""
        assert failed_obj_repr in str(self.is_in_between)

    def test_arguments_as_properties(self):
        """Test argument properties."""
        assert self.is_in_between.__dict__["value"] == 3
        assert self.is_in_between.__dict__["min_val"] == 4
        assert self.is_in_between.__dict__["max_val"] == 5
