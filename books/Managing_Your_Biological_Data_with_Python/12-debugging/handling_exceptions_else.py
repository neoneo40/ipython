'''

Catching errors with try.. except.. else

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 12.3.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

try:
    filename = raw_input("Insert a filename:")
    in_file = open(filename)
except IOError:
    print "The filename %s has not been found." % filename
    raise SystemExit
else:
    for line in in_file:
        print line
        in_file.close()
