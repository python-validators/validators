# -*- coding: utf-8 -*-
import pytest

from validators import iso_4217, ValidationFailure


@pytest.mark.parametrize('value', ['USD'])
def test_returns_true_on_valid_iso_4217(value):
    assert iso_4217(value)


@pytest.mark.parametrize('value', ['XBT'])
def test_returns_failed_on_valid_iso_4217(value):
    assert isinstance(iso_4217(value), ValidationFailure)
