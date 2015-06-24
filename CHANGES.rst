Changelog
---------

0.8.0 (unreleased)
^^^^^^^^^^^^^^^^^^

- Added new validator: ``iban``


0.7.0 (2014-09-07)
^^^^^^^^^^^^^^^^^^

- Fixed errors in code examples.
- Fixed ``TypeError`` when using ``between`` validator with ``datetime`` objects
  like in the code example.
- Changed validators to always return ``True`` instead of a truthy object when
  the validation succeeds.
- Fixed ``truthy`` validator to work like it's name suggests. Previously it
  worked like ``falsy``.

0.6.0 (2014-06-25)
^^^^^^^^^^^^^^^^^^

- Added new validator: ``slug``


0.5.0 (2013-10-31)
^^^^^^^^^^^^^^^^^^

- Renamed ``finnish_business_id`` to ``fi_business_id``
- Added new validator: ``fi_ssn``


0.4.0 (2013-10-29)
^^^^^^^^^^^^^^^^^^

- Added new validator: ``finnish_business_id``


0.3.0 (2013-10-27)
^^^^^^^^^^^^^^^^^^

- ``number_range`` -> ``between``


0.2.0 (2013-10-22)
^^^^^^^^^^^^^^^^^^

- Various new validators: ``ipv4``, ``ipv6``, ``length``, ``number_range``,
  ``mac_address``, ``url``, ``uuid``


0.1.0 (2013-10-18)
^^^^^^^^^^^^^^^^^^

- Initial public release
