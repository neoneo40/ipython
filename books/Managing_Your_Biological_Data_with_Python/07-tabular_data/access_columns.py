'''

Access columns in a nested list.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 7.3.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

data = [
    [ 0,  1,  2,  3],
    [10, 11, 12, 13],
    [20, 21, 22, 23]
    ]

columns = zip(*data)
print columns

    

