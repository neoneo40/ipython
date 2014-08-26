'''

Find proteins common to two lists.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 4.2.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''


# proteins participating in cell cycle
list_a = []
for line in open("cell_cycle_proteins.txt"):
    list_a.append(line.strip())
print list_a

# proteins expressed in a given cancer cell
list_b = []
for line in open("cancer_cell_proteins.txt"):
    list_b.append(line.strip())	
print list_b

for protein in list_a:
    if protein in list_b:
        print protein, 'detected in the cancer cell'
    else:
        print protein, 'not observed'
