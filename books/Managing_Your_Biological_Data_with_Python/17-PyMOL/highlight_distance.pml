# 
# Measure and highlight a distance.
# 
# To be run as a PyMOL script using the '@script.pml' command 
# or the File --> Run menu command.
# 
# -----------------------------------------------------------
# (c) 2013 Allegra Via and Kristian Rother
#     Licensed under the conditions of the Python License
# 
#     This code appears in section 17.4.3 of the book
#     "Managing Biological Data with Python".
# -----------------------------------------------------------

@prepare_1aay.pml

distance dist = (/1aay//C/DA`58/OP2),(/1aay//B/DG`10/OP2)
color black, dist
