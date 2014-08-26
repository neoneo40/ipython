'''

Read a FASTA file and store entries in a dictionary.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 5.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

sequences = {}
ac = ''
seq = ''
for line in open("SwissProt.fasta"):
    if line.startswith('>') and seq != '':
        sequences[ac] = seq
        seq = ''
    if line.startswith('>'):
        ac = line.split('|')[1]
    else:
        seq = seq + line.strip()

sequences[ac] = seq
print sequences.keys()
print sequences['P62258']
