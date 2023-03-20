"""Test IP Address."""
# -*- coding: utf-8 -*-

# external
import pytest

# local
from validators import ipv6, ipv4, ValidationFailure


@pytest.mark.parametrize(
    ("address",),
    [
        ("127.0.0.1",),
        ("123.5.77.88",),
        ("12.12.12.12",),
        # w/ cidr
        ("127.0.0.1/0",),
        ("123.5.77.88/8",),
        ("12.12.12.12/32",),
    ],
)
def test_returns_true_on_valid_ipv4_address(address: str):
    """Test returns true on valid ipv4 address."""
    assert ipv4(address)
    assert not ipv6(address)


@pytest.mark.parametrize(
    ("address",),
    [
        # leading zeroes error-out from Python 3.9.5
        # ("100.100.033.033",),
        ("900.200.100.75",),
        ("0127.0.0.1",),
        ("abc.0.0.1",),
        # w/ cidr
        ("1.1.1.1/-1",),
        ("1.1.1.1/33",),
        ("1.1.1.1/foo",),
    ],
)
def test_returns_failed_validation_on_invalid_ipv4_address(address: str):
    """Test returns failed validation on invalid ipv4 address."""
    assert isinstance(ipv4(address), ValidationFailure)


@pytest.mark.parametrize(
    ("address",),
    [
        ("::",),
        ("::1",),
        ("1::",),
        ("dead:beef:0:0:0:0000:42:1",),
        ("abcd:ef::42:1",),
        ("0:0:0:0:0:ffff:1.2.3.4",),
        ("::192.168.30.2",),
        ("0000:0000:0000:0000:0000::",),
        ("0:a:b:c:d:e:f::",),
        # w/ cidr
        ("::1/128",),
        ("::1/0",),
        ("dead:beef:0:0:0:0:42:1/8",),
        ("abcd:ef::42:1/32",),
        ("0:0:0:0:0:ffff:1.2.3.4/16",),
        ("2001:0db8:85a3:0000:0000:8a2e:0370:7334/64",),
        ("::192.168.30.2/128",),
    ],
)
def test_returns_true_on_valid_ipv6_address(address: str):
    """Test returns true on valid ipv6 address."""
    assert ipv6(address)
    assert not ipv4(address)


@pytest.mark.parametrize(
    ("address",),
    [
        ("abc.0.0.1",),
        ("abcd:1234::123::1",),
        ("1:2:3:4:5:6:7:8:9",),
        ("1:2:3:4:5:6:7:8::",),
        ("1:2:3:4:5:6:7::8:9",),
        ("abcd::1ffff",),
        ("1111:",),
        (":8888",),
        (":1.2.3.4",),
        ("18:05",),
        (":",),
        (":1:2:",),
        (":1:2::",),
        ("::1:2::",),
        ("8::1:2::9",),
        ("02001:0000:1234:0000:0000:C1C0:ABCD:0876",),
        # w/ cidr
        ("::1/129",),
        ("::1/-1",),
        ("::1/foo",),
    ],
)
def test_returns_failed_validation_on_invalid_ipv6_address(address: str):
    """Test returns failed validation on invalid ipv6 address."""
    assert isinstance(ipv6(address), ValidationFailure)
