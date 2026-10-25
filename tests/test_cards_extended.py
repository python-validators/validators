"""Extended coverage for card numbers and the brand validators.

The repo's card tests (219 lines) cover the standard test numbers;
this file pins the brand/prefix/length matrix the existing suite only
samples: every brand against every other brand's number, Luhn failures
that keep a valid prefix, and length-only failures.

All card numbers used here are the well-known gateway test numbers
already used in the repo's own tests and docstrings.
"""

import pytest

from validators import (
    ValidationError,
    amex,
    card_number,
    diners,
    discover,
    jcb,
    mastercard,
    mir,
    unionpay,
    visa,
)


# ---------------------------------------------------------------- generic Luhn


@pytest.mark.parametrize(
    "value",
    ["4242424242424242", "378282246310005", "6011111111111117", "30569309025904"],
)
def test_card_number_returns_true_on_luhn_valid_numbers(value):
    assert card_number(value) is True


@pytest.mark.parametrize(
    "value",
    [
        "",
        "4242424242424241",  # last digit breaks Luhn
        "4242 4242 4242 4242",  # spaces are not stripped
        "4242-4242-4242-4242",  # dashes are not stripped
        "abcd",  # non-digits fail int() conversion
        "123",  # Luhn sum is not a multiple of 10
    ],
)
def test_card_number_returns_failed_validation_on_invalid_numbers(value):
    assert isinstance(card_number(value), ValidationError)


# ---------------------------------------------------------------- brands


@pytest.mark.parametrize(
    ("validator", "value"),
    [
        (visa, "4242424242424242"),
        (visa, "4111111111111111"),
        (mastercard, "5555555555554444"),
        (mastercard, "2223003122003222"),  # 2-series Mastercard
        (amex, "378282246310005"),
        (amex, "371449635398431"),
        (unionpay, "6200000000000005"),
        (diners, "30569309025904"),  # 14 digits
        (diners, "3056930009020004"),
        (diners, "36148900647913"),
        (jcb, "3530111333300000"),
        (jcb, "3566002020360505"),
        (discover, "6011111111111117"),
        (discover, "6011000990139424"),
        (discover, "6445644564456445"),  # 644 prefix
        (mir, "2200123456789019"),
    ],
)
def test_brand_validators_accept_their_own_numbers(validator, value):
    assert validator(value) is True


@pytest.mark.parametrize(
    ("validator", "value"),
    [
        # Wrong brand, Luhn-valid number: prefix/length must reject it.
        (visa, "5555555555554444"),
        (mastercard, "4242424242424242"),
        (amex, "4242424242424242"),
        (unionpay, "4242424242424242"),
        (diners, "4242424242424242"),
        (jcb, "4242424242424242"),
        (discover, "4242424242424242"),
        (mir, "4242424242424242"),
        # Right prefix family, wrong length.
        (visa, "4222222222222"),  # 13 digits, not 16
        (visa, "424242424242424"),  # 15 digits, not 16
        (amex, "3782822463100050"),  # 16 digits, not 15
        (mastercard, "555555555555444"),  # 15 digits, not 16
        # Right prefix, broken Luhn.
        (amex, "378282246310006"),
        (unionpay, "6200000000000006"),
        (jcb, "3530111333300001"),
        (discover, "6011111111111118"),
        # Prefix just outside the accepted range.
        (mastercard, "2720992713989755"),  # 2720-series edge, Luhn-invalid
        (mir, "2205123456789019"),  # 2205 is outside 2200-2204
        (diners, "32148900647913"),  # 32 is not a Diners prefix
        (discover, "6221111111111117"),  # 62 is UnionPay, not Discover
    ],
)
def test_brand_validators_reject_other_numbers(validator, value):
    assert isinstance(validator(value), ValidationError)


def test_brand_validators_reject_empty_and_non_digit_input():
    for validator in (visa, mastercard, amex, unionpay, diners, jcb, discover, mir):
        assert isinstance(validator(""), ValidationError)
        assert isinstance(validator("abcd"), ValidationError)


# ---------------------------------------------------------------- ValidationError mechanics


def test_validation_error_is_falsy_and_carries_function_and_args():
    result = visa("5555555555554444")
    assert isinstance(result, ValidationError)
    assert bool(result) is False
    assert result.func.__name__ == "visa"
    assert result.value == "5555555555554444"
    assert repr(result).startswith("ValidationError(func=visa")


def test_validation_error_raised_with_r_ve():
    with pytest.raises(ValidationError):
        visa("5555555555554444", r_ve=True)


def test_validation_error_not_raised_with_r_ve_on_valid_input():
    assert visa("4242424242424242", r_ve=True) is True
