'''

Search papers in PubMed and parse the entries.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 20.2.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import Entrez
from Bio import Medline

keyword = "PyCogent"

# search publications in PubMed
Entrez.email = "my_email@address.com"
handle = Entrez.esearch(db="pubmed", term=keyword)
record = Entrez.read(handle)
pmids = record['IdList']
print pmids

# retrieve Medline entries from PubMed
handle = Entrez.efetch(db="pubmed", id=pmids, rettype="medline", retmode="text")
medline_records = Medline.parse(handle)
records = list(medline_records)

n = 1
for record in records:
    if keyword in record["TI"]:
        print n, ')', record["TI"]
        n += 1
