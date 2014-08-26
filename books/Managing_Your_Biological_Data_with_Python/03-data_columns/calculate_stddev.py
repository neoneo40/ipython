'''

Calculate a standard deviation from a list of numbers

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 3.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

import math

data = [3.53, 3.47, 3.51, 3.72, 3.43]
average = sum(data) / len(data)

total = 0.0
for value in data:
    total += (value - average) ** 2
stddev = math.sqrt(total / len(data))

print stddev
