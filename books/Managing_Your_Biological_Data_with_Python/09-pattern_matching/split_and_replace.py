'''

Split text and replace separators with a pattern.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 9.3.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

import re

separator = re.compile('\|')

# split
annotation = 'ATOM:CA|RES:ALA|CHAIN:B|NUMRES:166'
columns = separator.split(annotation)
print columns

# replace
new_annotation = separator.sub('@', annotation)
print new_annotation

new_annotation2 = separator.sub('@', annotation, 2)
print new_annotation2
