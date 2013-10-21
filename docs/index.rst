validators
==========

Python data validation for Humans.


Why?
====

Python has all kinds of validation tools, but every one of them requires defining a schema. I wanted to create a simple validation library where validating a simple value does not require defining a form or a schema. Apparently some other guys have felt the same way: http://opensourcehacker.com/2011/07/07/generic-python-validation-frameworks/

Often I've had for example a case where I just wanted to check if given string is an email. With `validators` this use case becomes as easy as:

::

    >>> import validators


    >>> validators.email('someone@example.com')
    True


Installation
============


::


    pip install validators


Currently validators supports python versions 2.7 and 3.3.


API
===

Each validator in `validators` is a simple function that takes the value to validate and possibly some additional key-value arguments. Each function returns `True` when validation succeeds and ValidationFailure object when validation fails.

ValidationFailure class implements __bool__ method so you can easily check if validation failed:

::


    if not email('some_bogus_email@@@'):
        # Do something here
        pass


ValidationFailure object also holds all the arguments passed to original function:

::


    result = number_range(3, min=5)
    if not result:
        result.value
        # 3

        result.min
        # 5



.. module:: validators

email
-----

.. autofunction:: email

ipv4
----

.. autofunction:: ipv4

ipv6
----

.. autofunction:: ipv6


length
------

.. autofunction:: length


mac_address
-----------

.. autofunction:: mac_address

number_range
------------

.. autofunction:: number_range


url
---
.. autofunction:: url

uuid
----
.. autofunction:: uuid

