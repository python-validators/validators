# -*- coding: utf-8 -*-
import pytest

from validators import ipv4, ipv6, ValidationFailure


@pytest.mark.parametrize(('address',), [
    ('::',),
    ('::1',),
    ('1::',),
    ('dead:beef:0:0:0:0000:42:1',),
    ('abcd:ef::42:1',),
    ('0:0:0:0:0:ffff:1.2.3.4',),
    ('::192.168.30.2',),
    ('0000:0000:0000:0000:0000::',),
    ('0:a:b:c:d:e:f::',),
])
def test_returns_true_on_valid_ipv6_address(address):
    assert ipv6(address)
    assert not ipv4(address)


@pytest.mark.parametrize(('address',), [
    ('abc.0.0.1',),
    ('abcd:1234::123::1',),
    ('1:2:3:4:5:6:7:8:9',),
    ('1:2:3:4:5:6:7:8::',),
    ('1:2:3:4:5:6:7::8:9',),
    ('abcd::1ffff',),
    ('1111:',),
    (':8888',),
    (':1.2.3.4',),
    ('18:05',),
    (':',),
    (':1:2:',),
    (':1:2::',),
    ('::1:2::',),
    ('8::1:2::9',),
    ('02001:0000:1234:0000:0000:C1C0:ABCD:0876',),
])
def test_returns_failed_validation_on_invalid_ipv6_address(address):
    assert isinstance(ipv6(address), ValidationFailure)
