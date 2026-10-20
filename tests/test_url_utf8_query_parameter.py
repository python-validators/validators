"""HA-01. Test URL validation with UTF-8 query parameters."""

# local
from validators import url


def test_url_with_utf8_query_parameter():
    """Test that URL validator accepts UTF-8 characters in query parameters."""
    result = url("https://domain.com/search?q=caña")

    assert result is True
