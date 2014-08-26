# 
# Displays spheres with translucent surface.
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

@prepare_1aay.pml

create zinc2, zinc
set sphere_transparency, 0.4, zinc2
set sphere_scale, 1.05, zinc2

set_view (\
    -0.196709424,   -0.775805354,   -0.599525988,\
    -0.517328799,    0.601554155,   -0.608689904,\
     0.832872272,    0.190417051,   -0.519677818,\
    -0.000003666,    0.000000536,  -40.010795593,\
    16.621603012,    6.123902798,   45.122585297,\
    19.480079651,   60.541667938,    0.000000000 )
ray
