# -*- coding: utf-8 -*-
import os
import pytest
from PIL import Image
from validators import image, ValidationFailure


@pytest.fixture()
def image_file(tmpdir):
    path = os.path.join(str(tmpdir), 'test.png')
    img = Image.new('RGBA', (10, 10))
    img.save(str(path), format='PNG')
    return str(path)


@pytest.fixture()
def text_file(tmpdir):
    path = os.path.join(str(tmpdir), 'test.txt')
    f = open(path, 'w')
    f.close()
    return str(path)


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
    assert image(image_file)


def test_returns_false_on_invalid_image_file(text_file):
    assert isinstance(image(text_file), ValidationFailure)