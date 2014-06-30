import zipfile
import optparse
from threading import Thread
from multiprocessing import Process, Queue

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Found password ' + password + '\n'
    except:
        pass
    
def main():
    parser = optparse.OptionParser('usage%prog ' + \
                                   '-f <zipfile> \
                                   -d <dictionary>')

    parser.add_option('-f', dest='zname', type='string', \
                      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', \
                      help='specify dictionary file')

    (options, args) = parser.parse_args()

    if(options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    
    passQueue = Queue()
    
    for line in passFile:
        passQueue.put(line.strip('\n'))
        
    pr1 = Process(target=extractFile, args=(zFile, passQueue.get()))
    pr2 = Process(target=extractFile, args=(zFile, passQueue.get()))
    pr1.start()
    pr2.start()
    pr1.join()
    pr2.join()
    
if __name__ == '__main__':
    main()