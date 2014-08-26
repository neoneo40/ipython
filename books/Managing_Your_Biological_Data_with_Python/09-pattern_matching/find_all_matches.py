'''
Find more than one occurrence of a search pattern.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 9.3.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

import re

pattern = re.compile('R.[ST][^P]')
seq = 'RQSAMGSNKSKPKDASQRRRSLEPAENVHGAGGGAFPASQRPSKP'

# findall returns a list of all matches
matches = pattern.findall(seq)
print matches

# finditer returns an iterator of match objects
match_iter = pattern.finditer(seq)
for match in match_iter:
    print match.group(), match.span(), 
    print match.start(), match.end()
