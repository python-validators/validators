"""Extended coverage for uuid, mac_address and iban.

Existing tests for these modules are thin (uuid: 39 lines, mac: 35,
iban: 33). All values below were verified against the cloned source
with a probe script; well-known IBAN examples (DE/GB/FR/NL/CH) were
checked by the mod-97 code path itself, not copied from documentation.

Quirks pinned as-is:
- ``uuid`` accepts *any* UUID version and even brace/URN spellings,
  despite the docstring saying "UUID-v4".
- ``uuid(123)`` raises ``AttributeError`` (the decorator only converts
  ValueError/TypeError/UnicodeError).
"""

from uuid import UUID, uuid1, uuid4

import pytest

from validators import ValidationError, iban, mac_address, uuid


# ---------------------------------------------------------------- uuid


@pytest.mark.parametrize(
    "value",
    [
        "2bc1c94f-0deb-43e9-92a1-4775189ec9f8",  # plain v4
        "2BC1C94F-0DEB-43E9-92A1-4775189EC9F8",  # upper case hex
        "888256d7c49341f19fa33f29d3f820d7",  # 32 hex digits, no dashes
        "{2bc1c94f-0deb-43e9-92a1-4775189ec9f8}",  # braces accepted
        "urn:uuid:2bc1c94f-0deb-43e9-92a1-4775189ec9f8",  # URN accepted
        str(uuid1()),  # version 1 accepted despite the "v4" docstring
        "2bc1c94f-0deb-13e9-92a1-4775189ec9f8",  # version nibble 1
        uuid4(),  # UUID objects are always accepted
        uuid1(),
        UUID("2bc1c94f-0deb-43e9-92a1-4775189ec9f8"),
    ],
)
def test_uuid_returns_true_on_valid_values(value):
    assert uuid(value) is True


@pytest.mark.parametrize(
    "value",
    [
        "",
        None,  # falsy input short-circuits to a failure
        "2bc1c94f-deb-43e9-92a1-4775189ec9f8",  # short second group
        "2bc1c94f-0deb-43e9-92a1-4775189ec9f",  # one hex digit short
        "gbc1c94f-0deb-43e9-92a1-4775189ec9f8",  # 'g' is not hex
        "2bc1c94f 0deb-43e9-92a1-4775189ec9f8",  # space separator
        "2bc1c94f-0deb-43e9-92a1-4775189ec9f8-extra",
        "2bc1c94f-0deb-43e9-92a1",  # truncated
    ],
)
def test_uuid_returns_failed_validation_on_invalid_values(value):
    assert isinstance(uuid(value), ValidationError)


def test_uuid_non_string_non_uuid_raises_attribute_error():
    # Not converted by @validator: AttributeError is not in its catch list.
    with pytest.raises(AttributeError):
        uuid(123)


def test_uuid_failure_carries_the_function_name():
    result = uuid("not-a-uuid")
    assert isinstance(result, ValidationError)
    assert result.func.__name__ == "uuid"
    assert result.value == "not-a-uuid"


# ---------------------------------------------------------------- mac_address


@pytest.mark.parametrize(
    "value",
    [
        "01:23:45:67:ab:CD",  # mixed case, colon separated
        "01-23-45-67-AB-CD",  # dash separated
        "00:00:00:00:00:00",  # all zeros is still a well-formed address
        "FF:FF:FF:FF:FF:FF",  # broadcast
        "aB:cD:eF:01:23:45",
    ],
)
def test_mac_address_returns_true_on_valid_values(value):
    assert mac_address(value) is True


@pytest.mark.parametrize(
    "value",
    [
        "",  # empty
        "00:00:00:00:00",  # only five groups
        "01:23:45:67:AB:CD:EF",  # seven groups
        "01:23-45:67:AB:CD",  # mixed separators are rejected explicitly
        "1:23:45:67:AB:CD",  # single-digit group
        "012:23:45:67:AB:CD",  # three-digit group
        "01:23:45:67:AB:CD:",  # trailing separator
        ":01:23:45:67:AB:CD",  # leading separator
        "gg:23:45:67:AB:CD",  # non-hex
        "01.23.45.67.AB.CD",  # dots are not a separator here
        "01:23:45:67:AB:CD ",  # trailing space breaks the full match
    ],
)
def test_mac_address_returns_failed_validation_on_invalid_values(value):
    assert isinstance(mac_address(value), ValidationError)


# ---------------------------------------------------------------- iban


@pytest.mark.parametrize(
    "value",
    [
        "DE29100500001061045672",
        "de29100500001061045672",  # country code is case-insensitive
        "GB29NWBK60161331926819",
        "FR1420041010050500013M02606",  # letters inside the BBAN
        "NL91ABNA0417164300",
        "CH9300762011623852957",
    ],
)
def test_iban_returns_true_on_valid_values(value):
    assert iban(value) is True


@pytest.mark.parametrize(
    "value",
    [
        "",
        "123456",  # no country code at all
        "DE29",  # far too short
        "DE29" + "1" * 31,  # 35 chars: over the 34-char maximum
        "DE29 1005 0000 1061 0456 72",  # spaces are not stripped
        "DE29100500001061045673",  # one check digit off: mod-97 fails
        "DE2910050000106104567",  # too short to be a real IBAN
        "XX29100500001061045672",  # unknown country still fails mod-97
    ],
)
def test_iban_returns_failed_validation_on_invalid_values(value):
    assert isinstance(iban(value), ValidationError)
