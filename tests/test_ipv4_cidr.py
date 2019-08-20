# -*- coding: utf-8 -*-
import pytest

from validators import ipv4_cidr, ipv6_cidr, ValidationFailure


@pytest.mark.parametrize(('address',), [
    ('127.0.0.1/0',),
    ('123.5.77.88/8',),
    ('12.12.12.12/32',),
])
def test_returns_true_on_valid_ipv4_address(address):
    assert ipv4_cidr(address)
    assert not ipv6_cidr(address)


@pytest.mark.parametrize(('address',), [
    ('abc.0.0.1',),
    ('1.1.1.1',),
    ('1.1.1.1/-1',),
    ('1.1.1.1/33',),
    ('1.1.1.1/foo',),
])
def test_returns_failed_validation_on_invalid_ipv4_address(address):
    assert isinstance(ipv4_cidr(address), ValidationFailure)
