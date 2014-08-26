'''

Represent a table as a dictionary and access a single cell.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 7.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

table = [
   {'protein': 0.16, 'ext1': 0.038, 'ext2': 0.044, 'ext3': 0.040},
   {'protein': 0.33, 'ext1': 0.089, 'ext2': 0.095, 'ext3': 0.091},
   {'protein': 0.66, 'ext1': 0.184, 'ext2': 0.191, 'ext3': 0.191},
   {'protein': 1.00, 'ext1': 0.280, 'ext2': 0.292, 'ext3': 0.283},
   {'protein': 1.32, 'ext1': 0.365, 'ext2': 0.367, 'ext3': 0.365},
   {'protein': 1.66, 'ext1': 0.441, 'ext2': 0.443, 'ext3': 0.444}
   ]

cell = table[1]['ext2']

print table
print cell
