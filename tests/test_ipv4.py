# -*- coding: utf-8 -*-
import pytest
from validators import ipv4, FailedValidation


@pytest.mark.parametrize(('address',), [
    ('127.0.0.1',),
    ('123.5.77.88',),
    ('12.12.12.12',),
])
def test_returns_true_on_valid_ipv4_address(address):
    assert ipv4(address)


@pytest.mark.parametrize(('address',), [
    ('abc.0.0.1',),
    ('1278.0.0.1',),
    ('127.0.0.abc',),
    ('900.200.100.75',),
])
def test_returns_failed_validation_on_invalid_email(address):
    assert isinstance(ipv4(address), FailedValidation)




    # def test_ip_address(self):





        # for bad_address in ('abc.0.0.1', 'abcd:1234::123::1', '1:2:3:4:5:6:7:8:9', 'abcd::1ffff'):
        #     self.assertRaises(ValidationError, ip_address(ipv6=True), self.form, DummyField(bad_address))

        # for good_address in ('::1', 'dead:beef:0:0:0:0:42:1', 'abcd:ef::42:1'):
        #     self.assertEqual(ip_address(ipv6=True)(self.form, DummyField(good_address)), None)

        # #Test ValueError on ipv6=False and ipv4=False
        # self.assertRaises(ValueError, ip_address, ipv4=False, ipv6=False)
