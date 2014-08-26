'''

Functions can take a variable number of parameters.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 10.4.2 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

def convert_to_string(*args):
    '''returns all arguments as a single tab-separated string'''
    result = [str(a) for a in args]
    return '\t'.join(result) + '\n'


output_file = open("nucleotideSubstitMatrix.txt", "w")
output_file.write(convert_to_string('', 'A', 'T', 'C', 'G'))
output_file.write(convert_to_string('A', 1.0))
output_file.write(convert_to_string('T', 0.5, 1.0))
output_file.write(convert_to_string('C', 0.1, 0.1, 1.0))
output_file.write(convert_to_string('G', 0.1, 0.1, 0.5, 1.0))
output_file.close()
