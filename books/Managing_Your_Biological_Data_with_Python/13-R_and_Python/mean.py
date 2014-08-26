'''

Calculate a mean value from a table file.

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
table = r("read.table('RandomDistribution.tsv',sep='\t')")
matrix = r.matrix(table, ncol=7)
mean_first_col = r.mean(matrix[0])
print mean_first_col
