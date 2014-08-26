'''

Avoid the lag when applications share files.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 14.3.5 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
# THIS CODE HAS NOT BEEN TESTED BEFORE SUBMISSION

import sys
import os
sys.path.append('/home/RNA-seq/')
from pathvariables import tophat_dir, index_dir, cufflinks_dir

# the tophat program creates a file 
os.system('tophat -o ' + tophat_dir + ' ' + index_dir + 'sample.fastq')

# here we don't know whether the tophat output file is already finished
# we open and close a dummy file, so the operating system catches up
lag_file = open('dummy.txt', 'w')
lag_file.write('tophat completed')
lag_file.close()

# read the output file
if os.path.exists('/home/RNA-seq/dummy.txt'):	
    os.system('cufflinks -o ' + cufflinks_dir + ' '
              + tophat_dir + '/accepted_hits.bam')
