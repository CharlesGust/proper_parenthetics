#proper_parenthetics
#===================
This project demonstrates a quick function to check whether parentheses
 in a Unicode string are balanced, when checked left to right.

##Collaborations
Dan Hable clarified that this function should return -1 when the first
 closed paren without a matching open paren is found, rather than when
 there are just more closed parens than open parens.

##Resources
[Stack Overflow 5113618](http://stackoverflow.com/questions/5113618/how-do-i-tell-python-that-sys-argv-is-in-unicode)
 This resource was consulted to see if it was possible to have a command
 line interface to this function. However, sys.argv does not pass
 unicode strings. Because command line passing of unicode strings was
 so difficult, any of the code for a standalone script was removed.
