'''

SeqRecord objects read by SeqIO can be stored in lists or dictionaries.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 19.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import SeqIO

# read fasta entries to a list
uniprot_iterator = SeqIO.parse("Uniprot.fasta", "fasta")
records = list(uniprot_iterator)
print records[0].id
print records[0].seq

print '-' * 40

# read fasta entries to a dictionary
uniprot_iterator = SeqIO.parse("Uniprot.fasta", "fasta")
records = SeqIO.to_dict(uniprot_iterator)
print records['sp|P03372|ESR1_HUMAN'].id
print records['sp|P03372|ESR1_HUMAN'].seq
