'''

Function to calculate distance between two coordinates.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 10.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from math import sqrt

def calc_dist(p1, p2):
    '''returns the distance between two 3D points'''
    dx = p1[0] - p2[0]  	
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    distsq = pow(dx, 2) + pow(dy, 2) + pow(dz, 2)
    distance = sqrt(distsq)
    return distance

print calc_dist([3.0, 3.0, 3.0], [9.0, 9.0, 9.0])
