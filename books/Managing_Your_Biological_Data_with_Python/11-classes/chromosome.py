'''

Chromosome class for import by other code examples.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License
-----------------------------------------------------------
'''

class Chromosome:
    '''Stores basic data about a chromosome.'''
    
    def __init__(self, number, kind, bases, genes):
        '''Sets data for a chromosome.'''
        self.cid = number
        self.ctype = kind
        self.base_pairs = bases
        self.genes = genes

    def get_gene_density(self):
        '''Returns the number of base pairs per gene.'''
        return self.base_pairs / self.genes

    def __repr__(self):
        '''Makes chromosome instances printable.'''
        return "%2s (%s): %11i bp, %4i genes" % \
                (self.cid, self.ctype, self.base_pairs, self.genes)
    

chromosomes = [
    Chromosome('1', 'autosome', 247199719, 4220),
    Chromosome('7', 'autosome', 158821424, 2135), 
    Chromosome('14', 'autosome', 106360585, 1347), 
    Chromosome('X', 'gonosome', 154913754, 1846),
    Chromosome('Y', 'gonosome', 57741652, 454)
    ]
