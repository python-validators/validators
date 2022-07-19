import re

from .utils import validator


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

        >>> git('git@bitbucket.org:username/reponame.git')
        True

        >>> git('http://192.168.1.127/user/project')
        True

        >>> git('git://github.com/somthing/somthing.git#ff786f9f')
        True

        >>> git('https://www.github.com')
        ValidationFailure(func=git, ...)

        >>> git('http://192.168.1.127/user/project', strict=True)
        ValidationFailure(func=git, ...)

    :param value: URL address string to validate
    :param strict: (default=False) enfocre URL end with .git
    """
    result = url_regex.match(value)

    if result or strict:
        return result
    else: # not strict and failed to match
        # try adding ".git" at end of value and retry
        value = value[:-1] if value.endswith('/') else value + ".git"
        result = url_regex.match(value)
        return result

'''
git@bitbucket.org:username/reponame.git
https://username@bitbucket.org/otherusername/reponame.git
https://github.com/username/reponame.git
git@github.com:username/reponame.git
git@gitlab.com:groupname/reponame.git
https://gitlab.com/groupname/reponame.git
git@bitbucket.org:workspace/reponame.git
https://username@bitbucket.org/workspace/reponame.git
https://bitbucket.org/workspace/reponame.git
git@gitlab.com:username/reponame.git
https://gitlab.com/username/reponame.git
git://github.com/somthing/somthing.git#ff786f9f
git://github.com/somthing/somthing.git#gh-pages
git://github.com/somthing/somthing.git#master
git://github.com/somthing/somthing.git#Quick-Fix
git://github.com/somthing/somthing.git#quick_fix
git://github.com/somthing/somthing.git#v0.1.0
git://host.xz/path/to/repo.git/
git://host.xz/~user/path/to/repo.git/
git@192.168.101.127:user/project.git
git@github.com:user/project.git
git@github.com:user/some-project.git
git@github.com:user/some-project.git
git@github.com:user/some_project.git
git@github.com:user/some_project.git
http://github.com/user/project.git
http://host.xz/path/to/repo.git/
https://github.com/user/project.git
https://host.xz/path/to/repo.git/
https://username::;*%$:@github.com/username/repository.git
https://username:$fooABC@:@github.com/username/repository.git
https://username:password@github.com/username/repository.git
ssh://host.xz/path/to/repo.git/
ssh://host.xz/path/to/repo.git/
ssh://host.xz/~/path/to/repo.git
ssh://host.xz/~user/path/to/repo.git/
ssh://user@host.xz/path/to/repo.git/
ssh://user@host.xz/path/to/repo.git/
ssh://user@host.xz/~/path/to/repo.git
ssh://user@host.xz/~user/path/to/repo.git/
ssh://user@host.xz:port/path/to/repo.git/
https://username@bitbucket.org:8080/otherusername/reponame.git
ssh://host.xz:port/path/to/repo.git/
ssh://host.xz:1234/path/to/repo.git/
https://192.168.1.127/user/project.git
http://192.168.1.127/user/project.git


https://www.github.com
git@bitbucket.org:username/repo name.git
https://gitlab.com/username/reponame.git -b branch
https://gitlab.com/username/reponame.git --flag
https://gitlab.com/username/reponame.git \-f
/path/to/repo.git/
file:///path/to/repo.git/
file://~/path/to/repo.git/
git@github.com:user/some_project.git/foo
git@github.com:user/some_project.gitfoo
host.xz:/path/to/repo.git/
host.xz:path/to/repo.git
host.xz:~user/path/to/repo.git/
path/to/repo.git/
rsync://host.xz/path/to/repo.git/
user@host.xz:/path/to/repo.git/
user@host.xz:path/to/repo.git
user@host.xz:~user/path/to/repo.git/
~/path/to/repo.git
git@bitbucket.org:username/reponame.gi

'''