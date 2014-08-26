'''

Remove duplicates from a file with accession numbers
Using a set (faster but distorts order).

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 6.3.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

input_file = open('UniprotID.txt')
output_file = open('UniprotID-unique.txt','w')

unique = set(input_file)
for line in input_file:
    unique.add(line)

for line in unique:
    output_file.write(line)

