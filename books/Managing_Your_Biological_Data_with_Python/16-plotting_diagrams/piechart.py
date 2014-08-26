'''

Draw a pie chart with protruding slices.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 16.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from pylab import figure, title, pie, savefig

nucleotides = 'G', 'C', 'A', 'U'
count = [1024, 759, 606, 398]
explode = [0.0, 0.0, 0.05, 0.05]

colors = ["#f0f0f0", "#dddddd", "#bbbbbb", "#999999"]

def get_percent(value):
    '''Formats float values in pie slices to percent.'''
    return "%4.1f%%" % (value)

figure(1)
title('nucleotides in 23S RNA from T.thermophilus')

pie(count, explode=explode, labels=nucleotides, shadow=True,
    colors=colors, autopct=get_percent)

savefig('piechart.png', dpi=150)
