'''

Search for non-header lines in a FASTA file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 5.3.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

rna = ''
for line in open('A06662-RNA.fasta'):
    if not line.startswith('>'): 
        rna = rna + line.strip()
