'''

Extract the protein sequence from a PDB chain.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 21.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import PDB
from Bio.PDB.Polypeptide import PPBuilder

parser = PDB.PDBParser()
structure = parser.get_structure("2DN1", "dn/pdb2dn1.ent")
ppb = PPBuilder()
peptides = ppb.build_peptides(structure)
for pep in peptides:
    print pep.get_sequence()
    
