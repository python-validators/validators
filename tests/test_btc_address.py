# -*- coding: utf-8 -*-
import pytest

from validators import btc_address, ValidationFailure


@pytest.mark.parametrize(('address',), [
    ('17nuNm4QpgKuDvWy7Jh2AZ2nzZpMyKSKzT',),
    ('3Cwgr2g7vsi1bXDUkpEnVoRLA9w4FZfC69',),
    ('bc1q2ve3m49wyvqnj8mhuk9gqm2jep8gh5cr59vk6j',),
    ('bc1qe3qwtl0m5m8wnzv2w3cmvv4ug4tqenwsfqdaas',),
    ('bc1qxutdwh78302u57x0psad869zwgzj7uxtmvr3j5',),
])
def test_returns_true_on_valid_mac_address(address):
    assert btc_address(address)


@pytest.mark.parametrize(('address',), [
    ('ff3Cwgr2g7vsi1bXDUkpEnVoRLA9w4FZfC69',),
    ('b3Cgwgr2g7vsi1bXyjyDUkphEnVoRLA9w4FZfC69',),
])
def test_returns_failed_validation_on_invalid_mac_address(address):
    assert isinstance(btc_address(address), ValidationFailure)
