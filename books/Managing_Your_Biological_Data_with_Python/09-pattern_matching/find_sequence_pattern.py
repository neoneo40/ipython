'''
Find a sequence pattern in a protein sequence.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 9.2.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

import re

seq = 'VSVLTMFRYAGWLDRLYMLVGTQLAAIIHGVALPLMMLI'

pattern = re.compile('[ST]Q')

match = pattern.search(seq)
if match:
    print '%10s' %(seq[match.start() - 4:match.end() + 4])
    print '%6s' % match.group()
else: 
    print "no match"
