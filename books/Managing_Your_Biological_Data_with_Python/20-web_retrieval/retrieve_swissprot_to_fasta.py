'''

Retrieve a protein sequence from SwissProt and save it as a FASTA file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 20.4.5 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import ExPASy
from Bio import SeqIO

handle = ExPASy.get_sprot_raw("P04637")
seq_record = SeqIO.read(handle, "swiss")
print seq_record.id
print seq_record.description

out = open('myfile.fasta','w')
fasta = SeqIO.write(seq_record, out, "fasta")
out.close()
