# -*- coding: utf-8 -*-
import pytest
from PIL import Image
from validators import image, ValidationFailure


@pytest.fixture()
def image_file(tmpdir):
    temp_path = tmpdir.join('test.png')
    new_image = Image.new('RGBA', (10, 10))
    new_image.save(str(temp_path))
    return temp_path


@pytest.mark.parametrize('address', [
    u'https://i.imgur.com/DKUR9Tk.png',
    u'https://i.imgur.com/DKUR9Tk.png?fb'
])
def test_returns_true_on_valid_image_url(address):
    assert image(address)


@pytest.mark.parametrize('address', [
    u'http://www.google.com/'
])
def test_returns_false_on_invalid_image_url(address):
    assert isinstance(image(address), ValidationFailure)


def test_returns_true_on_valid_image_file(image_file):
    assert image(str(image_file))
