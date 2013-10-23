"""
validators
----------

Validate scalars like a bauws.
"""

from setuptools import setup, Command
import subprocess
import sys


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)


PY3 = sys.version_info[0] == 3


extras_require = {
    'test': [
        'pytest>=2.2.3',
    ],
}


setup(
    name='validators',
    version='0.2.0',
    url='https://github.com/kvesteri/validators',
    license='BSD',
    author='Konsta Vesterinen',
    author_email='konsta@fastmonkeys.com',
    description='Validate scalars like a bauws.',
    long_description=__doc__,
    packages=['validators'],
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
    cmdclass={'test': PyTest},
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
