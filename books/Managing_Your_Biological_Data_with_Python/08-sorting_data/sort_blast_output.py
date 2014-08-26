'''
Sort entries in a tabular BLAST output file in reverse order.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 8.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from operator import itemgetter

input_file = open("BlastOut.csv")
output_file = open("BlastOutSorted.csv","w")

# read BLAST output table
table = []
for line in input_file:
    col = line.split(',')
    col[2] = float(col[2])
    table.append(col)

table_sorted = sorted(table, key=itemgetter(2), reverse=True)

# write sorted table to an output file
for row in table_sorted:
    row = [str(x) for x in row]
    output_file.write("\t".join(row) + '\n')
    
input_file.close()
output_file.close()
