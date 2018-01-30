Changelog
---------


0.12.1 (2018-01-30)
^^^^^^^^^^^^^^^^^^^

- Fixed IDNA encoded TLDs in domain validator (#75, pull request courtesy piewpiew)
- Fixed URL validator for URLs with invalid characters in userinfo part (#69, pull request courtesy timb07)


0.12.0 (2017-06-03)
^^^^^^^^^^^^^^^^^^^

- Added hash validators for md5, sha1, sha224, sha256 and sha512
- Made ipv6 validator support IPv4-mapped IPv6 addresses


0.11.3 (2017-03-27)
^^^^^^^^^^^^^^^^^^^

- Fixed URL validator for URLs containing localhost (#51, pull request courtesy vladimirdotk)


0.11.2 (2017-01-08)
^^^^^^^^^^^^^^^^^^^

- Fixed URL validator for urls with query parameters but without path (#44, pull request courtesy zjjw)


0.11.1 (2016-11-19)
^^^^^^^^^^^^^^^^^^^

- Fixed pyp2rpm build problem (#37, pull request courtesy BOPOHA)


0.11.0 (2016-08-30)
^^^^^^^^^^^^^^^^^^^

- Fixed public url validation (#29)
- Made URL validator case insensitive (#27)
- Drop Python 2.6 support


0.10.3 (2016-06-13)
^^^^^^^^^^^^^^^^^^^

- Added ``public`` parameter to url validator (#26, pull request courtesy Iconceicao)


0.10.2 (2016-06-11)
^^^^^^^^^^^^^^^^^^^

- Fixed various URL validation issues


0.10.1 (2016-04-09)
^^^^^^^^^^^^^^^^^^^

- Fixed domain name validation for numeric domain names (#21, pull request courtesy shaunpud)
- Fixed IBAN validation for Norwegian and Belgian IBANs (#17, pull request courtesy mboelens91)


0.10.0 (2016-01-09)
^^^^^^^^^^^^^^^^^^^

- Added support for internationalized domain names in ``domain`` validator


0.9.0 (2015-10-10)
^^^^^^^^^^^^^^^^^^

- Added new validator: ``domain``
- Added flake8 and isort checks in travis config


0.8.0 (2015-06-24)
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
