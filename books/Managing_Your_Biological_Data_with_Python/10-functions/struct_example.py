'''

Parse a string to a tuple using the struct module.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 10.3.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

import struct

# unpack() parses the string to a tuple
format = '1s2s1s1s'
line = '12345'
col = struct.unpack(format, line)
print col

# calcsize() returns the number of characters
# in a given format string
format = '30s30s20s1s'
print struct.calcsize(format)
