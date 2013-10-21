import re
from .utils import validator


regex = (
    r'^[a-z]+://([^/:]+{tld}|([0-9]{{1,3}}\.)'
    r'{{3}}[0-9]{{1,3}})(:[0-9]+)?(\/.*)?$'
)

pattern_with_tld = re.compile(regex.format(tld=r'\.[a-z]{2,10}'))
pattern_without_tld = re.compile(regex.format(tld=''))


@validator
def url(value, require_tld=True):
    if require_tld:
        return pattern_with_tld.match(value)
    return pattern_without_tld.match(value)
