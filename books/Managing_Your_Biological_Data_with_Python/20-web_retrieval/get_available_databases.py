'''

Display a list of databases available via Entrez.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 20.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import Entrez

handle = Entrez.einfo()
info = Entrez.read(handle)
print info

raw_input('... press enter for a list of fields in PubMed')

handle = Entrez.einfo(db="pubmed")
record = Entrez.read(handle)
print record.keys()
print record['DbInfo']['Description']
print record['DbInfo']
