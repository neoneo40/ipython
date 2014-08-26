'''

Find two alpha-C atoms in a PDB structure and calculate their distance.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 10.4.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from math import sqrt
from distance import calc_dist
from parse_pdb import parse_atom_line

pdb = open('3G5U.pdb')
points = []

while len(points) < 2:
    line = pdb.readline()
    if line.startswith("ATOM"):
        chain, res_type, res_num, atom, x, y, z = parse_atom_line(line)
        if res_num == '123' and chain == 'A' and atom == 'CA':
            points.append((x, y, z))
        if res_num == '209' and chain == 'A' and atom == 'CA':
            points.append((x, y, z))

print calc_dist(points[0], points[1])
