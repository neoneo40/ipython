'''
Seq objects can't be changed but MutableSeq objects can

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 19.3.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import Seq
from Bio.Alphabet import IUPAC

seq = Seq.Seq("AGCATCGTAGCATG", IUPAC.unambiguous_dna)
print seq[5]
# SEQ[5] = "T" # doesn't work!

mutable = Seq.MutableSeq("AGCATCGTAGCATG", IUPAC.unambiguous_dna)
mutable[5] = "T"
print mutable
