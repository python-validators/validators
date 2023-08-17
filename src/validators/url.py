"""URL."""

# standard
from functools import lru_cache
import re
from urllib.parse import unquote, urlsplit

# local
from .hostname import hostname
from .utils import validator


@lru_cache
def _username_regex():
    return re.compile(
        # dot-atom
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*$"
        # non-quoted-string
        + r"|^([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*$)",
        re.IGNORECASE,
    )


@lru_cache
def _path_regex():
    return re.compile(
        # allowed symbols
        r"^[\/a-zA-Z0-9\-\.\_\~\!\$\&\'\(\)\*\+\,\;\=\:\@\%"
        # emoticons / emoji
        + r"\U0001F600-\U0001F64F"
        # multilingual unicode ranges
        + r"\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+$",
        re.IGNORECASE,
    )


@lru_cache
def _query_regex():
    return re.compile(r"&?(\w+=?[^\s&]*)", re.IGNORECASE)


def _validate_scheme(value: str):
    """Validate scheme."""
    # More schemes will be considered later.
    return (
        value in {"ftp", "ftps", "git", "http", "https", "rtsp", "sftp", "ssh", "telnet"}
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
        # everything before @ is then considered as a username
        # this is a bad practice, but syntactically valid URL
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
    rfc_1034: bool,
    rfc_2782: bool,
):
    """Validate netloc."""
    if not value or value.count("@") > 1:
        return False
    if value.count("@") < 1:
        return hostname(
            value
            if _confirm_ipv6_skip(value, skip_ipv6_addr) or "]:" in value
            else value.lstrip("[").replace("]", "", 1),
            skip_ipv6_addr=_confirm_ipv6_skip(value, skip_ipv6_addr),
            skip_ipv4_addr=skip_ipv4_addr,
            may_have_port=may_have_port,
            maybe_simple=simple_host,
            rfc_1034=rfc_1034,
            rfc_2782=rfc_2782,
        )
    basic_auth, host = value.rsplit("@", 1)
    return hostname(
        host
        if _confirm_ipv6_skip(host, skip_ipv6_addr) or "]:" in value
        else host.lstrip("[").replace("]", "", 1),
        skip_ipv6_addr=_confirm_ipv6_skip(host, skip_ipv6_addr),
        skip_ipv4_addr=skip_ipv4_addr,
        may_have_port=may_have_port,
        maybe_simple=simple_host,
        rfc_1034=rfc_1034,
        rfc_2782=rfc_2782,
    ) and _validate_auth_segment(basic_auth)


def _validate_optionals(path: str, query: str, fragment: str):
    """Validate path query and fragments."""
    optional_segments = True
    if path:
        optional_segments &= bool(_path_regex().match(path))
    if query:
        optional_segments &= bool(_query_regex().match(query))
    if fragment:
        fragment = fragment.lstrip("/") if fragment.startswith("/") else fragment
        optional_segments &= all(char_to_avoid not in fragment for char_to_avoid in ("/", "?"))
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
    rfc_1034: bool = False,
    rfc_2782: bool = False,
):
    r"""Return whether or not given value is a valid URL.

    This validator was inspired from [URL validator of dperini][1].
    The following diagram is from [urlly][2].

            foo://admin:hunter1@example.com:8042/over/there?name=ferret#nose
            \_/   \___/ \_____/ \_________/ \__/\_________/ \_________/ \__/
             |      |       |       |        |       |          |         |
          scheme username password hostname port    path      query    fragment

    [1]: https://gist.github.com/dperini/729294
    [2]: https://github.com/treeform/urlly

    Examples:
        >>> url('http://duck.com')
        # Output: True
        >>> url('ftp://foobar.dk')
        # Output: True
        >>> url('http://10.0.0.1')
        # Output: True
        >>> url('http://example.com/">user@example.com')
        # Output: ValidationError(func=url, ...)

    Args:
        value:
            URL string to validate.
        skip_ipv6_addr:
            When URL string cannot contain an IPv6 address.
        skip_ipv4_addr:
            When URL string cannot contain an IPv4 address.
        may_have_port:
            URL string may contain port number.
        simple_host:
            URL string maybe only hyphens and alpha-numerals.
        rfc_1034:
            Allow trailing dot in domain/host name.
            Ref: [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034).
        rfc_2782:
            Domain/Host name is of type service record.
            Ref: [RFC 2782](https://www.rfc-editor.org/rfc/rfc2782).

    Returns:
        (Literal[True]):
            If `value` is a valid slug.
        (ValidationError):
            If `value` is an invalid slug.

    Note:
        - *In version 0.11.3*:
            - Added support for URLs containing localhost.
        - *In version 0.11.0*:
            - Made the regular expression case insensitive.
        - *In version 0.10.3*:
            - Added a `public` parameter.
        - *In version 0.10.2*:
            - Added support for various exotic URLs.
            - Fixed various false positives.

    > *New in version 0.2.0*.
    """
    if not value or re.search(r"\s", value):
        # url must not contain any white
        # spaces, they must be encoded
        return False

    try:
        scheme, netloc, path, query, fragment = urlsplit(value)
    except ValueError:
        return False

    return (
        _validate_scheme(scheme)
        and _validate_netloc(
            netloc,
            skip_ipv6_addr,
            skip_ipv4_addr,
            may_have_port,
            simple_host,
            rfc_1034,
            rfc_2782,
        )
        and _validate_optionals(path, query, fragment)
    )
