'''

Extract three residues from a PDB file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 10.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

import struct
from parse_pdb import parse_atom_line

def main(pdb_filename, residues, output_filename):
    '''writes residues from a PDB file to an output file.'''
    pdb = open(pdb_filename)
    outfile = open(output_filename, "w")
    for line in pdb:
        if line.startswith("ATOM"):
            chain, res_type, res_num, atom, x, y, z = parse_atom_line(line)
            for aa, num in residues:
                if res_type == aa and res_num == num:
                    outfile.write(line)
    outfile.close()

residues = [('ASP', '102'), ('HIS', '57'), ('SER', '195')]
main("1TLD.pdb", residues, "trypsin_triad.pdb")
