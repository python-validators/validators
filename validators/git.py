import re

from .utils import validator

"""
sources:
https://github.com/git/git/blob/master/url.c
https://git-scm.com/docs/git-clone
https://stackoverflow.com/questions/23976019/how-to-verify-valid-format-of-url-as-a-git-repo/60000569#comment111902087_60000569
https://github.com/jonschlinkert/is-git-url
"""
url_regex = re.compile(
    # protocol
    # either prot:// (protocol captured as group 1) or git@serv (server captured as group 2)
    r"(?:(git|ssh|https?)|git@([A-Za-z0-9][A-Za-z0-9\+\.\-_]+)):(?:\/\/)?"
    # username and maybe password, if either provided (both are captured as group 3)
    r"(?:(\S*)@)?"
    # the actual targeted URL as per STD66 (RFC3986) [A-Za-z][A-Za-z0-9+.-]* 
    # with some added leniency for IPs and allowed URI special chars (_~/:) in order to capture full path+ports
    # (entire URI captured as group 4)
    r"([A-Za-z0-9][A-Za-z0-9\+\.\-_\/\~\:]*?)"
    # .git matched if provided
    r"(?:\.git)"
    # ending '/' OR branch name/commit id (captured as group 5)
    r"(\/?|\#[-\d\w._]+?)",
    re.UNICODE | re.IGNORECASE
)


@validator
def git(value: str, strict: bool = False):
    """
    Return whether a given value is a valid git URL.

    If the value is valid git URL this function returns ``True``, otherwise
    :class:`~validators.utils.ValidationFailure`.

    Examples::

        >>> git('git@github.org:username/reponame.git')
        True

        >>> git('git@github.com:username/reponame')
        True

        >>> git('http://192.168.1.127/user/project.git')
        True

        >>> git('git://bitbucket.org/org/repo.git#ff786f9f')
        True

        >>> git('https://www.github.com')
        ValidationFailure(func=git, ...)

        >>> git('git@github.com:username/reponame', strict=True)
        ValidationFailure(func=git, ...)

    :param value: URL address string to validate
    :param strict: (default=False) enfocre URL end with .git (if false, upon validation failure '.git; is added
    to the end if the procided value and validation retried)
    """
    result = url_regex.match(value)

    if result or strict:
        return result
    else: # not strict and failed to match
        # try adding ".git" at end of value and retry
        value = value[:-1] if value.endswith('/') else value + ".git"
        result = url_regex.match(value)
        return result
