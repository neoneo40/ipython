'''

Use R functions to calculate a z-score and p-value.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 13.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
# THIS CODE HAS NOT BEEN TESTED BEFORE SUBMISSION

import rpy2.robjects as ro

r = ro.r
table = r("read.table('RandomDistribution.tsv',sep='\t')")
m = r.mean(table[2], trim=0, na_rm='FALSE')
sdev = r.sd(table[2], na_rm='FALSE')
value = 0.01844
zscore = (m[0] - value) / sdev[0]
print zscore

x = r.abs(zscore)
pvalue = r.pnorm(-x[0])
print pvalue[0]
