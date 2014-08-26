'''
Read tabular data from a tab-separated text file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 7.4.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

table = []
for line in open('lowry_data.txt'):
    table.append(line.strip().split('\t'))
    
print table
    
