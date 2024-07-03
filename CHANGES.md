# Changelog

<!--

Note to self: Breaking changes must increment either

- minor version: as long as versions are in 0.y.z or
- major version: when versions are in in x.y.z (x>0)

-->

## 0.30.0 (2024-07-04)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

- feat: add validator for trx addresses by @msamsami in [#384](https://github.com/python-validators/validators/pull/384)

_**Maintenance**_

- maint: bump version by @msamsami in [#384](https://github.com/python-validators/validators/pull/384)

**Full Changelog**: [`0.29.0...0.30.0`](https://github.com/python-validators/validators/compare/0.29.0...0.30.0)

---

## 0.29.0 (2024-07-01)

_**Breaking**_ ⚠️

- patch: moves `btc_address` to `crypto_addresses` by @msamsami in [#383](https://github.com/python-validators/validators/pull/383) on [`2f300b`](https://github.com/python-validators/validators/pull/383/commits/2f300bccf31e7d8914817cac2ca466fd2a0a4d08)

_**Features**_

- feat: add validator for eth addresses by @msamsami in [#383](https://github.com/python-validators/validators/pull/383)

_**Maintenance**_

- chore: update dev deps; adds python EOL info by @yozachar in [#381](https://github.com/python-validators/validators/pull/381)

**Full Changelog**: [`0.28.3...0.29.0`](https://github.com/python-validators/validators/compare/0.28.3...0.29.0)

---

## 0.28.3 (2024-05-25)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

- hotfix: ensure `_tld.txt` is in `sdist` and `bdist` by @yozachar in [#379](https://github.com/python-validators/validators/pull/379)

**Full Changelog**: [`0.28.2...0.28.3`](https://github.com/python-validators/validators/compare/0.28.2...0.28.3)

## 0.28.2 (2024-05-24)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

- fix: corrects a few typo by @yozachar in [#371](https://github.com/python-validators/validators/pull/371)
- build(deps): bump jinja2 from 3.1.3 to 3.1.4 in /package by @dependabot in [#372](https://github.com/python-validators/validators/pull/372)
- fix(ip_address): properly handle private is false by @grleblanc in [#374](https://github.com/python-validators/validators/pull/374)
- chore(url): allow symbols and pictographs in url by @prousso in [#375](https://github.com/python-validators/validators/pull/375)
- build(deps): bump requests from 2.31.0 to 2.32.0 in /package by @dependabot in [#376](https://github.com/python-validators/validators/pull/376)
- chore: fix typo; update dev deps; bump version by @yozachar in [#377](https://github.com/python-validators/validators/pull/377)

**Full Changelog**: [`0.28.1...0.28.2`](https://github.com/python-validators/validators/compare/0.28.1...0.28.2)

## 0.28.1 (2024-04-19)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

- fix: reduce memory footprint when loading TLDs by @yozachar in [#362](https://github.com/python-validators/validators/pull/362)
- build(deps): bump idna from 3.6 to 3.7 in /package by @dependabot in [#365](https://github.com/python-validators/validators/pull/365)
- fix: rfc cases in the `domain` validator by @yozachar in [#367](https://github.com/python-validators/validators/pull/367)
- chore: documentation maintenance  by @yozachar in [#368](https://github.com/python-validators/validators/pull/368)
- chore: update contribution guidelines by @yozachar in [#369](https://github.com/python-validators/validators/pull/369)
- chore: updated dev dependencies; bump version by @yozachar in [#370](https://github.com/python-validators/validators/pull/370)

**Full Changelog**: [`0.28.0...0.28.1`](https://github.com/python-validators/validators/compare/0.28.0...0.28.1)

## 0.28.0 (2024-04-04)

_**Breaking**_ ⚠️

- patch: moves `country_code` module to `country` module by @yozachar in [#357](https://github.com/python-validators/validators/pull/357)

_**Features**_

- feat: adds indian aadhar and pan validator by @yozachar in [#358](https://github.com/python-validators/validators/pull/358)
- feat: adds `finance` validator by @yozachar in [#359](https://github.com/python-validators/validators/pull/359)
- feat: adds `consider_tld` parameter to `domain`, `hostname` and `url` modules by @yozachar in [#360](https://github.com/python-validators/validators/pull/360)

_**Maintenance**_

- maint: updated dev dependencies, doc links; bump version by @yozachar in [#361](https://github.com/python-validators/validators/pull/361)

**Full Changelog**: [`0.27.0...0.28.0`](https://github.com/python-validators/validators/compare/0.27.0...0.28.0)

---

## 0.27.0 (2024-04-03)

_**Breaking**_ ⚠️

- patch: moves `base58` and `base64` into `encoding` by @yozachar in [#354](https://github.com/python-validators/validators/pull/354)

_**Features**_

- feat: lays foundation for URI validation by @yozachar in [#353](https://github.com/python-validators/validators/pull/353)
- feat: adds `private` parameter to `ip_address`, `hostname` & `url` by @yozachar in [#356](https://github.com/python-validators/validators/pull/356)

_**Maintenance**_

- patch: adds `encoding` tests and docs by @yozachar in [#355](https://github.com/python-validators/validators/pull/355)

**Full Changelog**: [`0.26.0...0.27.0`](https://github.com/python-validators/validators/compare/0.26.0...0.27.0)

---

## 0.26.0 (2024-04-02)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

- feat: adds `base58` and `base64` validators by @yozachar in [#351](https://github.com/python-validators/validators/pull/351)

_**Maintenance**_

- fix: regex ignore-case uses only `a-z` by @yozachar in [#349](https://github.com/python-validators/validators/pull/349)
- patch: supported extended latin in username by @yozachar in [#350](https://github.com/python-validators/validators/pull/350)

**Full Changelog**: [`0.25.0...0.26.0`](https://github.com/python-validators/validators/compare/0.25.0...0.26.0)

---

## 0.25.0 (2024-04-02)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

- feat: adds basic `cron` validator by @yozachar in [#348](https://github.com/python-validators/validators/pull/348)

_**Maintenance**_

- maint: adds quick start docs by @yozachar in [#344](https://github.com/python-validators/validators/pull/344)
- fix: `domain` validation is now more consistent across rfcs by @yozachar in [#347](https://github.com/python-validators/validators/pull/347)

**Full Changelog**: [`0.24.2...0.25.0`](https://github.com/python-validators/validators/compare/0.24.2...0.25.0)

---

## 0.24.0 (2024-03-24)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

- feat: conditionally raises `ValidationError`; bump version by @yozachar in [#343](https://github.com/python-validators/validators/pull/343)

_**Maintenance**_

- patch: `domain` & `url` modules by @yozachar in [#339](https://github.com/python-validators/validators/pull/339)
- fix: domain name not confirming to rfc_2782 by @yozachar in [#341](https://github.com/python-validators/validators/pull/341)
- maint: update dev dependencies; adds favicon to docs by @yozachar in [#342](https://github.com/python-validators/validators/pull/342)

**Full Changelog**: [`0.23.2...0.24.0`](https://github.com/python-validators/validators/compare/0.23.2...0.24.0)

---

## 0.23.2 (2024-03-20)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

- maint: rectifies changelog by @yozachar in [#336](ttps://github.com/python-validators/validators/pull/336)
- fix: packaging as well as `rST` & `md` document generation by @yozachar in [#337](ttps://github.com/python-validators/validators/pull/337)

**Full Changelog**: [`0.23.1...0.23.2`](https://github.com/python-validators/validators/compare/0.23.1...0.23.2)

## 0.23.1 (2024-03-19)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

- maint: fix `between` & `length` validators by @yozachar in [#334](https://github.com/python-validators/validators/pull/334)
- fix: manual nav reference for mkdocs; bumps version by @yozachar in [#335](https://github.com/python-validators/validators/pull/335)

**Full Changelog**: [`0.23.0...0.23.1`](https://github.com/python-validators/validators/compare/0.23.0...0.23.1)

## 0.23.0 (2024-03-19)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

- feat: add french i18n validation by @imperosol in [#308](https://github.com/python-validators/validators/pull/308)

_**Maintenance**_

- fix: Valid URLs failing validation - query and fragment parts by @danherbriley in [#297](https://github.com/python-validators/validators/pull/297)
- fix: bug in `between` module by @yozachar in [#301](https://github.com/python-validators/validators/pull/301)
- chore: update dependencies, improve packaging by @yozachar in [#304](https://github.com/python-validators/validators/pull/304)
- Fix fragment check by @darkdragon-001 in [#305](https://github.com/python-validators/validators/pull/305)
- build(deps): bump urllib3 from 2.0.6 to 2.0.7 in /package by @dependabot in [#310](https://github.com/python-validators/validators/pull/310)
- fix: allow pct-encoded entities in fragments by @conitrade-as in [#317](https://github.com/python-validators/validators/pull/317)
- chore: update dev dependencies by @yozachar in [#318](https://github.com/python-validators/validators/pull/318)
- build(deps): bump gitpython from 3.1.37 to 3.1.41 in /package by @dependabot in [#321](https://github.com/python-validators/validators/pull/321)
- build(deps): bump jinja2 from 3.1.2 to 3.1.3 in /package by @dependabot in [#322](https://github.com/python-validators/validators/pull/322)
- chore: monthly updates for Jan'24 by @yozachar in [#324](https://github.com/python-validators/validators/pull/324)
- maint: adds versiond docs; update copyright year by @yozachar in [#329](https://github.com/python-validators/validators/pull/329)
- chore: update dev dependencies by @yozachar in [#330](https://github.com/python-validators/validators/pull/330)
- build(deps): bump gitpython from 3.1.37 to 3.1.41 in /package by @dependabot in [#331](https://github.com/python-validators/validators/pull/331)
- build(deps): bump jinja2 from 3.1.2 to 3.1.3 in /package by @dependabot in [#332](https://github.com/python-validators/validators/pull/332)
- build(deps): bump urllib3 from 2.0.6 to 2.0.7 in /package by @dependabot in [#319](https://github.com/python-validators/validators/pull/319)

**Full Changelog**: [`0.22.0...0.23.0`](https://github.com/python-validators/validators/compare/0.22.0...0.23.0)

---

## 0.22.0 (2023-09-02)

_**Breaking**_ ⚠️

- A new keyword parameter `host_bit = True`, is added to `validators.ipv4` and `validators.ipv6`.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

- fix: url validator considers urls with /#/ as valid by @adrienthiery in [#289](https://github.com/python-validators/validators/pull/289)
- Add note about ValidationFailure to ValidationError in changes.md by @tswfi in [#291](https://github.com/python-validators/validators/pull/291)
- fix: simple hostname validation regex by @yozachar in [#294](https://github.com/python-validators/validators/pull/294)
- fix: strict CIDR IP validation; bump version by @yozachar in [#295](https://github.com/python-validators/validators/pull/295)

**Full Changelog**: [`0.21.2...0.22.0`](https://github.com/python-validators/validators/compare/0.21.2...0.22.0)

---

## 0.21.2 (2023-08-07)

_**Breaking**_ ⚠️

- `ValidationFailure` is renamed to `ValidationError` in [`yozachar@12ae1f5`](https://github.com/yozachar/pyvalidators/commit/12ae1f5850555d11e1f1a2c03f597fd10610215a)

_**Features**_

- Added Country Code Validation by @aviiciii in [#280](https://github.com/python-validators/validators/pull/280)
- add validator ETH addresses (ERC20) by @msamsami in [#276](https://github.com/python-validators/validators/pull/276)

_**Maintenance**_

- feat: refactoring; updates; fixes; bump version by @yozachar in [#283](https://github.com/python-validators/validators/pull/283)(ref: <https://github.com/yozachar/pyvalidators/commit/12ae1f5850555d11e1f1a2c03f597fd10610215a>)
- build(deps): bump pymdown-extensions from 9.11 to 10.0 by @dependabot in [#273](https://github.com/python-validators/validators/pull/273)
- build(deps): bump requests from 2.28.2 to 2.31.0 by @dependabot in [#275](https://github.com/python-validators/validators/pull/275)
- build(deps-dev): bump certifi from 2022.12.7 to 2023.7.22 by @dependabot in [#281](https://github.com/python-validators/validators/pull/281)

**Full Changelog**: [`0.21.1...0.21.2`](https://github.com/python-validators/validators/compare/0.21.1...0.21.2)

## 0.21.1 (2023-04-10)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

- fix: `source .venv/bin/activate` before build by @yozachar in [#260](https://github.com/python-validators/validators/pull/260)
- fix: id-token write permission at job level by @yozachar in [#261](https://github.com/python-validators/validators/pull/261)
- feat: docs can be built with both sphinx & mkdocs by @yozachar in [#262](https://github.com/python-validators/validators/pull/262)
- fix: improves build process by @yozachar in [#263](https://github.com/python-validators/validators/pull/263)
- fix: removes 64-char limit for url path & query by @yozachar in [#264](https://github.com/python-validators/validators/pull/264)

**Full Changelog**: [`0.21.0...0.21.1`](https://github.com/python-validators/validators/compare/0.21.0...0.21.1)

## 0.21.0 (2023-03-25)

_**Breaking**_ ⚠️

- Drops support for all Python versions below `v3.8`.
- Makes API's primary parameter, `positional`, and the remaining, `keyword-only`.
- Keyword-only parameters like `max` and `min`, has been renamed to `max_val` and `min_val` respectively.
- `domain` API now accepts two new keyword-only arguments: `rfc_1034: bool = False` and `rfc_2782: bool = False`.
- `extremes.py` renamed to `_extremes.py` and is no longer exposed.
- `truthy` was discarded in favour of simple `bool()` function.
- `ipv4_cidr()` and `ipv6_cidr()` has been dropped in favour of `cidr: bool = True` and `cidr: bool = True` keyword-only parameters.
- `email()` API now accepts the following keyword-only arguments:
  - `simple_host: bool = False`,
  - `ipv6_address: bool = False`,
  - `ipv4_address: bool = False`,
  - `rfc_1034: bool = False` and
  - `rfc_2782: bool = False`.
- `whitelist=None` has been removed from `email()`.
- `url()` has been refactored, it accepts the following keyword-only arguments:
  - `skip_ipv6_addr: bool = False`,
  - `skip_ipv4_addr: bool = False`,
  - `may_have_port: bool = True`,
  - `simple_host: bool = False`,
  - `rfc_1034: bool = False` and
  - `rfc_2782: bool = False`.
- `public=False` keyword argument has been removed from `url()`.
- Exposes `i18n` functions directly via `__init__.py`.
- `@validator` decorator catches `Exception`.

<!-- please don't shoot me -->

_**Features**_

- Adds `hostname` validator.

_**Maintenance**_

- feat: add build for pypi workflow by @yozachar in [#255](https://github.com/python-validators/validators/pull/255)
- feat: @validator now catches `Exception` by @yozachar in [#254](https://github.com/python-validators/validators/pull/254)
- maint: improves `i18n` package by @yozachar in [#252](https://github.com/python-validators/validators/pull/252)
- maint: misc changes to dev and ci by @yozachar in [#251](https://github.com/python-validators/validators/pull/251)
- maint: misc fixes and improvements by @yozachar in [#249](https://github.com/python-validators/validators/pull/249)
- maint: improves state of package development by @yozachar in [#248](https://github.com/python-validators/validators/pull/248)
- fix: generate dynamic reference docs by @yozachar in [#247](https://github.com/python-validators/validators/pull/247)
- maint: moving docs from `.rst` to `.md` by @yozachar in [#246](https://github.com/python-validators/validators/pull/246)
- maint: improves `url` module by @yozachar in [#245](https://github.com/python-validators/validators/pull/245)
- maint: improve `domain`, `email` & `hostname` by @yozachar in [#244](https://github.com/python-validators/validators/pull/244)
- maint: simplified `hostname` module by @yozachar in [#242](https://github.com/python-validators/validators/pull/242)
- maint: update `email` module by @yozachar in [#241](https://github.com/python-validators/validators/pull/241)
- feat: adds `hostname` validator by @yozachar in [#240](https://github.com/python-validators/validators/pull/240)
- maint: improves `ip_address` module by @yozachar in [#239](https://github.com/python-validators/validators/pull/239)
- fix: misc fixes, use bandit by @yozachar in [#238](https://github.com/python-validators/validators/pull/238)
- Create SECURITY.md by @yozachar in [#237](https://github.com/python-validators/validators/pull/237)
- maint: improves `mac_address`, `slug` and `uuid` by @yozachar in [#236](https://github.com/python-validators/validators/pull/236)
- maint: improve `hashes` and `iban` modules by @yozachar in [#235](https://github.com/python-validators/validators/pull/235)
- feat: auto docs using mkdocstrings by @yozachar in [#234](https://github.com/python-validators/validators/pull/234)
- maint: improves `email` module by @yozachar in [#233](https://github.com/python-validators/validators/pull/233)
- maint: minor improvements by @yozachar in [#232](https://github.com/python-validators/validators/pull/232)
- maint: improves `domain` module by @yozachar in [#231](https://github.com/python-validators/validators/pull/231)
- maint: reformats `card` module, fix typo by @yozachar in [#230](https://github.com/python-validators/validators/pull/230)
- feat: formats google pydoc style for mkdocstring by @yozachar in [#229](https://github.com/python-validators/validators/pull/229)
- maint: refresh `btc_address` module by @yozachar in [#228](https://github.com/python-validators/validators/pull/228)
- maint: improve type annotations by @yozachar in [#227](https://github.com/python-validators/validators/pull/227)
- maint: improves `between` and `length` modules by @yozachar in [#225](https://github.com/python-validators/validators/pull/225)
- maint: follows google's python style guide for docstrings by @yozachar in [#224](https://github.com/python-validators/validators/pull/224)
- feat: type hints in utils.py, gh-actions by @yozachar in [#223](https://github.com/python-validators/validators/pull/223)
- feat: add pyproject.toml, README.md, upd gitignore by @yozachar in [#221](https://github.com/python-validators/validators/pull/221)
- remove Travis CI settings by @ktdreyer in [#196](https://github.com/python-validators/validators/pull/196)

**Full Changelog**: [`0.20.0...0.21.0`](https://github.com/python-validators/validators/compare/0.20.0...0.21.0)

---

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

- Added new validators `ipv4_cidr`, `ipv6_cidr` (#117, pull request courtesy woodruffw)

## 0.13.0 (2019-05-20)

- Added new validator: `es_doi`, `es_nif`, `es_cif`, `es_nie` (#121, pull request courtesy kingbuzzman)

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

- Added `public` parameter to url validator (#26, pull request courtesy Iconceicao)

## 0.10.2 (2016-06-11)

- Fixed various URL validation issues

## 0.10.1 (2016-04-09)

- Fixed domain name validation for numeric domain names (#21, pull request courtesy shaunpud)
- Fixed IBAN validation for Norwegian and Belgian IBANs (#17, pull request courtesy mboelens91)

## 0.10.0 (2016-01-09)

- Added support for internationalized domain names (IDN) in `domain` validator

## 0.9.0 (2015-10-10)

- Added new validator: `domain`
- Added flake8 and isort checks in travis config

## 0.8.0 (2015-06-24)

- Added new validator: `iban`

## 0.7.0 (2014-09-07)

- Fixed errors in code examples.
- Fixed `TypeError` when using `between` validator with `datetime` objects
  like in the code example.
- Changed validators to always return `True` instead of a truthy object when
  the validation succeeds.
- Fixed `truthy` validator to work like it's name suggests. Previously it
  worked like `falsy`.

## 0.6.0 (2014-06-25)

- Added new validator: `slug`

## 0.5.0 (2013-10-31)

- Renamed `finnish_business_id` to `fi_business_id`
- Added new validator: `fi_ssn`

## 0.4.0 (2013-10-29)

- Added new validator: `finnish_business_id`

## 0.3.0 (2013-10-27)

- `number_range` -> `between`

## 0.2.0 (2013-10-22)

- Various new validators: `ipv4`, `ipv6`, `length`, `number_range`,
  `mac_address`, `url`, `uuid`

## 0.1.0 (2013-10-18)

- Initial public release
