'''

Use a Seq object for a single sequence like a string.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 19.3.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import Seq

my_seq = Seq.Seq("AGCATCGTAGCATGCAC")
print my_seq[0]
print my_seq[0:3]
print my_seq.split('T')
print my_seq.count('A')
print my_seq.count('A') / float(len(my_seq))
