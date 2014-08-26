'''

Reads a FASTA file to to a series of SeqRecord instances.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 19.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import SeqIO

fasta_file = open("Uniprot.fasta","r")
for seq_record in SeqIO.parse(fasta_file, "fasta"):
    print seq_record.id
    print repr(seq_record.seq)
    print len(seq_record)

fasta_file.close()
