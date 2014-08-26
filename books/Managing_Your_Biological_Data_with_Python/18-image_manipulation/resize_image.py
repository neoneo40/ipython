'''
Resizes a big image to a small one.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 18.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

import Image

image = Image.open('big.png')
small = image.resize((100, 100))
small.save('small.png')
