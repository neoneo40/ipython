'''

Draw a histogram with R.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 13.4.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
# THIS CODE HAS NOT BEEN TESTED BEFORE SUBMISSION

import rpy2.robjects as ro
from rpy2.robjects.packages import importr

r = ro.r
table = r("read.table('RandomDistribution.tsv',sep='\t')")
grdevices = importr('grDevices')
grdevices.png(file="Plot.png", width=512, height=512)
r.plot(table[1], table[2], xlab="x", ylab="y")
grdevices.dev_off()

grdevices.png(file="Histogram.png", width=512, height=512)
r.hist(table[4], xlab='x', main='Distribution of values')
grdevices.dev_off()
