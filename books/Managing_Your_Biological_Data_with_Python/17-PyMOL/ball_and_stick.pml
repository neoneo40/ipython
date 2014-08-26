# 
# Display residues as ball-and-stick.
# 
# To be run as a PyMOL script using the '@script.pml' command 
# or the File --> Run menu command.
# 
# -----------------------------------------------------------
# (c) 2013 Allegra Via and Kristian Rother
#     Licensed under the conditions of the Python License
# 
#     This code appears in section 17.4.1 of the book
#     "Managing Biological Data with Python".
# -----------------------------------------------------------

@prepare_1aay.pml

show sticks, pocket
show spheres, pocket
set stick_radius, 0.1, pocket
set sphere_scale, 0.25, pocket 
color marine, pocket

indicate none

