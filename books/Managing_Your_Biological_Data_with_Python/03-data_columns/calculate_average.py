'''

Calculate the average of a list of numbers

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 3.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

# calculate average from float numbers
data = [3.53, 3.47, 3.51, 3.72, 3.43]
average = sum(data) / len(data)
print average

# calculate average from integer numbers
data = [1, 2, 3, 4]
average = float(sum(data)) / len(data)
print average

