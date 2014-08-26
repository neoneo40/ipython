'''

Create a class that uses another class.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 11.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from pea import Pea

class PeaStrain:
    def __init__(self, peas):
        self.peas = peas

    def __repr__(self):
        return 'strain with %i peas'%(len(self.peas))

yellow = Pea('GG')
green = Pea('gg')
strain = PeaStrain([yellow, green])
print strain

