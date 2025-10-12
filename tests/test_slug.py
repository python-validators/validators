"""Test Slug."""

# external

from typing import Any

import pytest

# local
from validators import ValidationError, slug


@pytest.mark.parametrize(
    "value",
    [
        # with numbers
        "hello123",
        "123hello",
        "123",
        # with hyphens
        "hello-world",
        "hello-world-test",
        "test-123-abc",
        # with mixed alphanumeric
        "hello123-world456",
        "123-456-789",
        "a1-b2-c3",
        # with single character
        "a",
        "1",
        "z",
        # with complex slug
        "test-123-abc-456-def",
        "this-is-a-very-long-slug-with-many-words",
        # with multiple hyphens
        "a-b-c",
        "1-2-3",
        # very long
        "a" * 100,
        # very long with hyphens
        "a-" * 50 + "end",
        # very long with hyphens and different alphabets|letters
        "a1-b2-c3-d4-e5-f6-g7-h8-i9-j0",
        # old
        "123-asd-7sda",
        "123-k-123",
        "dac-12sa-459",
        "dac-12sa7-ad31as",
    ],
)
def test_returns_true_on_valid_slug(value: str):
    """Test returns true on valid slug."""
    assert slug(value)


@pytest.mark.parametrize(
    "value",
    [
        # with empty_string
        "",
        # with upper case
        "Hello",
        "HELLO",
        "hello-World",
        "Test-Slug",
        # with special characters
        "hello world",
        "hello_world",
        "hello.world",
        "hello@world",
        "hello#world",
        "hello$world",
        # starting with hyphen
        "-hello",
        "-123",
        "-hello-world",
        # with consecutive hyphens
        "hello--world",
        "test---slug",
        "a--b",
        # with unicode characters
        "café",
        "привет",
        "東京",
        "hello-мир",
        # with spaces
        "hello world",
        " hello ",
        "hello  world",
        # with only hyphens
        "-",
        "--",
        "---",
        # with mixed case
        "HelloWorld",
        "helloWorld",
        "HELLOworld",
        # old
        "some.slug&",
        "1231321%",
        "   21312",
        "-47q-p--123",
    ],
)
def test_returns_failed_validation_on_invalid_slug(value: str):
    """Test returns failed validation on invalid slug."""
    assert isinstance(slug(value), ValidationError)


@pytest.mark.parametrize(
    ("val", "input_type"),
    [
        (1, "int"),
        (1.0, "float"),
        (None, "NoneType"),
        ([], "list"),
        ((), "tuple"),
        ({}, "dict"),
    ],
)
def test_non_string_input(val: Any, input_type: Any):
    """Test with non string input."""
    # given
    message = f"expected string or bytes-like object, got '{input_type}'"
    # when
    result = slug(val)
    # then
    assert isinstance(result, ValidationError)
    assert result.reason == message


def test_slug_function_signature():
    """Test with keyword argument."""
    # given
    message = "slug() got some positional-only arguments passed as keyword arguments: 'value'"
    # when
    result = slug(value="test-slug")
    # then
    assert isinstance(result, ValidationError)
    assert result.reason == message
