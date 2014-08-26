'''

Calculate the distance between two atoms in a PDB file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 21.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import PDB

parser = PDB.PDBParser()
structure = parser.get_structure("2DN1","dn/pdb2dn1.ent")

model = structure[0]
chain = model['A']
residue_1 = chain[2]
residue_2 = chain[3]
atom_1 = residue_1['CA']
atom_2 = residue_2['CA']

dist = atom_1 - atom_2
print dist
