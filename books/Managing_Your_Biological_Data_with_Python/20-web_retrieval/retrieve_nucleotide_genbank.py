'''

Retrieve Genbank entries from the nucleotide database at NCBI.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 20.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import Entrez

# search sequences by a combination of keywords
handle = Entrez.esearch(db="nucleotide", term="Homo sapiens AND mRNA AND MapK")
records = Entrez.read(handle)
print records['Count']

top3_records = records['IdList'][0:3]
print top3_records

# retrieve the sequences by their GI numbers
gi_list = ','.join(top3_records)
print gi_list
handle = Entrez.efetch(db="nucleotide", id=gi_list, rettype="gb", retmode="xml")
records = Entrez.read(handle)
print len(records)

print records[0].keys()
print records[0]['GBSeq_organism']

