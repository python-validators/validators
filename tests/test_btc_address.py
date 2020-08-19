# -*- coding: utf-8 -*-
import pytest

from validators import btc_address, ValidationFailure


@pytest.mark.parametrize(('address',), [
    ('17nuNm4QpgKuDvWy7Jh2AZ2nzZpMyKSKzT',),
    ('3Cwgr2g7vsi1bXDUkpEnVoRLA9w4FZfC69',),
])
def test_returns_true_on_valid_mac_address(address):
    assert btc_address(address)


@pytest.mark.parametrize(('address',), [
    ('ff3Cwgr2g7vsi1bXDUkpEnVoRLA9w4FZfC69',),
    ('b3Cgwgr2g7vsi1bXyjyDUkphEnVoRLA9w4FZfC69',),
])
def test_returns_failed_validation_on_invalid_mac_address(address):
    assert isinstance(btc_address(address), ValidationFailure)
