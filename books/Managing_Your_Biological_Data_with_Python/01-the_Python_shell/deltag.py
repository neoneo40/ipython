'''

Calculate the deltaG value of ATP hydrolysis from concentrations

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 1.2.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

ATP = 3.5
ADP = 1.8
Pi = 5.0
R = 0.00831
T = 298
deltaG0 = -30.5

import math
print deltaG0 + R * T * math.log(ADP * Pi / ATP)
