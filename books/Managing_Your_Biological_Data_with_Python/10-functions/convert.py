'''

Extract a FASTA sequence from a PDB file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 10.2.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

import struct

pdb_format = '6s5s1s4s1s3s1s1s4s1s3s8s8s8s6s6s10s2s3s'

amino_acids = {
    'ALA':'A', 'CYS':'C', 'ASP':'D', 'GLU':'E',
    'PHE':'F', 'GLY':'G', 'HIS':'H', 'LYS':'K',
    'ILE':'I', 'LEU':'L', 'MET':'M', 'ASN':'N',
    'PRO':'P', 'GLN':'Q', 'ARG':'R', 'SER':'S',
    'THR':'T', 'VAL':'V', 'TYR':'Y', 'TRP':'W'
    }

def threeletter2oneletter(residues):
    '''
    Converts the first element of each residue
    to a one letter amino acid symbol
    '''
    for i, threeletter in enumerate(residues):
        residues[i][0] = amino_acids[threeletter[0]]

def get_residues(pdb_file):
    '''
    Reads the PDB input file, extracts the
    residue type and chain from the CA lines
    and appends both to the residues list
    '''
    residues = []
    for line in pdb_file:
        if line[0:4] == "ATOM":
            tmp = struct.unpack(pdb_format, line)
            ca = tmp[3].strip()
            if ca == 'CA':
                res_type = tmp[5].strip()
                chain = tmp[7]
                residues.append([res_type, chain])
    return residues

def write_fasta_records(residues, pdb_id, fasta_file):
    '''
    Write a FASTA record for each PDB chain
    '''
    seq = ''
    chain = residues[0][1]
    for aa, new_chain in residues:
        if new_chain == chain:
            seq = seq + aa
        else:
            # write sequence in FASTA format
            fasta_file.write(">%s_%s\n%s\n" % (pdb_id, chain, seq))
            seq = aa
            chain = new_chain
    # write the last PDB chain
    fasta_file.write(">%s_%s\n%s\n" % (pdb_id, chain, seq))

def extract_sequence(pdb_id):
    '''
    Main function: Opens files, writes files
    and calls other functions.
    '''
    pdb_file = open(pdb_id + ".pdb")
    fasta_file = open(pdb_id + ".fasta", "w")
    residues = get_residues(pdb_file)
    threeletter2oneletter(residues)
    write_fasta_records(residues, pdb_id, fasta_file)
    pdb_file.close()
    fasta_file.close()
    
# call the main function
extract_sequence("3G5U")
