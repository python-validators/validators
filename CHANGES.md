# Changelog

<!--

Note to self: Breaking changes must increment either

* minor version: as long as versions are in 0.y.z or
* major version: when versions are in in x.y.z (x>0)

-->

## 0.36.0 (2026-10-10)

_**Breaking**_ ⚠️

* Drops support for Python `v3.9` and `v3.10`. Python `v3.11` or newer is required. ([#488](https://github.com/python-validators/validators/pull/488))
* Stricter validation: the following inputs, previously accepted by mistake, are now rejected.
    * `isin()` now verifies the check digit, which was previously ignored. Lowercase ISINs are still accepted. ([#464](https://github.com/python-validators/validators/pull/464))
    * `cusip()` and `sedol()` require a numeric check digit. ([#487](https://github.com/python-validators/validators/pull/487))
    * `md5()`, `sha1()`, `sha224()`, `sha256()`, `sha384()`, `sha512()`, `base16()`, `base32()`, `base58()` and `base64()` reject trailing characters, such as a trailing newline. ([#486](https://github.com/python-validators/validators/pull/486))
    * `ind_pan()` requires a full-string match. ([#478](https://github.com/python-validators/validators/pull/478))
    * `fr_ssn()` no longer accepts a comma as the gender or Corsica department character. ([#469](https://github.com/python-validators/validators/pull/469), merged as [#491](https://github.com/python-validators/validators/pull/491))
    * `domain()` rejects an underscore in the last label ([#485](https://github.com/python-validators/validators/pull/485)) and names longer than 253 octets once IDNA-encoded, as defined by RFC 1035. ([#461](https://github.com/python-validators/validators/pull/461))
    * `mastercard()` accepts only the 2221-2720 range of the 2-series BINs. ([#467](https://github.com/python-validators/validators/pull/467))
    * `eth_address()` rejects non-hexadecimal characters. ([#466](https://github.com/python-validators/validators/pull/466))
    * `mac_address()` rejects mixed separators. ([#432](https://github.com/python-validators/validators/pull/432))
    * `slug()` rejects a trailing newline, and telnet URIs reject control characters. ([#492](https://github.com/python-validators/validators/pull/492))

_**Features**_

* feat(uri): add telnet URI validation per RFC 4248 by @tofetpuzo in [#446](https://github.com/python-validators/validators/pull/446)
* Accept `file://` URLs per RFC 8089 by @itzzdev09 in [#483](https://github.com/python-validators/validators/pull/483)
* cron: accept a step over a range (e.g. `1-5/2`) and in list items by @itzzdev09 in [#482](https://github.com/python-validators/validators/pull/482)
* Accept lowercase IBANs in `iban()` by @sayantanmandal1 in [#471](https://github.com/python-validators/validators/pull/471)
* fix(cron): accept day-of-week `7` as a Sunday alias by @binggao1230 in [#470](https://github.com/python-validators/validators/pull/470)
* Accept a trailing dot on simple hostnames with `rfc_1034` by @assinscreedFC in [#462](https://github.com/python-validators/validators/pull/462)
* fix(crypto_addresses): accept testnet (`tb`) segwit addresses by @Jordan-Bourillot in [#466](https://github.com/python-validators/validators/pull/466)

_**Maintenance**_

* chore(deps): bump requests from 2.32.3 to 2.32.4 in /package by @dependabot in [#430](https://github.com/python-validators/validators/pull/430)
* fix: reject MAC addresses with mixed separators by @iCasture in [#432](https://github.com/python-validators/validators/pull/432)
* feat: Optimize slug. Extend tests. by @welder87 in [#439](https://github.com/python-validators/validators/pull/439)
* chore: update codebase to reflect new username by @nandgator in [#447](https://github.com/python-validators/validators/pull/447)
* docs: correct PossibleValueTypes note in between to include None by @SAY-5 in [#460](https://github.com/python-validators/validators/pull/460)
* chore!: drop Python 3.9 and 3.10, bump vulnerable dev dependencies by @nandgator in [#488](https://github.com/python-validators/validators/pull/488)
* fix: restore certifi and jinja2 pins downgraded by stale lock by @nandgator in [#489](https://github.com/python-validators/validators/pull/489)
* chore: use native pyproject config for tox and pytest by @nandgator in [#490](https://github.com/python-validators/validators/pull/490)
* test: cover RFC length limits for domain() and hostname() by @nandgator in [#493](https://github.com/python-validators/validators/pull/493)
* chore!: adopt uv and PEP 735 dependency groups by @nandgator in [#495](https://github.com/python-validators/validators/pull/495)
* ci: update GitHub Actions to their latest versions by @nandgator in [#496](https://github.com/python-validators/validators/pull/496)
* docs: explain why the documentation is hosted on the maintainer's fork by @nandgator in [#497](https://github.com/python-validators/validators/pull/497)
* docs: hide badges from the man page; upgrade docs tooling to latest stable by @nandgator in [#498](https://github.com/python-validators/validators/pull/498)
* ci: deploy versioned documentation with mike from the fork by @nandgator in [#500](https://github.com/python-validators/validators/pull/500)
* docs!: build and version the online documentation with Zensical by @nandgator in [#502](https://github.com/python-validators/validators/pull/502)
* ci: publish to PyPI with trusted publishing by @nandgator in [#504](https://github.com/python-validators/validators/pull/504)

**Full Changelog**: [`0.35.0...0.36.0`](https://github.com/python-validators/validators/compare/0.35.0...0.36.0)

## 0.35.0 (2025-05-01)

_**Breaking**_ ⚠️

* Drops support for Python `v3.8`.

_**Features**_

* Validator russian individual tax number by @TheDrunkenBear in [#408](https://github.com/python-validators/validators/pull/408)
* feat: allow custom URL scheme validation by @e3krisztian in [#409](https://github.com/python-validators/validators/pull/409)
* Refactor API: remove print from `ru_inn`, update description, and expose via `__init__` by @TheDrunkenBear in [#419](https://github.com/python-validators/validators/pull/419)
* Add Mir card validation support by @TheDrunkenBear in [#420](https://github.com/python-validators/validators/pull/420)

_**Maintenance**_

* Update README.md by @mattseymour in [#400](https://github.com/python-validators/validators/pull/400)
* fix(domain): accept .onion as a valid TLD by @davidt99 in [#402](https://github.com/python-validators/validators/pull/402)
* fix(url): add hashtag to allowed fragment characters by @davidt99 in [#405](https://github.com/python-validators/validators/pull/405)
* chore(deps): bump jinja2 from 3.1.4 to 3.1.6 in /package by @dependabot in [#414](https://github.com/python-validators/validators/pull/414)
* Fix email regex issue 140 by @cwisdo in [#411](https://github.com/python-validators/validators/pull/411)
* fix(uri): replace `lstrip("mailto:")` with manual prefix removal by @max-moser in [#418](https://github.com/python-validators/validators/pull/418)
* running `doctest` failes by @d-chris in [#417](https://github.com/python-validators/validators/pull/417)
* Fix: Allow Special DOI Cases Used in Public Administration Tests by @MaurizioPilia in [#415](https://github.com/python-validators/validators/pull/415)
* chore: formatting; sync dependencies by @nandgator in [#422](https://github.com/python-validators/validators/pull/422)
* chore: prepare for new release by @nandgator in [#424](https://github.com/python-validators/validators/pull/424)
* chore: updates changelog by @nandgator in [#425](https://github.com/python-validators/validators/pull/425)

**Full Changelog**: [`0.34.0...0.35.0`](https://github.com/python-validators/validators/compare/0.34.0...0.35.0)

## 0.34.0 (2024-09-03)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

* feat: cache IANA TLDs for faster lookups by @salty-horse in [#390](https://github.com/python-validators/validators/pull/390)

_**Maintenance**_

* chore: update dependencies by @nandgator in [#394](https://github.com/python-validators/validators/pull/394)
* docs: adds configuration info by @nandgator in [#395](https://github.com/python-validators/validators/pull/395)

**Full Changelog**: [`0.33.0...0.34.0`](https://github.com/python-validators/validators/compare/0.33.0...0.34.0)

## 0.33.0 (2024-07-15)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

* feat: adds validator for `bsc` addresses by @msamsami in [#389](https://github.com/python-validators/validators/pull/389)

_**Maintenance**_

* chore: bump version by @msamsami in [#389](https://github.com/python-validators/validators/pull/389)

**Full Changelog**: [`0.32.0...0.33.0`](https://github.com/python-validators/validators/compare/0.32.0...0.33.0)

---

## 0.32.0 (2024-07-10)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

* feat: add validator for `sha384` hash by @msamsami in [#387](https://github.com/python-validators/validators/pull/387)

_**Maintenance**_

* maint: bump version by @msamsami in [#387](https://github.com/python-validators/validators/pull/387)

**Full Changelog**: [`0.31.0...0.32.0`](https://github.com/python-validators/validators/compare/0.31.0...0.32.0)

---

## 0.31.0 (2024-07-08)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

* feat: add validators for `base16` and `base32` encodings by @msamsami in [#386](https://github.com/python-validators/validators/pull/386)

_**Maintenance**_

* maint: bump version by @msamsami in [#386](https://github.com/python-validators/validators/pull/386)

**Full Changelog**: [`0.30.0...0.31.0`](https://github.com/python-validators/validators/compare/0.30.0...0.31.0)

---

## 0.30.0 (2024-07-04)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

* feat: add validator for trx addresses by @msamsami in [#384](https://github.com/python-validators/validators/pull/384)

_**Maintenance**_

* maint: bump version by @msamsami in [#384](https://github.com/python-validators/validators/pull/384)

**Full Changelog**: [`0.29.0...0.30.0`](https://github.com/python-validators/validators/compare/0.29.0...0.30.0)

---

## 0.29.0 (2024-07-01)

_**Breaking**_ ⚠️

* patch: moves `btc_address` to `crypto_addresses` by @msamsami in [#383](https://github.com/python-validators/validators/pull/383) on [`2f300b`](https://github.com/python-validators/validators/pull/383/commits/2f300bccf31e7d8914817cac2ca466fd2a0a4d08)

_**Features**_

* feat: add validator for eth addresses by @msamsami in [#383](https://github.com/python-validators/validators/pull/383)

_**Maintenance**_

* chore: update dev deps; adds python EOL info by @nandgator in [#381](https://github.com/python-validators/validators/pull/381)

**Full Changelog**: [`0.28.3...0.29.0`](https://github.com/python-validators/validators/compare/0.28.3...0.29.0)

---

## 0.28.3 (2024-05-25)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

* hotfix: ensure `_tld.txt` is in `sdist` and `bdist` by @nandgator in [#379](https://github.com/python-validators/validators/pull/379)

**Full Changelog**: [`0.28.2...0.28.3`](https://github.com/python-validators/validators/compare/0.28.2...0.28.3)

## 0.28.2 (2024-05-24)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

* fix: corrects a few typo by @nandgator in [#371](https://github.com/python-validators/validators/pull/371)
* build(deps): bump jinja2 from 3.1.3 to 3.1.4 in /package by @dependabot in [#372](https://github.com/python-validators/validators/pull/372)
* fix(ip_address): properly handle private is false by @grleblanc in [#374](https://github.com/python-validators/validators/pull/374)
* chore(url): allow symbols and pictographs in url by @prousso in [#375](https://github.com/python-validators/validators/pull/375)
* build(deps): bump requests from 2.31.0 to 2.32.0 in /package by @dependabot in [#376](https://github.com/python-validators/validators/pull/376)
* chore: fix typo; update dev deps; bump version by @nandgator in [#377](https://github.com/python-validators/validators/pull/377)

**Full Changelog**: [`0.28.1...0.28.2`](https://github.com/python-validators/validators/compare/0.28.1...0.28.2)

## 0.28.1 (2024-04-19)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

* fix: reduce memory footprint when loading TLDs by @nandgator in [#362](https://github.com/python-validators/validators/pull/362)
* build(deps): bump idna from 3.6 to 3.7 in /package by @dependabot in [#365](https://github.com/python-validators/validators/pull/365)
* fix: rfc cases in the `domain` validator by @nandgator in [#367](https://github.com/python-validators/validators/pull/367)
* chore: documentation maintenance  by @nandgator in [#368](https://github.com/python-validators/validators/pull/368)
* chore: update contribution guidelines by @nandgator in [#369](https://github.com/python-validators/validators/pull/369)
* chore: updated dev dependencies; bump version by @nandgator in [#370](https://github.com/python-validators/validators/pull/370)

**Full Changelog**: [`0.28.0...0.28.1`](https://github.com/python-validators/validators/compare/0.28.0...0.28.1)

## 0.28.0 (2024-04-04)

_**Breaking**_ ⚠️

* patch: moves `country_code` module to `country` module by @nandgator in [#357](https://github.com/python-validators/validators/pull/357)

_**Features**_

* feat: adds indian aadhar and pan validator by @nandgator in [#358](https://github.com/python-validators/validators/pull/358)
* feat: adds `finance` validator by @nandgator in [#359](https://github.com/python-validators/validators/pull/359)
* feat: adds `consider_tld` parameter to `domain`, `hostname` and `url` modules by @nandgator in [#360](https://github.com/python-validators/validators/pull/360)

_**Maintenance**_

* maint: updated dev dependencies, doc links; bump version by @nandgator in [#361](https://github.com/python-validators/validators/pull/361)

**Full Changelog**: [`0.27.0...0.28.0`](https://github.com/python-validators/validators/compare/0.27.0...0.28.0)

---

## 0.27.0 (2024-04-03)

_**Breaking**_ ⚠️

* patch: moves `base58` and `base64` into `encoding` by @nandgator in [#354](https://github.com/python-validators/validators/pull/354)

_**Features**_

* feat: lays foundation for URI validation by @nandgator in [#353](https://github.com/python-validators/validators/pull/353)
* feat: adds `private` parameter to `ip_address`, `hostname` & `url` by @nandgator in [#356](https://github.com/python-validators/validators/pull/356)

_**Maintenance**_

* patch: adds `encoding` tests and docs by @nandgator in [#355](https://github.com/python-validators/validators/pull/355)

**Full Changelog**: [`0.26.0...0.27.0`](https://github.com/python-validators/validators/compare/0.26.0...0.27.0)

---

## 0.26.0 (2024-04-02)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

* feat: adds `base58` and `base64` validators by @nandgator in [#351](https://github.com/python-validators/validators/pull/351)

_**Maintenance**_

* fix: regex ignore-case uses only `a-z` by @nandgator in [#349](https://github.com/python-validators/validators/pull/349)
* patch: supported extended latin in username by @nandgator in [#350](https://github.com/python-validators/validators/pull/350)

**Full Changelog**: [`0.25.0...0.26.0`](https://github.com/python-validators/validators/compare/0.25.0...0.26.0)

---

## 0.25.0 (2024-04-02)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

* feat: adds basic `cron` validator by @nandgator in [#348](https://github.com/python-validators/validators/pull/348)

_**Maintenance**_

* maint: adds quick start docs by @nandgator in [#344](https://github.com/python-validators/validators/pull/344)
* fix: `domain` validation is now more consistent across rfcs by @nandgator in [#347](https://github.com/python-validators/validators/pull/347)

**Full Changelog**: [`0.24.2...0.25.0`](https://github.com/python-validators/validators/compare/0.24.2...0.25.0)

---

## 0.24.0 (2024-03-24)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

* feat: conditionally raises `ValidationError`; bump version by @nandgator in [#343](https://github.com/python-validators/validators/pull/343)

_**Maintenance**_

* patch: `domain` & `url` modules by @nandgator in [#339](https://github.com/python-validators/validators/pull/339)
* fix: domain name not confirming to rfc_2782 by @nandgator in [#341](https://github.com/python-validators/validators/pull/341)
* maint: update dev dependencies; adds favicon to docs by @nandgator in [#342](https://github.com/python-validators/validators/pull/342)

**Full Changelog**: [`0.23.2...0.24.0`](https://github.com/python-validators/validators/compare/0.23.2...0.24.0)

---

## 0.23.2 (2024-03-20)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

* maint: rectifies changelog by @nandgator in [#336](ttps://github.com/python-validators/validators/pull/336)
* fix: packaging as well as `rST` & `md` document generation by @nandgator in [#337](ttps://github.com/python-validators/validators/pull/337)

**Full Changelog**: [`0.23.1...0.23.2`](https://github.com/python-validators/validators/compare/0.23.1...0.23.2)

## 0.23.1 (2024-03-19)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

* maint: fix `between` & `length` validators by @nandgator in [#334](https://github.com/python-validators/validators/pull/334)
* fix: manual nav reference for mkdocs; bumps version by @nandgator in [#335](https://github.com/python-validators/validators/pull/335)

**Full Changelog**: [`0.23.0...0.23.1`](https://github.com/python-validators/validators/compare/0.23.0...0.23.1)

## 0.23.0 (2024-03-19)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

* feat: add french i18n validation by @imperosol in [#308](https://github.com/python-validators/validators/pull/308)

_**Maintenance**_

* fix: Valid URLs failing validation * query and fragment parts by @danherbriley in [#297](https://github.com/python-validators/validators/pull/297)
* fix: bug in `between` module by @nandgator in [#301](https://github.com/python-validators/validators/pull/301)
* chore: update dependencies, improve packaging by @nandgator in [#304](https://github.com/python-validators/validators/pull/304)
* Fix fragment check by @darkdragon-001 in [#305](https://github.com/python-validators/validators/pull/305)
* build(deps): bump urllib3 from 2.0.6 to 2.0.7 in /package by @dependabot in [#310](https://github.com/python-validators/validators/pull/310)
* fix: allow pct-encoded entities in fragments by @conitrade-as in [#317](https://github.com/python-validators/validators/pull/317)
* chore: update dev dependencies by @nandgator in [#318](https://github.com/python-validators/validators/pull/318)
* build(deps): bump gitpython from 3.1.37 to 3.1.41 in /package by @dependabot in [#321](https://github.com/python-validators/validators/pull/321)
* build(deps): bump jinja2 from 3.1.2 to 3.1.3 in /package by @dependabot in [#322](https://github.com/python-validators/validators/pull/322)
* chore: monthly updates for Jan'24 by @nandgator in [#324](https://github.com/python-validators/validators/pull/324)
* maint: adds versiond docs; update copyright year by @nandgator in [#329](https://github.com/python-validators/validators/pull/329)
* chore: update dev dependencies by @nandgator in [#330](https://github.com/python-validators/validators/pull/330)
* build(deps): bump gitpython from 3.1.37 to 3.1.41 in /package by @dependabot in [#331](https://github.com/python-validators/validators/pull/331)
* build(deps): bump jinja2 from 3.1.2 to 3.1.3 in /package by @dependabot in [#332](https://github.com/python-validators/validators/pull/332)
* build(deps): bump urllib3 from 2.0.6 to 2.0.7 in /package by @dependabot in [#319](https://github.com/python-validators/validators/pull/319)

**Full Changelog**: [`0.22.0...0.23.0`](https://github.com/python-validators/validators/compare/0.22.0...0.23.0)

---

## 0.22.0 (2023-09-02)

_**Breaking**_ ⚠️

* A new keyword parameter `host_bit = True`, is added to `validators.ipv4` and `validators.ipv6`.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

* fix: url validator considers urls with /#/ as valid by @adrienthiery in [#289](https://github.com/python-validators/validators/pull/289)
* Add note about ValidationFailure to ValidationError in changes.md by @tswfi in [#291](https://github.com/python-validators/validators/pull/291)
* fix: simple hostname validation regex by @nandgator in [#294](https://github.com/python-validators/validators/pull/294)
* fix: strict CIDR IP validation; bump version by @nandgator in [#295](https://github.com/python-validators/validators/pull/295)

**Full Changelog**: [`0.21.2...0.22.0`](https://github.com/python-validators/validators/compare/0.21.2...0.22.0)

---

## 0.21.2 (2023-08-07)

_**Breaking**_ ⚠️

* `ValidationFailure` is renamed to `ValidationError` in [`nandgator@12ae1f5`](https://github.com/nandgator/pyvalidators/commit/12ae1f5850555d11e1f1a2c03f597fd10610215a)

_**Features**_

* Added Country Code Validation by @aviiciii in [#280](https://github.com/python-validators/validators/pull/280)
* add validator ETH addresses (ERC20) by @msamsami in [#276](https://github.com/python-validators/validators/pull/276)

_**Maintenance**_

* feat: refactoring; updates; fixes; bump version by @nandgator in [#283](https://github.com/python-validators/validators/pull/283)(ref: <https://github.com/nandgator/pyvalidators/commit/12ae1f5850555d11e1f1a2c03f597fd10610215a>)
* build(deps): bump pymdown-extensions from 9.11 to 10.0 by @dependabot in [#273](https://github.com/python-validators/validators/pull/273)
* build(deps): bump requests from 2.28.2 to 2.31.0 by @dependabot in [#275](https://github.com/python-validators/validators/pull/275)
* build(deps-dev): bump certifi from 2022.12.7 to 2023.7.22 by @dependabot in [#281](https://github.com/python-validators/validators/pull/281)

**Full Changelog**: [`0.21.1...0.21.2`](https://github.com/python-validators/validators/compare/0.21.1...0.21.2)

## 0.21.1 (2023-04-10)

_**Breaking**_

> No breaking changes were introduced in this version.

_**Features**_

> No features were introduced in this version.

_**Maintenance**_

* fix: `source .venv/bin/activate` before build by @nandgator in [#260](https://github.com/python-validators/validators/pull/260)
* fix: id-token write permission at job level by @nandgator in [#261](https://github.com/python-validators/validators/pull/261)
* feat: docs can be built with both sphinx & mkdocs by @nandgator in [#262](https://github.com/python-validators/validators/pull/262)
* fix: improves build process by @nandgator in [#263](https://github.com/python-validators/validators/pull/263)
* fix: removes 64-char limit for url path & query by @nandgator in [#264](https://github.com/python-validators/validators/pull/264)

**Full Changelog**: [`0.21.0...0.21.1`](https://github.com/python-validators/validators/compare/0.21.0...0.21.1)

## 0.21.0 (2023-03-25)

_**Breaking**_ ⚠️

* Drops support for all Python versions below `v3.8`.
* Makes API's primary parameter, `positional`, and the remaining, `keyword-only`.
* Keyword-only parameters like `max` and `min`, has been renamed to `max_val` and `min_val` respectively.
* `domain` API now accepts two new keyword-only arguments: `rfc_1034: bool = False` and `rfc_2782: bool = False`.
* `extremes.py` renamed to `_extremes.py` and is no longer exposed.
* `truthy` was discarded in favour of simple `bool()` function.
* `ipv4_cidr()` and `ipv6_cidr()` has been dropped in favour of `cidr: bool = True` and `cidr: bool = True` keyword-only parameters.
* `email()` API now accepts the following keyword-only arguments:
  * `simple_host: bool = False`,
  * `ipv6_address: bool = False`,
  * `ipv4_address: bool = False`,
  * `rfc_1034: bool = False` and
  * `rfc_2782: bool = False`.
* `whitelist=None` has been removed from `email()`.
* `url()` has been refactored, it accepts the following keyword-only arguments:
  * `skip_ipv6_addr: bool = False`,
  * `skip_ipv4_addr: bool = False`,
  * `may_have_port: bool = True`,
  * `simple_host: bool = False`,
  * `rfc_1034: bool = False` and
  * `rfc_2782: bool = False`.
* `public=False` keyword argument has been removed from `url()`.
* Exposes `i18n` functions directly via `__init__.py`.
* `@validator` decorator catches `Exception`.

<!-* please don't shoot me -->

_**Features**_

* Adds `hostname` validator.

_**Maintenance**_

* feat: add build for pypi workflow by @nandgator in [#255](https://github.com/python-validators/validators/pull/255)
* feat: @validator now catches `Exception` by @nandgator in [#254](https://github.com/python-validators/validators/pull/254)
* maint: improves `i18n` package by @nandgator in [#252](https://github.com/python-validators/validators/pull/252)
* maint: misc changes to dev and ci by @nandgator in [#251](https://github.com/python-validators/validators/pull/251)
* maint: misc fixes and improvements by @nandgator in [#249](https://github.com/python-validators/validators/pull/249)
* maint: improves state of package development by @nandgator in [#248](https://github.com/python-validators/validators/pull/248)
* fix: generate dynamic reference docs by @nandgator in [#247](https://github.com/python-validators/validators/pull/247)
* maint: moving docs from `.rst` to `.md` by @nandgator in [#246](https://github.com/python-validators/validators/pull/246)
* maint: improves `url` module by @nandgator in [#245](https://github.com/python-validators/validators/pull/245)
* maint: improve `domain`, `email` & `hostname` by @nandgator in [#244](https://github.com/python-validators/validators/pull/244)
* maint: simplified `hostname` module by @nandgator in [#242](https://github.com/python-validators/validators/pull/242)
* maint: update `email` module by @nandgator in [#241](https://github.com/python-validators/validators/pull/241)
* feat: adds `hostname` validator by @nandgator in [#240](https://github.com/python-validators/validators/pull/240)
* maint: improves `ip_address` module by @nandgator in [#239](https://github.com/python-validators/validators/pull/239)
* fix: misc fixes, use bandit by @nandgator in [#238](https://github.com/python-validators/validators/pull/238)
* Create SECURITY.md by @nandgator in [#237](https://github.com/python-validators/validators/pull/237)
* maint: improves `mac_address`, `slug` and `uuid` by @nandgator in [#236](https://github.com/python-validators/validators/pull/236)
* maint: improve `hashes` and `iban` modules by @nandgator in [#235](https://github.com/python-validators/validators/pull/235)
* feat: auto docs using mkdocstrings by @nandgator in [#234](https://github.com/python-validators/validators/pull/234)
* maint: improves `email` module by @nandgator in [#233](https://github.com/python-validators/validators/pull/233)
* maint: minor improvements by @nandgator in [#232](https://github.com/python-validators/validators/pull/232)
* maint: improves `domain` module by @nandgator in [#231](https://github.com/python-validators/validators/pull/231)
* maint: reformats `card` module, fix typo by @nandgator in [#230](https://github.com/python-validators/validators/pull/230)
* feat: formats google pydoc style for mkdocstring by @nandgator in [#229](https://github.com/python-validators/validators/pull/229)
* maint: refresh `btc_address` module by @nandgator in [#228](https://github.com/python-validators/validators/pull/228)
* maint: improve type annotations by @nandgator in [#227](https://github.com/python-validators/validators/pull/227)
* maint: improves `between` and `length` modules by @nandgator in [#225](https://github.com/python-validators/validators/pull/225)
* maint: follows google's python style guide for docstrings by @nandgator in [#224](https://github.com/python-validators/validators/pull/224)
* feat: type hints in utils.py, gh-actions by @nandgator in [#223](https://github.com/python-validators/validators/pull/223)
* feat: add pyproject.toml, README.md, upd gitignore by @nandgator in [#221](https://github.com/python-validators/validators/pull/221)
* remove Travis CI settings by @ktdreyer in [#196](https://github.com/python-validators/validators/pull/196)

**Full Changelog**: [`0.20.0...0.21.0`](https://github.com/python-validators/validators/compare/0.20.0...0.21.0)

---

## 0.20.0 (2022-06-05)

* Added ipv4 digit lenghts validation (#191, pull request courtesy of Norbiox)
* Fixes error with international URLs that have more than 2 hyphens (#184, pull request courtesy of automationator)

## 0.19.0 (2022-05-04)

* Dropped py34 support
* Improve IPv6 validation (#201, pull request courtesy of SimonIT)

## 0.18.2 (2020-12-18)

* Implement actual validation for old style BTC addresses including checksumming (#182, pull request courtesy of tpatja)
* Use a regex to guesstimate validity of new segwit BTC addresses (#182, pull request courtesy of tpatja)

## 0.18.1 (2020-09-03)

* Made uuid validator accept UUID objects (#174, pull request courtesy of Letsch22)

## 0.18.0 (2020-08-19)

* Added bitcoin address validator (#166, pull request courtesy of daveusa31)

## 0.17.1 (2020-08-03)

* Fixed python_requires using twine

## 0.17.0 (2020-08-02)

* Added python_requires='>=3.4' to setup.py (#163, pull request courtesy of vphilippon)
* Fixed URL validator ip_last_octet regex (#145, pull request courtesy of ghost)

## 0.16.0 (2020-07-16)

* Added support for emojis and more IDNA URLs (#161, pull request courtesy of automationator)

## 0.15.0 (2020-05-07)

* Added bank card validators (#157, pull request courtesy of TimonPeng)

## 0.14.3 (2020-04-02)

* Handle None values gracefully in domain validator (#144, pull request courtesy reahaas)
* Local part of the email address should be less or equal than 64 bytes (#147, pull request courtesy mondeja)
* Removed py27 support
* Removed pypy2 support

## 0.14.2 (2020-01-24)

* Made domain validation case-insensitive (#136, pull request courtesy ehmkah)

## 0.14.1 (2019-12-04)

* Updated domain validator regex to not allow numeric only TLDs (#133, pull request courtesy jmeridth)
* Allow for idna encoded domains (#133, pull request courtesy jmeridth)

## 0.14.0 (2019-08-21)

* Added new validators `ipv4_cidr`, `ipv6_cidr` (#117, pull request courtesy woodruffw)

## 0.13.0 (2019-05-20)

* Added new validator: `es_doi`, `es_nif`, `es_cif`, `es_nie` (#121, pull request courtesy kingbuzzman)

## 0.12.6 (2019-05-08)

* Fixed domain validator for single character domains (#118, pull request courtesy kingbuzzman)

## 0.12.5 (2019-04-15)

* Fixed py37 support (#113, pull request courtesy agiletechnologist)

## 0.12.4 (2019-01-02)

* Use inspect.getfullargspec() in py3 (#110, pull request courtesy riconnon)

## 0.12.3 (2018-11-13)

* Added `allow_temporal_ssn` parameter to fi_ssn validator (#97, pull request courtesy quantus)
* Remove py33 support

## 0.12.2 (2018-06-03)

* Fixed IPv4 formatted IP address returning True on ipv6 (#85, pull request courtesy johndlong)
* Fixed IPv6 address parsing (#83, pull request courtesy JulianKahnert)
* Fixed domain validator for international domains and certain edge cases (#76, pull request courtesy Ni-Knight)

## 0.12.1 (2018-01-30)

* Fixed IDNA encoded TLDs in domain validator (#75, pull request courtesy piewpiew)
* Fixed URL validator for URLs with invalid characters in userinfo part (#69, pull request courtesy timb07)

## 0.12.0 (2017-06-03)

* Added hash validators for md5, sha1, sha224, sha256 and sha512
* Made ipv6 validator support IPv4-mapped IPv6 addresses

## 0.11.3 (2017-03-27)

* Fixed URL validator for URLs containing localhost (#51, pull request courtesy vladimirdotk)

## 0.11.2 (2017-01-08)

* Fixed URL validator for urls with query parameters but without path (#44, pull request courtesy zjjw)

## 0.11.1 (2016-11-19)

* Fixed pyp2rpm build problem (#37, pull request courtesy BOPOHA)

## 0.11.0 (2016-08-30)

* Fixed public url validation (#29)
* Made URL validator case insensitive (#27)
* Drop Python 2.6 support

## 0.10.3 (2016-06-13)

* Added `public` parameter to url validator (#26, pull request courtesy Iconceicao)

## 0.10.2 (2016-06-11)

* Fixed various URL validation issues

## 0.10.1 (2016-04-09)

* Fixed domain name validation for numeric domain names (#21, pull request courtesy shaunpud)
* Fixed IBAN validation for Norwegian and Belgian IBANs (#17, pull request courtesy mboelens91)

## 0.10.0 (2016-01-09)

* Added support for internationalized domain names (IDN) in `domain` validator

## 0.9.0 (2015-10-10)

* Added new validator: `domain`
* Added flake8 and isort checks in travis config

## 0.8.0 (2015-06-24)

* Added new validator: `iban`

## 0.7.0 (2014-09-07)

* Fixed errors in code examples.
* Fixed `TypeError` when using `between` validator with `datetime` objects
  like in the code example.
* Changed validators to always return `True` instead of a truthy object when
  the validation succeeds.
* Fixed `truthy` validator to work like it's name suggests. Previously it
  worked like `falsy`.

## 0.6.0 (2014-06-25)

* Added new validator: `slug`

## 0.5.0 (2013-10-31)

* Renamed `finnish_business_id` to `fi_business_id`
* Added new validator: `fi_ssn`

## 0.4.0 (2013-10-29)

* Added new validator: `finnish_business_id`

## 0.3.0 (2013-10-27)

* `number_range` -> `between`

## 0.2.0 (2013-10-22)

* Various new validators: `ipv4`, `ipv6`, `length`, `number_range`,
  `mac_address`, `url`, `uuid`

## 0.1.0 (2013-10-18)

* Initial public release
