'''

Classes can inherit from other classes
and extend their functionality.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 11.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from pea import Pea

class CommentedPea(Pea):

    def __init__(self, genotype, comment):
        Pea.__init__(self, genotype)
        self.comment = comment

    def __repr__(self):
        return  '%s [%s] (%s)' % (self.get_phenotype(), self.genotype, self.comment)

yellow1 = CommentedPea('GG', 'homozygote')
yellow2 = CommentedPea('Gg', 'heterozygote')
print yellow1
