'''
Predict protein disorder.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 5.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

propensities = {
   'N': 0.2299, 'P': 0.5523, 'Q':-0.18770, 'A':-0.2615,
   'R':-0.1766, 'S': 0.1429, 'C':-0.01515, 'T': 0.0089,
   'D': 0.2276, 'E':-0.2047, 'V':-0.38620, 'F':-0.2256,
   'W':-0.2434, 'G': 0.4332, 'H':-0.00120, 'Y':-0.2075,
   'I':-0.4222, 'K':-0.1001, 'L': 0.33793, 'M':-0.2259
   }

threshold = 0.3

input_seq = "IVGGYTCGANTVPYQVSLNSGYHFCGGSLINSQWVVSAAHCYKSG\
IQVRLGEDNINVVEGNEQFISASKSIVHPSYNSNTLNNDIMLIKLKSAASLNSR\
VASISLPTSCASAGTQCLISGWGNTKSSGTSYPDVLKCLKAPILSDSSCKSAYP\
GQITSNMFCAGYLEGGKDSCQGDSGGPVVCSGKLQGIVSWGSGCAQKNKPGVYT\
KVCNYVSWIKQTIASN"

output_seq = ""

# Cycle over every amino acid in inputSeq
for res in input_seq: 
   if res in propensities:
      if propensities[res] >= threshold:
         output_seq += res.upper()
      else:
         output_seq += res.lower()
   else:
      print 'unrecognized character:', res
      break

print output_seq
