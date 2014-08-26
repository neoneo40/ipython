'''

Example: boolean operators: and, or, not

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 4.3.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
seq = "MGSNKSKPKDASQRRRSLEPAENVHGAGGGAFPASQTPSKPASADGHRGPSAAFAPAAAE"

if 'GGG' in seq and 'RRR'in seq:
    print 'GGG is at position: ', seq.find('GGG')
    print 'RRR is at position: ', seq.find('RRR')

if 'WWW' in seq or 'AAA' in seq:
    print 'Either WWW or AAA occur in the sequence'
     
if 'AAA' in seq and not 'PPP' in seq:
    print 'AAA occurs in the sequence but not PPP'
