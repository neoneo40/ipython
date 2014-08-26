'''

Write a list of numbers to a text file

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 3.3.6 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

data = [16.38, 139.90, 441.46, 29.03, 40.93, 202.07, 142.30, 346.00, 300.00]

out = []
for value in data:
    out.append(str(value) + '\n')
open('results.txt', 'w').writelines(out)
