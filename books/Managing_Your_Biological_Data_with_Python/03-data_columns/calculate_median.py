'''

Calculate the median from a list of numbers

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 3.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

data = [3.53, 3.47, 3.51, 3.72, 3.43]

data.sort()
mid = len(data) / 2 
if len(data) % 2 == 0:
    median = (data[mid - 1] + data[mid]) / 2.0
else:
    median = data[mid]

print median
