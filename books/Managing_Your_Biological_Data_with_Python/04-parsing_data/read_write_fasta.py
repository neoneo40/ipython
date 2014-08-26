'''

Write all headers from a FASTA file to a separate file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 4.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

fasta_file = open('SwissProt.fasta','r')
out_file = open('SwissProt.header','w')

for line in fasta_file:
    if line[0:1] == '>':
        out_file.write(line)
out_file.close()
