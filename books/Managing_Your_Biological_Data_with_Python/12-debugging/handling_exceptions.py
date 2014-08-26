'''

Catching errors with try.. except

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 12.3.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

try:
    a = float(raw_input("Insert a number:"))
    print a
except ValueError:
    print "You haven't inserted a number. Please retry."
    raise SystemExit
