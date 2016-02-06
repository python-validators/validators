# -*- coding: utf-8 -*-
"""
validators
----------

Python Data Validation for Humans™.
"""

from setuptools import setup, find_packages
import os
import re
import sys


PY3 = sys.version_info[0] == 3
HERE = os.path.dirname(os.path.abspath(__file__))


def get_version():
    filename = os.path.join(HERE, 'validators', '__init__.py')
    with open(filename) as f:
        contents = f.read()
    pattern = r"^__version__ = '(.*?)'$"
    return re.search(pattern, contents, re.MULTILINE).group(1)


extras_require = {
    'test': [
        'pytest>=2.2.3',
        'flake8>=2.4.0',
        'isort>=4.2.2'
    ],
}


setup(
    name='validators',
    version=get_version(),
    url='https://github.com/kvesteri/validators',
    license='BSD',
    author='Konsta Vesterinen',
    author_email='konsta@fastmonkeys.com',
    description='Python Data Validation for Humans™.',
    long_description=__doc__,
    packages=find_packages('.', exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'six>=1.4.0',
        'decorator>=3.4.0',
        'ordereddict>=1.1'
        if sys.version_info[0] == 2 and sys.version_info[1] < 7 else '',
        'total_ordering>=0.1'
        if sys.version_info[0] == 2 and sys.version_info[1] < 7 else ''
    ],
    extras_require=extras_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
