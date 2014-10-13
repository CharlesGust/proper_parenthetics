#!/usr/bin/env python

"""
code that tests the check_paren() function defined in parenbal.py

can be run with py.test
"""
from __future__ import unicode_literals
import unittest

from parenbal import paren_check


class MyFuncTestCase(unittest.TestCase):
    def test_paren_check(self):
        # check for balanced parens
        self.assertEqual(paren_check(""), 0)
        self.assertEqual(paren_check("()"), 0)
        self.assertEqual(paren_check("()()"), 0)
        self.assertEqual(paren_check("(())"), 0)
        self.assertEqual(paren_check("(}]><[{)"), 0)

        self.assertEqual(paren_check("A(B())"), 0)
        self.assertEqual(paren_check("CAR(CDR(A))"), 0)

        with self.assertRaises(TypeError):
            paren_check()
            paren_check(None)
            paren_check(1)
            paren_check(1.5)
            paren_check(["Hello, World"])
            paren_check((u"()", 0))
            paren_check({u"Hello", u"World"})
            paren_check(u"Hello", u"World")

        # check for closed paren without matching open
        self.assertEqual(paren_check(")"), -1)
        self.assertEqual(paren_check(")("), -1)
        self.assertEqual(paren_check(")(((((((((((("), -1)
        self.assertEqual(paren_check("A(B(C())))"), -1)

        # check for open paren without matching closed
        self.assertEqual(paren_check("("), 1)
        self.assertEqual(paren_check("(("), 1)
        self.assertEqual(paren_check("(((((((((((((()"), 1)
        self.assertEqual(paren_check("CAR(CDR(A)"), 1)

if __name__ == "__main__":
    unittest.main()
