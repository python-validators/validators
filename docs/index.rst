validators
==========

Python Data Validation for Humans™.


Why?
====

Python has all kinds of validation tools, but every one of them requires
defining a schema. I wanted to create a simple validation library where
validating a simple value does not require defining a form or a schema.
Apparently `some other guys have felt the same way`_.

.. _some other guys have felt the same way:
   http://opensourcehacker.com/2011/07/07/generic-python-validation-frameworks/

Often I've had for example a case where I just wanted to check if given string
is an email. With ``validators`` this use case becomes as easy as::

    >>> import validators

    >>> validators.email('someone@example.com')
    True


Installation
============

You can install ``validators`` using pip::

    pip install validators


Currently ``validators`` supports python versions 2.6, 2.7, 3.3, 3.4, 3.5 and
PyPy.


Basic validators
================

Each validator in ``validators`` is a simple function that takes the value to
validate and possibly some additional key-value arguments. Each function returns
``True`` when validation succeeds and
:class:`~validators.utils.ValidationFailure` object when validation fails.

:class:`~validators.utils.ValidationFailure` class implements ``__bool__``
method so you can easily check if validation failed::

    >>> if not validators.email('some_bogus_email@@@'):
    ...     # Do something here
    ...     pass

:class:`~validators.utils.ValidationFailure` object also holds all the arguments
passed to original function::

    >>> result = validators.between(3, min=5)
    >>> result.value
    3
    >>> result.min
    5


between
-------

.. module:: validators.between

.. autofunction:: between


domain
------

.. module:: validators.domain

.. autofunction:: domain


email
-----

.. module:: validators.email

.. autofunction:: email


iban
----

.. module:: validators.iban

.. autofunction:: iban

ipv4
----

.. module:: validators.ip_address

.. autofunction:: ipv4

ipv6
----

.. autofunction:: ipv6


length
------

.. module:: validators.length

.. autofunction:: length


mac_address
-----------

.. module:: validators.mac_address

.. autofunction:: mac_address


slug
----

.. module:: validators.slug

.. autofunction:: slug


truthy
------

.. module:: validators.truthy

.. autofunction:: truthy

url
---

.. module:: validators.url

.. autofunction:: url

uuid
----

.. module:: validators.uuid

.. autofunction:: uuid


i18n validators
===============

Finnish
-------

.. module:: validators.i18n.fi

fi_business_id
^^^^^^^^^^^^^^

.. autofunction:: fi_business_id

fi_ssn
^^^^^^

.. autofunction:: fi_ssn


Internals
=========

validator
---------

.. module:: validators.utils

.. autoclass:: ValidationFailure
.. autofunction:: validator
