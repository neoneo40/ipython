'''

Sort a tuple by converting it to a list.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 8.3.5 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

# sort a tuple
data = (1, 4, 5, 3, 8, 9, 2, 6, 8, 9, 30)
list_data = list(data)
list_data.sort()
new_tup = tuple(data)
print new_tup

# sort a tuple using the sorted() built-in function
new_tup = tuple(sorted(data))
print new_tup

