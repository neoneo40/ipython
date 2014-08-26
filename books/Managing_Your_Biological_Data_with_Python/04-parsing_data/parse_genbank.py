'''

Read a Genbank file and convert it to a FASTA file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 4.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

genbank_file = open("AY810830.gb")
output_file = open("AY810830.fasta","w")

flag = False
for line in genbank_file:
    if line[0:9] == 'ACCESSION':
        accession = line.split()[1].strip()
        output_file.write('>' + accession + '\n')
    if line[0:6] == 'ORIGIN': 
        flag = True
    elif flag:
        fields = line.split()
        if fields != []:
            seq = ''.join(fields[1:])
            output_file.write(seq.upper() + '\n')
            
genbank_file.close()
output_file.close()


