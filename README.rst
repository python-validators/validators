validators
==========

Python data validation for Humans.

Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or a
schema.

.. code-block:: python

    >>> import validators

    >>> validators.email('someone@example.com')
    True


Resources
---------

- `Documentation <http://validators.readthedocs.org/>`_
- `Issue Tracker <http://github.com/kvesteri/validators/issues>`_
- `Code <http://github.com/kvesteri/validators/>`_
