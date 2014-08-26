'''

Write and then read the same file

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 3.3.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

file1 = open('count.txt','w')
file1.write('this is just a dummy test')
file1.close()

file2 = open('my_file')
print file2.read()
