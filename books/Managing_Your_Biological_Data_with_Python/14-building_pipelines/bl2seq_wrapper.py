'''

Python wrapper for the bl2seq program.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 15.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
# THIS CODE HAS NOT BEEN TESTED BEFORE SUBMISSION

import sys
import os
import urllib2

sys.path.append('pathmodules/')
from blastvariables import *

def run_bl2seq(seq1, seq2):
    os.system("bl2seq -p blastp -i " + input_seq + seq1 + ".fasta -j "
              + input_seq + seq2 + ".fasta -o " + blast_out + seq1
              + "-" + seq2 + ".aln")

def get_seq(seq1, seq2):
    for seq in (seq1, seq2):
        url = 'http://www.uniprot.org/uniprot/' + seq + '.fasta'
        handler = urllib2.urlopen(url)
        fasta = handler.read()
        out = open(input_seq + seq + '.fasta', 'w')
        out.write(fasta)
        out.close()


if __name__ == '__main__':
    try:
        seq1 = sys.argv[1]
        seq2 = sys.argv[2]
    except:
        print 'usage: Bl2seqWrapper.py seq1-UniprotAC seq2-UniprotAC'
        raise SystemExit
    else:
        if os.path.exists(input_seq + seq1 + '.fasta') and os.path.exists(input_seq + seq2 + '.fasta'):
            run_bl2seq(seq1, seq2)
        else:
            get_seq(seq1, seq2)
            run_bl2seq(seq1, seq2)
