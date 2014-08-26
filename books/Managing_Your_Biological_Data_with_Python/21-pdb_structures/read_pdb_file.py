'''

Retrieve a PDB structure file from the web and parse it with Biopython.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 21.2.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import PDB

pdbl = PDB.PDBList()
pdbl.retrieve_pdb_file("2DN1")

parser = PDB.PDBParser()
structure = parser.get_structure("2DN1", "dn/pdb2dn1.ent")

for model in structure:
    for chain in model:
        print chain
        for residue in chain:
            print residue.resname, residue.id[1]
            for atom in residue:
                print atom.name, atom.coord
