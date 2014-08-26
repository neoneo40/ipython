'''

Calculate the differences of two lists

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 6.3.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

data_a = [1, 2, 3, 4, 5, 6]
data_b = [1, 5, 7, 8, 9]

a_not_b = []
b_not_a = []

for num in data_a:
    if num not in data_b:
        a_not_b.append(num)
        
for num in data_b:
    if num not in data_a:
        b_not_a.append(num)

print a_not_b
print b_not_a
