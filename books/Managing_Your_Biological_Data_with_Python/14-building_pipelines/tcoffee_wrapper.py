'''

Run tcoffee to create a multiple alignment.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 14.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
# THIS CODE HAS NOT BEEN TESTED BEFORE SUBMISSION

from tcoffeevariables import tcoffeeout
import sys
import os

sys.path.append('pathmodules/')
cmd = 't_coffee -in="file.fasta" –run_name="' + tcoffeeout
          + 'tcoffe.aln" -output=clustalw')
os.system(cmd)
          
