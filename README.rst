validators
==========

|Build Status| |Version Status| |Downloads|

Python data validation for Humans.

Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or a
schema.

.. code-block:: python

    >>> import validators

    >>> validators.email('someone@example.com')
    True


Development
-----------

To install the package for development use `make install`, to run tests use :bash:`make test` and finally to run check linting run :bash:`make lint`.

.. code-block:: bash

    make install  # For installing the package

    make test  # For running tests

    make lint  # For checking lint



Pre-commit hooks are run as soon as you commit something.

To run pre-commit hooks manually

.. code-block:: bash

   pre-commit run --all-files

Resources
---------

- `Documentation <https://validators.readthedocs.io/>`_
- `Issue Tracker <http://github.com/kvesteri/validators/issues>`_
- `Code <http://github.com/kvesteri/validators/>`_


.. |Build Status| image:: https://travis-ci.org/kvesteri/validators.svg?branch=master
   :target: https://travis-ci.org/kvesteri/validators
.. |Version Status| image:: https://img.shields.io/pypi/v/validators.svg
   :target: https://pypi.python.org/pypi/validators/
.. |Downloads| image:: https://img.shields.io/pypi/dm/validators.svg
   :target: https://pypi.python.org/pypi/validators/
