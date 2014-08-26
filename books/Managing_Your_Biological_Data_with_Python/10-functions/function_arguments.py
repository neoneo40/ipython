'''

Functions with and without return values.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 10.3.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

def increment(number):
    '''returns the given number plus one'''
    return number + 1
 
def print_arg(number):
    '''prints the argument'''
    print number

print_arg(increment(5))
