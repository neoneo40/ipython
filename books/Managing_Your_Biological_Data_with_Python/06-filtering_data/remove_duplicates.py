'''

Remove duplicates from a list of accession numbers
Using a list (easier to write but slow for big files).

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 6.3.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

input_file = open('UniprotID.txt')
output_file = open('UniprotID-unique.txt','w')

unique = []
for line in input_file:
    if line not in unique:
        output_file.write(line)
        unique.append(line)

input_file.close()
output_file.close()
