'''
Search a regular expression pattern.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 9.3.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

import re

# compile a pattern and assign it to a variable
pattern = re.compile('R.[ST][^P]')

# define a string with three occurrences of regexp:
seq = 'RQSAMGSNKSKPKDASQRRRSLEPAENVHGAGGGAFPASQRPSKP'

# search for the pattern in the string
match = pattern.search(seq)

# print the first match along the sequence with the group() method
print match.group()
