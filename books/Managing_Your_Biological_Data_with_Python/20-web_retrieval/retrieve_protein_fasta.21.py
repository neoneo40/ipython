'''

Retrieve protein sequence entries in FASTA format.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 20.4.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import Entrez

# search IDs of protein sequences by keywords
handle = Entrez.esearch(db="protein", term="Human AND cancer AND p21")
records = Entrez.read(handle)
print records['Count']
id_list = records['IdList'][0:3]

# retrieve sequences 
id_list = ",".join(id_list)
print id_list
handle = Entrez.efetch(db="protein", id=id_list, rettype="fasta", retmode="xml")
records = Entrez.read(handle)
rec = list(records)
print rec[0].keys()
print rec[0]['TSeq_defline']
