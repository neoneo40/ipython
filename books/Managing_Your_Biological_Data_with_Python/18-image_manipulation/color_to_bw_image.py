'''

Converts a color to a black/white image.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 18.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from PIL import Image

image = Image.open('color.png', 'r')
bw_image = Image.new('LA', image.size, (255, 255))
bw_image.paste(image, (0, 0))
bw_image.save('black_white.png')
