# -*- coding: utf-8 -*-
import pytest

from validators import iso_4217, ValidationFailure


@pytest.mark.parametrize('value, case_sensitive', [
    ('USD', True),
    ('usd', False),
])
def test_returns_true_on_valid_iso_4217(value, case_sensitive):
    assert iso_4217(value, case_sensitive)


@pytest.mark.parametrize('value, case_sensitive', [
    ('XTB', True),
    ('usd', True),
])
def test_returns_failed_on_valid_iso_4217(value, case_sensitive):
    assert isinstance(iso_4217(value, case_sensitive), ValidationFailure)
