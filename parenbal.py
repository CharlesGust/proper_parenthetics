"""
    paren_check:

    A quick Python function that takes a unicode string (text) as input
     and returns one of three possible values:

    Return 1 if the string is "open"
        (there are more open parens than closed)
    Return 0 if the string is "balanced"
        (there are an equal number of parentheses in the string)
    Return -1 if the string is "broken"
        (there are more closing parens than open)

    Although the typical usage of "more" is to simply do counts, this
        function actually does a left to right scan of the input string
        and returns -1 if the string ever has a closed paren without
        a prior matching open paren, 1 if the string still has an open
        paren at the end, and 0 otherwise, which indicates not only that
        the count of open and closed parens are equal, but that every
        closed paren has a prior matching open paren
"""
from __future__ import unicode_literals


def paren_check(literal):
    """ return 0 if parens balanced, -1 if closed without open, 1 if opened without close """
    if type(literal) != unicode:
        raise TypeError("usage: paren_check(unicode)")

    count = 0
    for x in literal:
        if x == "(":
            count += 1
        elif x == ")":
            count -= 1
            if count < 0:
                break

    return count if count <= 0 else 1
