'''

Filter transcripts from NGS.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 6.2.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
tracking = open('transcripts.tracking', 'r')
out_file = open('transcripts-filtered.tracking', 'w')

for track in tracking:
    # split tab-separated columns
    columns = track.strip().split('\t')
    wildtype = columns[4:7].count('-')
    treatment = columns[7:10].count('-')
    if wildtype < 2 or treatment < 2:
        out_file.write(track)
	
tracking.close()
out_file.close()
