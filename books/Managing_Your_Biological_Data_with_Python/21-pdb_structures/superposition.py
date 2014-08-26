'''

Superimposes three atoms on top of three others
and calculates a rotation/translation matrix plus RMSD.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 21.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from Bio import PDB

parser = PDB.PDBParser()
structure = parser.get_structure("2DN1", "dn/pdb2dn1.ent")

atom1 = structure[0]["A"][10]["CA"]
atom2 = structure[0]["A"][20]["CA"]
atom3 = structure[0]["A"][30]["CA"]
atom4 = structure[0]["B"][10]["CA"]
atom5 = structure[0]["B"][20]["CA"]
atom6 = structure[0]["B"][30]["CA"]

moving = [atom1, atom2, atom3]
fixed = [atom4, atom5, atom6]

sup = PDB.Superimposer()
sup.set_atoms(fixed, moving)
print sup.rotran
print 'RMS:', sup.rms
