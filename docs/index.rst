validators
==========

Why?
====

Python has all kinds of validation tools, but every one of them requires defining a schema. I wanted to create a simple validation library that eases the validation of scalar values.

Often I've had a case where I just wanted to check for example if given string is an email. For this use case it feels awkward to define a Form / Schema class to simply validate a scalar value.

With `validators` validating scalars is as easy as:

::

    >>> import validators


    >>> validators.email('someone@example.com')
    True


Installation
============


::


    pip install validators


Currently validators supports python versions 2.7 and 3.3.



.. toctree::
   :maxdepth: 2

API
===

.. module:: validators

email
-----

.. autofunction:: is_email

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

