'''

Calculate the distance between two points

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 1.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''


from math import sqrt

x1, y1, z1 = 0.1,  0.0, -0.7
x2, y2, z2 = 0.5, -1.0,  2.7
dx = x1 - x2
dy = y1 - y2
dz = z1 - z2
dsquare = pow(dx, 2) + pow(dy, 2) + pow(dz, 2)
distance = sqrt(dsquare)
print distance
