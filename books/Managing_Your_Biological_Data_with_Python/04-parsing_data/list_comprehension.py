'''
Creating a list with a one line for loop.
Remove non-base symbols from a sequence.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 4.3.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

squares = [x**2 for x in range(5)]
print squares

bases = ['A', 'C', 'T', 'G']
print bases

seq = 'GGACXCAGXXGATT'
print seq

seqlist = [base for base in seq if base in bases]
print seqlist
