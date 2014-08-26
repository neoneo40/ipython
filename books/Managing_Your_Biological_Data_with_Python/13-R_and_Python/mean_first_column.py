'''

Calculate a mean value from a table file

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 13.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
# THIS CODE HAS NOT BEEN TESTED BEFORE SUBMISSION

import rpy2.robjects as robjects

r = robjects.r
in_file = open('RandomDistribution.tsv')
numbers = []
for line in in_file.readlines():
    numbers.append(float(line.split()[0]))
r_vector = robjects.FloatVector(numbers)
print r.mean(r_vector)
