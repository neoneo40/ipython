'''

Generate all possible five aa long fragments from a protein sequence.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 2.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

seq = "PRQTEINSEQWENCE"

for i in range(len(seq)-4):
    print seq[i:i+5]
