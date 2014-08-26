'''

Find numbers common to three lists.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 6.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

a = set((1, 2, 3, 4, 5))
b = set((2, 4, 6, 7, 1))
c = set((1, 4, 5, 9))

triple_set = [a, b, c]
common = reduce(set.intersection, triple_set)
print common
