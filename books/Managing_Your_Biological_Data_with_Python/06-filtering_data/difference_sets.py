'''

Calculate the differences of two sets

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 6.3.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

data_a = set([1, 2, 3, 4, 5, 6])
data_b = set([1, 5, 7, 8, 9])

a_not_b = data_a.difference(data_b)
b_not_a = data_b.difference(data_a)

print a_not_b
print b_not_a


# see also:
a_or_b = data_a.union(data_b)
a_xor_b = data_a.symmetric_difference(data_b)

print a_or_b
print a_xor_b
