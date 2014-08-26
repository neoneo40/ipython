'''

One class can have many instances.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License
-----------------------------------------------------------
'''

class Protein:
    '''Class storing protein names'''
    
    def __init__(self, name):
        '''Sets the name of a protein'''
        self.name = name

    def write(self):
        '''Writes protein name to the screen.'''
        print 'I am ' + self.name

lys = Protein('lysozyme')
myo = Protein('myoglobin')
myo.write()
lys.write()
