'''

Draw an image of a plasmid and label it.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 18.3.6 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from PIL import Image, ImageDraw
import math

PLASMID_LENGTH = 4361
SIZE = (500, 500)
CENTER = (250, 250)

pBR322 = Image.new('RGB', SIZE, 'white')
DRAW = ImageDraw.Draw(pBR322)

def get_angle(bp, length=PLASMID_LENGTH):
    """Converts base position into an angle."""
    return bp * 360 / length

def coord(angle, center, radius):
    """Return (x,y) coordinates of a point in a circle."""
    rad = math.radians(90 - angle)
    x = int(center[0] + math.sin(rad) * radius)
    y = int(center[1] + math.cos(rad) * radius)
    return x, y

def draw_arrow_tip(start, direction, color):
    """Draws a triangle at the given start angle."""
    p1 = coord(start + direction, CENTER, 185)
    p2 = coord(start, CENTER, 160)
    p3 = coord(start, CENTER, 210)
    DRAW.polygon((p1, p2, p3), fill=color)


TET_START, TET_END = get_angle(88), get_angle(1276)
AMP_START, AMP_END = get_angle(3293), get_angle(4153)
ORI_START, ORI_END = get_angle(2519), get_angle(3133)

# drawing the plasmid
BOX = (50, 50, 450, 450)
DRAW.pieslice(BOX, 0, 360, fill='gray')
DRAW.pieslice(BOX, TET_START, TET_END, fill='blue')
DRAW.pieslice(BOX, AMP_START, AMP_END, fill='orange')
DRAW.pieslice(BOX, ORI_START, ORI_END, fill='darkmagenta')
DRAW.pieslice((80, 80, 420, 420), 0, 360, fill='white')

draw_arrow_tip(TET_END, 10, 'blue')
draw_arrow_tip(AMP_START, -10, 'orange')
draw_arrow_tip(ORI_START, -10, 'darkmagenta')

DRAW.text((150, 130), "ori", fill=(0, 0, 0))
DRAW.text((340, 130), "amp", fill=(0, 0, 0))
DRAW.text((300, 380), "tet", fill=(0, 0, 0))

pBR322.save('plasmid_pBR322.png')
