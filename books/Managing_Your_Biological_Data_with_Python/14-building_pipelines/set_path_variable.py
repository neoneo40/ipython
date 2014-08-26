'''

Add a directory to sys.path where Python is looking for modules.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 14.3.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
# THIS CODE HAS NOT BEEN TESTED BEFORE SUBMISSION

import sys
import os

sys.path.append('/home/RNA-seq/')

from pathvariables import tophat_dir, index_dir

if os.path.exists(tophat_dir) and os.path.exists(index_dir):
    os.system('tophat -o ' + tophat_dir + ' ' + index_dir + 'sample.fastq')
else: 
    print '''You have to create tophat and/or index directories
before running your wrapper'''

