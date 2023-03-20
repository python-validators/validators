"""Validate Anything!"""
# -*- coding: utf-8 -*-

from .card import card_number, mastercard, unionpay, discover, diners, visa, amex, jcb
from .hashes import sha512, sha256, sha224, sha1, md5
from .utils import validator, ValidationFailure
from .i18n import fi_business_id, fi_ssn
from .mac_address import mac_address
from .btc_address import btc_address
from .ip_address import ipv6, ipv4
from .hostname import hostname
from .between import between
from .length import length
from .domain import domain
from .email import email
from .uuid import uuid
from .slug import slug
from .iban import iban
from .url import url

__all__ = (
    "amex",
    "between",
    "btc_address",
    "card_number",
    "diners",
    "discover",
    "domain",
    "email",
    "fi_business_id",
    "fi_ssn",
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
)

__version__ = "0.20.0"
