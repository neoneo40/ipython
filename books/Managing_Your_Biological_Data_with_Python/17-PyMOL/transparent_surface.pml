# 
# Display a transparent protein surface.
# 
# To be run as a PyMOL script using the '@script.pml' command 
# or the File --> Run menu command.
# 
# -----------------------------------------------------------
# (c) 2013 Allegra Via and Kristian Rother
#     Licensed under the conditions of the Python License
# 
#     This code appears in section 17.4.2 of the book
#     "Managing Biological Data with Python".
# -----------------------------------------------------------

delete *

load 1aay.pdb, zf_surface
load 1aay.pdb, zf_cartoon

hide all
show cartoon, zf_cartoon
show surface, zf_surface
set transparency, 0.5