'''

Find the insulin sequence in a FASTA file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 5.3.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

swissprot = open("SwissProt.fasta")
insulin_ac = 'P61981'
result = None

while result == None:
    line = swissprot.next()
    if line.startswith('>'):
        ac = line.split('|')[1]
        if ac == insulin_ac:
            result = line.strip()

print result
