'''
Example for parsing a text file.
Reads all AC numbers from the deflines of a FASTA file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 4.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

input_file = open("SwissProtSeq.fasta","r")
ac_list = []

for line in input_file:
    if line[0] == '>':
        fields = line.split('|')
        ac_list.append(fields[1])

print ac_list
