import sys
print 'Count:', len(sys.argv)
print 'Type:', type(sys.argv)
for i, arg in enumerate(sys.argv):
    print 'Argument:', i,  arg