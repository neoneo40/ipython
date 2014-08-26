'''

Run two external programs from one Python script.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 14.2.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
# THIS CODE HAS NOT BEEN TESTED BEFORE SUBMISSION

import os

tophat_output_dir = '/home/RNA-seq/tophat'
tophat_output_file = 'accepted_hits.bam'
bowtie_index_dir = '/home/RNA-seq/index'
cufflinks_output_dir = '/home/RNA-seq/cufflinks'
cufflinks_output_file = 'transcripts.gtf'
illumina_output_file = 'sample.fastq'

tophat_command = 'tophat -o %s %s %s' % (tophat_output_dir, bowtie_index_dir, illumina_output_file)
os.system(tophat_command)

cufflinks_command = 'cufflinks -o %s %s%s%s' % (cufflinks_output_dir, tophat_output_dir, os.sep, tophat_output_file)
os.system(cufflinks_command)
