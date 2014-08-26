'''

Convert symbols in a prosite pattern to a regular expression.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 9.4.1 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

pattern = '[DEQN]-x-[DEQN](2)-C-x(3,14)-C-x(3,7)-C-x-[DN]-x(4)-[FY]-x-C'
pattern = pattern.replace('{', '[^')
pattern = pattern.replace('}', ']')
pattern = pattern.replace('(', '{')
pattern = pattern.replace(')', '}')
pattern = pattern.replace('-', '')
pattern = pattern.replace('x', '.')
pattern = pattern.replace('>', '$')
pattern = pattern.replace('<', '^')
print pattern
