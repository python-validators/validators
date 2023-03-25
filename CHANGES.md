# Changelog

## 0.21.0 (2023-03-25)

- feat: add build for pypi workflow by @joe733 in [#255](https://github.com/python-validators/validators/pull/255)
- feat: @validator now catches `Exception` by @joe733 in [#254](https://github.com/python-validators/validators/pull/254)
- maint: improves `i18n` package by @joe733 in [#252](https://github.com/python-validators/validators/pull/252)
- maint: misc changes to dev and ci by @joe733 in [#251](https://github.com/python-validators/validators/pull/251)
- maint: misc fixes and improvements by @joe733 in [#249](https://github.com/python-validators/validators/pull/249)
- maint: improves state of package development by @joe733 in [#248](https://github.com/python-validators/validators/pull/248)
- fix: generate dynamic reference docs by @joe733 in [#247](https://github.com/python-validators/validators/pull/247)
- maint: moving docs from `.rst` to `.md` by @joe733 in [#246](https://github.com/python-validators/validators/pull/246)
- maint: improves `url` module by @joe733 in [#245](https://github.com/python-validators/validators/pull/245)
- maint: improve `domain`, `email` & `hostname` by @joe733 in [#244](https://github.com/python-validators/validators/pull/244)
- maint: simplified `hostname` module by @joe733 in [#242](https://github.com/python-validators/validators/pull/242)
- maint: update `email` module by @joe733 in [#241](https://github.com/python-validators/validators/pull/241)
- feat: adds `hostname` validator by @joe733 in [#240](https://github.com/python-validators/validators/pull/240)
- maint: improves `ip_address` module by @joe733 in [#239](https://github.com/python-validators/validators/pull/239)
- fix: misc fixes, use bandit by @joe733 in [#238](https://github.com/python-validators/validators/pull/238)
- Create SECURITY.md by @joe733 in [#237](https://github.com/python-validators/validators/pull/237)
- maint: improves `mac_address`, `slug` and `uuid` by @joe733 in [#236](https://github.com/python-validators/validators/pull/236)
- maint: improve `hashes` and `iban` modules by @joe733 in [#235](https://github.com/python-validators/validators/pull/235)
- feat: auto docs using mkdocstrings by @joe733 in [#234](https://github.com/python-validators/validators/pull/234)
- maint: improves `email` module by @joe733 in [#233](https://github.com/python-validators/validators/pull/233)
- maint: minor improvements by @joe733 in [#232](https://github.com/python-validators/validators/pull/232)
- maint: improves `domain` module by @joe733 in [#231](https://github.com/python-validators/validators/pull/231)
- maint: reformats `card` module, fix typo by @joe733 in [#230](https://github.com/python-validators/validators/pull/230)
- feat: formats google pydoc style for mkdocstring by @joe733 in [#229](https://github.com/python-validators/validators/pull/229)
- maint: refresh `btc_address` module by @joe733 in [#228](https://github.com/python-validators/validators/pull/228)
- maint: improve type annotations by @joe733 in [#227](https://github.com/python-validators/validators/pull/227)
- maint: improves `between` and `length` modules by @joe733 in [#225](https://github.com/python-validators/validators/pull/225)
- maint: follows google's python style guide for docstrings by @joe733 in [#224](https://github.com/python-validators/validators/pull/224)
- feat: type hints in utils.py, gh-actions by @joe733 in [#223](https://github.com/python-validators/validators/pull/223)
- feat: add pyproject.toml, README.md, upd gitignore by @joe733 in [#221](https://github.com/python-validators/validators/pull/221)
- remove Travis CI settings by @ktdreyer in [#196](https://github.com/python-validators/validators/pull/196)

**Full Changelog**: [0.20.0...0.21.0](https://github.com/python-validators/validators/compare/0.20.0...0.21.0)

## 0.20.0 (2022-06-05)

- Added ipv4 digit lenghts validation (#191, pull request courtesy of Norbiox)
- Fixes error with international URLs that have more than 2 hyphens (#184, pull request courtesy of automationator)

## 0.19.0 (2022-05-04)

- Dropped py34 support
- Improve IPv6 validation (#201, pull request courtesy of SimonIT)

## 0.18.2 (2020-12-18)

- Implement actual validation for old style BTC addresses including checksumming (#182, pull request courtesy of tpatja)
- Use a regex to guesstimate validity of new segwit BTC addresses (#182, pull request courtesy of tpatja)

## 0.18.1 (2020-09-03)

- Made uuid validator accept UUID objects (#174, pull request courtesy of Letsch22)

## 0.18.0 (2020-08-19)

- Added bitcoin address validator (#166, pull request courtesy of daveusa31)

## 0.17.1 (2020-08-03)

- Fixed python_requires using twine

## 0.17.0 (2020-08-02)

- Added python_requires='>=3.4' to setup.py (#163, pull request courtesy of vphilippon)
- Fixed URL validator ip_last_octet regex (#145, pull request courtesy of ghost)

## 0.16.0 (2020-07-16)

- Added support for emojis and more IDNA URLs (#161, pull request courtesy of automationator)

## 0.15.0 (2020-05-07)

- Added bank card validators (#157, pull request courtesy of TimonPeng)

## 0.14.3 (2020-04-02)

- Handle None values gracefully in domain validator (#144, pull request courtesy reahaas)
- Local part of the email address should be less or equal than 64 bytes (#147, pull request courtesy mondeja)
- Removed py27 support
- Removed pypy2 support

## 0.14.2 (2020-01-24)

- Made domain validation case-insensitive (#136, pull request courtesy ehmkah)

## 0.14.1 (2019-12-04)

- Updated domain validator regex to not allow numeric only TLDs (#133, pull request courtesy jmeridth)
- Allow for idna encoded domains (#133, pull request courtesy jmeridth)

## 0.14.0 (2019-08-21)

- Added new validators ``ipv4_cidr``, ``ipv6_cidr`` (#117, pull request courtesy woodruffw)

## 0.13.0 (2019-05-20)

- Added new validator: ``es_doi``, ``es_nif``, ``es_cif``, ``es_nie`` (#121, pull request courtesy kingbuzzman)

## 0.12.6 (2019-05-08)

- Fixed domain validator for single character domains (#118, pull request courtesy kingbuzzman)

## 0.12.5 (2019-04-15)

- Fixed py37 support (#113, pull request courtesy agiletechnologist)

## 0.12.4 (2019-01-02)

- Use inspect.getfullargspec() in py3 (#110, pull request courtesy riconnon)

## 0.12.3 (2018-11-13)

- Added `allow_temporal_ssn` parameter to fi_ssn validator (#97, pull request courtesy quantus)
- Remove py33 support

## 0.12.2 (2018-06-03)

- Fixed IPv4 formatted IP address returning True on ipv6 (#85, pull request courtesy johndlong)
- Fixed IPv6 address parsing (#83, pull request courtesy JulianKahnert)
- Fixed domain validator for international domains and certain edge cases (#76, pull request courtesy Ni-Knight)

## 0.12.1 (2018-01-30)

- Fixed IDNA encoded TLDs in domain validator (#75, pull request courtesy piewpiew)
- Fixed URL validator for URLs with invalid characters in userinfo part (#69, pull request courtesy timb07)

## 0.12.0 (2017-06-03)

- Added hash validators for md5, sha1, sha224, sha256 and sha512
- Made ipv6 validator support IPv4-mapped IPv6 addresses

## 0.11.3 (2017-03-27)

- Fixed URL validator for URLs containing localhost (#51, pull request courtesy vladimirdotk)

## 0.11.2 (2017-01-08)

- Fixed URL validator for urls with query parameters but without path (#44, pull request courtesy zjjw)

## 0.11.1 (2016-11-19)

- Fixed pyp2rpm build problem (#37, pull request courtesy BOPOHA)

## 0.11.0 (2016-08-30)

- Fixed public url validation (#29)
- Made URL validator case insensitive (#27)
- Drop Python 2.6 support

## 0.10.3 (2016-06-13)

- Added ``public`` parameter to url validator (#26, pull request courtesy Iconceicao)

## 0.10.2 (2016-06-11)

- Fixed various URL validation issues

## 0.10.1 (2016-04-09)

- Fixed domain name validation for numeric domain names (#21, pull request courtesy shaunpud)
- Fixed IBAN validation for Norwegian and Belgian IBANs (#17, pull request courtesy mboelens91)

## 0.10.0 (2016-01-09)

- Added support for internationalized domain names in ``domain`` validator

## 0.9.0 (2015-10-10)

- Added new validator: ``domain``
- Added flake8 and isort checks in travis config

## 0.8.0 (2015-06-24)

- Added new validator: ``iban``

## 0.7.0 (2014-09-07)

- Fixed errors in code examples.
- Fixed ``TypeError`` when using ``between`` validator with ``datetime`` objects
  like in the code example.
- Changed validators to always return ``True`` instead of a truthy object when
  the validation succeeds.
- Fixed ``truthy`` validator to work like it's name suggests. Previously it
  worked like ``falsy``.

## 0.6.0 (2014-06-25)

- Added new validator: ``slug``

## 0.5.0 (2013-10-31)

- Renamed ``finnish_business_id`` to ``fi_business_id``
- Added new validator: ``fi_ssn``

## 0.4.0 (2013-10-29)

- Added new validator: ``finnish_business_id``

## 0.3.0 (2013-10-27)

- ``number_range`` -> ``between``

## 0.2.0 (2013-10-22)

- Various new validators: ``ipv4``, ``ipv6``, ``length``, ``number_range``,
  ``mac_address``, ``url``, ``uuid``

## 0.1.0 (2013-10-18)

- Initial public release
