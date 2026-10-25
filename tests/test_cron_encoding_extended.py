"""Extended coverage for cron and the base16/32/58/64 encodings.

Existing cron tests are 59 lines and only exercise the happy path plus a
few out-of-range fields; the step/list grammar below is probed, not
assumed. Encoding tests in the repo are 151 lines but leave padding
and alphabet edge cases unpinned.
"""

import pytest

from validators import (
    ValidationError,
    base16,
    base32,
    base58,
    base64,
    cron,
)


# ---------------------------------------------------------------- cron


@pytest.mark.parametrize(
    "value",
    [
        "0 0 * * *",
        "*/15 * * * *",  # step over the whole range
        "0 9-17 * * 1-5",  # ranges in two fields
        "5/10 * * * *",  # a single value with a step is accepted
        "0 0 * * 7",  # Sunday may be written as 7
        "1,2,3 * * * *",  # comma list
        "0 0 1,15 * *",
        "*/2 0-23/2 * * *",  # step over a range
        "  0   0  *  *  *  ",  # extra whitespace is stripped/split away
        "30 4 1 * *",
        "59 23 31 12 7",  # every field at its maximum
        "0 0 1 1 0",  # every field at its minimum
    ],
)
def test_cron_returns_true_on_valid_expressions(value):
    assert cron(value) is True


@pytest.mark.parametrize(
    "value",
    [
        "*/0 * * * *",  # step must be >= 1
        "*/abc * * * *",  # step must be decimal
        "30-20 * * * *",  # reversed range
        "1,,2 * * * *",  # empty list item
        "1- * * * *",  # dangling range end
        "1-2-3 * * * *",  # three-part range
        "0 0 * * MON",  # month/weekday names are not supported
        "0 0 0 * *",  # day of month starts at 1
        "0 0 * 0 *",  # month starts at 1
        "0 0 * * 8",  # weekday ends at 7
        "60 * * * *",  # minute ends at 59
        "0 24 * * *",  # hour ends at 23
        "0 0 32 * *",  # day of month ends at 31
        "0 0 * 13 *",  # month ends at 12
        "-1 * * * *",  # negatives are not decimal
        "* * * *",  # four fields: badly formatted
        "0 0 * * * *",  # six fields: badly formatted
        "",
    ],
)
def test_cron_returns_failed_validation_on_invalid_expressions(value):
    assert isinstance(cron(value), ValidationError)


def test_cron_wrong_field_count_carries_the_reason():
    result = cron("* * * *")
    assert isinstance(result, ValidationError)
    assert result.reason == "Badly formatted cron string"


# ---------------------------------------------------------------- base16


@pytest.mark.parametrize("value", ["00ff", "FF", "a3f4b2", "00" * 10])
def test_base16_returns_true_on_valid_values(value):
    assert base16(value) is True


@pytest.mark.parametrize("value", ["", "0", "abc", "0x12", "a3f4Z1", "ff "])
def test_base16_returns_failed_validation_on_invalid_values(value):
    assert isinstance(base16(value), ValidationError)


# ---------------------------------------------------------------- base32


@pytest.mark.parametrize(
    "value",
    [
        "MY======",  # 1 byte + padding
        "MZXW6===",  # 2 bytes + padding
        "MZXW6YQ=",  # 4 bytes + padding
        "MZXW6YTBOI======",  # 8-char group + padding
        "MZXW6",  # padding is optional for the short forms
        "MZXW6YQ",  # 6 chars, no padding needed
        "ABCDEFGHIJKLMNOP",  # two full 8-char groups
    ],
)
def test_base32_returns_true_on_valid_values(value):
    assert base32(value) is True


@pytest.mark.parametrize(
    "value",
    [
        "",
        "MfZW3zLT9Q======",  # lower case is not in the alphabet
        "MZXW6Y==",  # 6 chars may not take "==" padding
        "MZXW6YQ==",  # 7 chars may take at most one "="
        "MZXW6YQ===",  # too much padding
        "MZXW68==",  # '8' is not in the base32 alphabet
        "MZXW6YQ=extra",
    ],
)
def test_base32_returns_failed_validation_on_invalid_values(value):
    assert isinstance(base32(value), ValidationError)


# ---------------------------------------------------------------- base58


@pytest.mark.parametrize("value", ["StV1DL6CwTryKyV", "cUSECm5YzcXJwP", "1111111111"])
def test_base58_returns_true_on_valid_values(value):
    assert base58(value) is True


@pytest.mark.parametrize(
    "value",
    [
        "",
        "0abc",  # '0' is excluded from base58
        "Oabc",  # 'O' is excluded
        "Iabc",  # 'I' is excluded
        "labc",  # 'l' is excluded
        "abc def",  # spaces are excluded
        "abc+def",  # '+' is excluded
    ],
)
def test_base58_returns_failed_validation_on_invalid_values(value):
    assert isinstance(base58(value), ValidationError)


# ---------------------------------------------------------------- base64


@pytest.mark.parametrize(
    "value",
    [
        "YQ==",  # 1 byte
        "YWI=",  # 2 bytes
        "TWFu",  # 3 bytes, no padding
        "Y2hhcmFjdGVyIHNldA==",
        "TWFuTWFu",  # two full groups
    ],
)
def test_base64_returns_true_on_valid_values(value):
    assert base64(value) is True


@pytest.mark.parametrize(
    "value",
    [
        "",
        "YQ=",  # 1 byte needs "==", not "="
        "YWI",  # missing padding
        "YQ==YQ==",  # padding may only appear at the end
        "Y W I=",  # spaces are not in the alphabet
        "YQ==\n",
        "YQ*=",
    ],
)
def test_base64_returns_failed_validation_on_invalid_values(value):
    assert isinstance(base64(value), ValidationError)
