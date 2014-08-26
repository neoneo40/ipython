'''

Read a multiple FASTA file and extract human sequences.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 4.4.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

fasta_file = open('SwissProt.fasta','r')
out_file = open('SwissProtHuman.fasta','w')

seq = ''
for line in fasta_file:
    if line[0] == '>' and seq == '':
        # process the first line of the input file
        header = line
    elif line [0] != '>':
        # join the lines with sequence
        seq = seq + line
    elif line[0] == '>' and seq != '':
        # in subsequent lines starting with '>',
        # write the previous header and sequence
        # to the output file. Then re-initialize
        # the header and seq variables for the next record
        if "Homo sapiens" in header:
            out_file.write(header + seq)
        seq = ''
        header = line

# take care of the very last record of the input file
if "Homo sapiens" in header:
    out_file.write(header + seq)
out_file.close()
