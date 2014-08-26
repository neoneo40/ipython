'''

Draw a simple line plot.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 16.3.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

from pylab import figure, plot, savefig

xdata = [1, 2, 3, 4]
ydata = [1.25, 2.5, 5.0, 10.0]
    
figure()
plot(xdata, ydata)
savefig('figure1.png')
