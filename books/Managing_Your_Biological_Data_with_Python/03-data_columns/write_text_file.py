'''

Write to a text file

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 3.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

output_file = open('counts.txt', 'w')
output_file.write('number of neuron lengths: 7\n')
output_file.close()
