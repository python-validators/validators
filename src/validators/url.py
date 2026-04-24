"""URL."""

# standard
from functools import lru_cache
import re
from typing import Callable, Optional
from urllib.parse import parse_qs, unquote, urlsplit

# local
from .hostname import hostname
from .utils import validator


def _validate_percent_encoding(value: str):
    """Validate percent-encoding in a URL component."""
    return not bool(re.search(r"%(?![0-9A-Fa-f]{2})", value))


@lru_cache
def _username_regex():
    return re.compile(
        # extended latin
        r"(^[\u0100-\u017F\u0180-\u024F]"
        # dot-atom (FIXED: removed possessive ++)
        + r"|[-!#$%&'*+/=?^_`{}|~0-9a-z]+(?:\.[-!#$%&'*+/=?^_`{}|~0-9a-z]+)*$"
        # non-quoted-string (FIXED: removed possessive *+)
        + r"|^([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\011.])*$)",
        re.IGNORECASE,
    )


@lru_cache
def _path_regex():
    return re.compile(
        # allowed symbols
        r"^[\/a-z0-9\-\.\_\~\!\$\&\'\(\)\*\+\,\;\=\:\@\%"
        # symbols / pictographs
        + r"\U0001F300-\U0001F5FF"
        # emoticons / emoji
        + r"\U0001F600-\U0001F64F"
        # multilingual unicode ranges
        + r"\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+$",
        re.IGNORECASE,
    )


def _validate_scheme(value: str):
    """Validate scheme."""
    return (
        value
        in {
            "ftp",
            "ftps",
            "git",
            "http",
            "https",
            "irc",
            "rtmp",
            "rtmps",
            "rtsp",
            "sftp",
            "ssh",
            "telnet",
        }
        if value
        else False
    )


def _confirm_ipv6_skip(value: str, skip_ipv6_addr: bool):
    """Confirm skip IPv6 check."""
    return skip_ipv6_addr or value.count(":") < 2 or not value.startswith("[")


def _validate_auth_segment(value: str):
    """Validate authentication segment."""
    if not value:
        return True
    if (colon_count := value.count(":")) > 1:
        return _username_regex().match(unquote(value))
    if colon_count < 1:
        return _username_regex().match(value)
    username, password = value.rsplit(":", 1)
    return _username_regex().match(username) and all(
        char_to_avoid not in password for char_to_avoid in ("/", "?", "#", "@")
    )


def _validate_netloc(
    value: str,
    skip_ipv6_addr: bool,
    skip_ipv4_addr: bool,
    may_have_port: bool,
    simple_host: bool,
    consider_tld: bool,
    private: Optional[bool],
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False

    if value.count("@") < 1:
        return hostname(
            (
                value
                if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
                else value.lstrip("[").replace("]", "", 1)
            ),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            consider_tld=consider_tld,
            private=private,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )

    basic_auth, host = value.rsplit("@", 1)

    return hostname(
        (
            host
            if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
            else host.lstrip("[").replace("]", "", 1)
        ),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        consider_tld=consider_tld,
        private=private,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def _validate_optionals(path: str, query: str, fragment: str, strict_query: bool):
    """Validate path query and fragments."""
    optional_segments = True

    if path:
        optional_segments &= bool(_path_regex().match(path)) and _validate_percent_encoding(path)

    if query:
        optional_segments &= _validate_percent_encoding(query)
        if optional_segments:
            try:
                optional_segments &= bool(parse_qs(query, strict_parsing=strict_query, separator="&")) and bool(
                    parse_qs(query, strict_parsing=strict_query, separator=";")
                )
            except TypeError:
                optional_segments &= bool(parse_qs(query, strict_parsing=strict_query))

    if fragment:
        optional_segments &= bool(
            re.fullmatch(r"[0-9a-z?/:@\-._~%!$&'()*+,;=#]*", fragment, re.IGNORECASE)
        ) and _validate_percent_encoding(fragment)

    return optional_segments


@validator
def url(
    value: str,
    /,
    *,
    skip_ipv6_addr: bool = False,
    skip_ipv4_addr: bool = False,
    may_have_port: bool = True,
    simple_host: bool = False,
    strict_query: bool = True,
    consider_tld: bool = False,
    private: Optional[bool] = None,
    rfc_1034: bool = False,
    rfc_2782: bool = False,
    validate_scheme: Callable[[str], bool] = _validate_scheme,
):
    if not value or re.search(r"\s", value):
        return False

    try:
        scheme, netloc, path, query, fragment = urlsplit(value)
    except ValueError:
        return False

    return (
        validate_scheme(scheme)
        and _validate_netloc(
            netloc,
            skip_ipv6_addr,
            skip_ipv4_addr,
            may_have_port,
            simple_host,
            consider_tld,
            private,
            rfc_1034,
            rfc_2782,
        )
        and _validate_optionals(path, query, fragment, strict_query)
    )
