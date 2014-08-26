'''

Create an interactive plot and histogram from data in a file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 13.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
# THIS CODE HAS NOT BEEN TESTED BEFORE SUBMISSION

import rpy2.robjects as robjects

r = robjects.r
table = r("read.table('RandomDistribution.tsv',sep='\t')")
r.plot(table[1], table[2], xlab="x", ylab="y")
r.hist(table[4], xlab='x', main='Distribution of values')
