'''

Write a structure object to a PDB file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 21.4.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import PDB
from Bio.PDB import PDBIO

parser = PDB.PDBParser()
structure = parser.get_structure("2DN1", "dn/pdb2dn1.ent")

io = PDBIO()
io.set_structure(structure)
io.save('my_structure.pdb')
