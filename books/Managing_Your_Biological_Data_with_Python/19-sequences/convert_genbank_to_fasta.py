'''

Read and write sequence files with SeqIO

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 19.4.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import SeqIO

genbank_file = open ("AY810830.gbk", "r")
output_file = open("AY810830.fasta", "w")
records = SeqIO.parse(genbank_file, "genbank")
SeqIO.write(records, output_file, "fasta")
output_file.close()
