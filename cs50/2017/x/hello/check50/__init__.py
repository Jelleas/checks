import re

from check50 import *

@check()
def exists(check):
    """hello.c exists."""
    check.require("hello.c")

@check("exists")
def compiles(check):
    """hello.c compiles."""
    check.spawn("clang -std=c11 -o hello hello.c").exit(0)

@check("compiles")
def prints_hello(check):
    """prints "hello, world\\n" """
    expected = "[Hh]ello, world!?\n"
    actual = check.spawn("./hello").stdout()
    if not re.match(expected, actual):
        err = Error(Mismatch("hello, world\n", actual))
        if re.match(expected[:-1], actual):
            err.helpers = "Did you forget a newline (\"\\n\") at the end of your printf string?"
        raise err
