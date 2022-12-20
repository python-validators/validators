# -*- coding: utf-8 -*-
import pytest

from validators import hostname, ValidationFailure


@pytest.mark.parametrize(('address',), [
    ('127.0.0.1',),
    ('123.5.77.88',),
    ('12.12.12.12',),
    ('google.com',),
    ('www.duck.com',),
    ('ashdjkha.asdjaks.to',),
])
def test_returns_true_on_valid_hostname(address):
    assert hostname(address)


@pytest.mark.parametrize(('address',), [
    ('abc.0.0.1',),
    ('1278.0.0.1',),
    ('900.200.100.75',),
    ('0127.0.0.1',),
    ('!@#google.com',),
    ('  www.duck.com',),
    ('ashdj_>kha.asdjaks.to',),
])
def test_returns_failed_validation_on_invalid_hostname(address):
    assert isinstance(hostname(address), ValidationFailure)
