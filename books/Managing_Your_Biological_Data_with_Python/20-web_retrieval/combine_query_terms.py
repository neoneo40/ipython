'''

Send queries with combinations of multiple keywords to Entrez.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 20.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import Entrez

handle = Entrez.esearch(db="pubmed", term="PyCogent AND RNA")
record = Entrez.read(handle)
print record['IdList']

handle = Entrez.esearch(db="pubmed", term="PyCogent OR RNA")
record = Entrez.read(handle)
print record['Count']

handle = Entrez.esearch(db="pubmed", term="PyCogent AND 2008[Year]")
record = Entrez.read(handle)
print record['IdList']

handle = Entrez.esearch(db="pubmed", term="C. elegans[Organism] AND 2008[Year] AND Mapk[Gene]")
record = Entrez.read(handle)
print record['Count']
