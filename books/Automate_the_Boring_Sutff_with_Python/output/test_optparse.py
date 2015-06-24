import optparse

def main():
    parser = optparse.OptionParser('usage%prog ' + \
                                   '-f <zipfile> \
                                   -d <dictionary>')

    parser.add_option('-f', dest='zname', type='string', \
                      help='specify zip file')
    parser.add_option('-d', dest='dname', type='int', \
                      help='specify dictionary file')

    (options, args) = parser.parse_args()

    if(options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    print options
    print type(options.dname)
    
if __name__ == '__main__':
    main()