# -*- coding: utf-8 -*-
import pytest

from validators import ipv6, ValidationFailure


@pytest.mark.parametrize(('address',), [
    ('::1',),
    ('dead:beef:0:0:0:0:42:1',),
    ('abcd:ef::42:1',),
])
def test_returns_true_on_valid_ipv4_address(address):
    assert ipv6(address)


@pytest.mark.parametrize(('address',), [
    ('abc.0.0.1',),
    ('abcd:1234::123::1',),
    ('1:2:3:4:5:6:7:8:9',),
    ('abcd::1ffff',),
])
def test_returns_failed_validation_on_invalid_ipv6_address(address):
    assert isinstance(ipv6(address), ValidationFailure)
