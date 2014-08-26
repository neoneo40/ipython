'''

Paste a small image into a big one.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 18.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from PIL import Image

image = Image.open('color.png', 'r')
label = Image.open('label.png', 'r')
image.paste(label, (40, 460))
image.save('combined.png')
