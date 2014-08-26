'''

Read from a text file

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 3.3.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

text_file = open('neuron_data.txt')
lines = text_file.readlines()
text_file.close()

print lines
