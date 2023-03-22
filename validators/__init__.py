"""Validate Anything!"""
# -*- coding: utf-8 -*-

# isort: skip_file

# The following imports are sorted alphabetically, manually.
# Each line is grouped based first or type, then sorted alphabetically.
# This is for the reference documentation.

# local
from .between import between
from .btc_address import btc_address
from .card import amex, card_number, diners, discover, jcb, mastercard, unionpay, visa
from .domain import domain
from .email import email
from .hashes import md5, sha1, sha224, sha256, sha512
from .hostname import hostname
from .iban import iban
from .ip_address import ipv4, ipv6
from .length import length
from .mac_address import mac_address
from .slug import slug
from .url import url
from .utils import validator, ValidationFailure
from .uuid import uuid

from .i18n import es_cif, es_doi, es_nie, es_nif, fi_business_id, fi_ssn

__all__ = (
    "amex",
    "between",
    "btc_address",
    "card_number",
    "diners",
    "discover",
    "domain",
    "email",
    "hostname",
    "iban",
    "ipv4",
    "ipv6",
    "jcb",
    "length",
    "mac_address",
    "mastercard",
    "md5",
    "sha1",
    "sha224",
    "sha256",
    "sha512",
    "slug",
    "unionpay",
    "url",
    "uuid",
    "ValidationFailure",
    "validator",
    "visa",
    # i18n
    "es_cif",
    "es_doi",
    "es_nie",
    "es_nif",
    "fi_business_id",
    "fi_ssn",
)

__version__ = "0.20.0"
