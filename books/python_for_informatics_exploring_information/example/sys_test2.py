import sys
name = sys.argv[1]
handle = open(name, 'r')
text = handle.read()
# print name, 'is', len(text), 'bytes'
print '{name}, is {len_text} bytes'.format(name=name, len_text=len(text))