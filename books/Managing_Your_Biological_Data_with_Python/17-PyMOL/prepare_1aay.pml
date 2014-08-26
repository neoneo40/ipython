# 
# Prepare zinc finger molecule for other scripts
# (like the zinc finger script but without the time-consuming 'ray')
# 
# You don't need to run this at all.
# 
# -----------------------------------------------------------
# (c) 2013 Allegra Via and Kristian Rother
#     Licensed under the conditions of the Python License
# 
#     This code appears in chapter 17 of the book
#     "Managing Biological Data with Python".
# -----------------------------------------------------------

delete *
load 1aay.pdb

hide everything
bg_color white

# protein
select zinc_finger, chain a
show cartoon, zinc_finger
color blue, zinc_finger

# DNA
select dna, chain b or chain c
select dna_backbone, elem P
show cartoon, dna
set cartoon_ring_mode, 3
color green, dna
color forest, dna_backbone

# zinc
select zinc, resn zn
show spheres, zinc
color gray, zinc

# binding residues
select atoms_pocket, zinc around 5.0 and not zinc
select pocket, byres atoms_pocket
show sticks, pocket
set valence, 1
color marine, pocket

set_view (\
     0.385022461,   -0.910319746,   -0.151902989,\
    -0.748979092,   -0.212032005,   -0.627752066,\
     0.539247334,    0.355471820,   -0.763447404,\
     0.000005471,    0.000029832, -134.466125488,\
     1.499966264,   12.841400146,   50.074134827,\
   100.975906372,  167.958770752,    0.000000000 )
