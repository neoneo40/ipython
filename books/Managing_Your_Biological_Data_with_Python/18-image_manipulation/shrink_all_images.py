'''
Diminishes the size of all .png files by half.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 18.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

import Image
import os

for filename in os.listdir('.'):
    if filename.endswith('.png'):
        im = Image.open(filename)
        x = im.size[0] / 2
        y = im.size[1] / 2
        small = im.resize((x, y))
        small.save('small_'+filename)
