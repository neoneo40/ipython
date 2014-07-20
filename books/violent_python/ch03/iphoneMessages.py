
import os
import sqlite3
import optparse
from urllib import unquote
import sys
reload(sys)
sys.setdefaultencoding = 'utf-8'

def isMessageTable(iphoneDB):
    try:
        conn = sqlite3.connect(iphoneDB)
        c = conn.cursor()
        c.execute("SELECT tbl_name FROM sqlite_master WHERE type='table';")
        for row in c:
            if 'message' in str(row):
                return True
    except:
        return False

def printMessage(msgDB):
    try:
        conn = sqlite3.connect(msgDB)
        c = conn.cursor()
        c.execute("SELECT datetime(date, 'unixepoch'), text \
        FROM message;")
        for row in c:
            date = str(row[0])
            try:
                text1 = unquote(row[1])
            except Exception, e:
                print e
            # text = unquote(row[1]).decode('utf-8')
            print text1
#             print date, text
#             print '\n[+] Date: ' + date + ', Addr: ' + addr +\
#             ' Message: ' + text
    except Exception, e:
        print e
    
def main():
    parser = optparse.OptionParser("usage %prog " +\
                                   "-p <iPhone Backup Directory>")
    parser.add_option('-p', dest='pathName', type='string', \
                      help='specify iphone backup path')
    (options, args) = parser.parse_args()
    pathName = options.pathName
    if pathName == None:
        print parser.usage
        exit(0)
    elif os.path.isdir(pathName) == False:
        print '[!] Path Does Not Exist: ' + pathName
        exit(0)
    else:
        dirList = os.listdir(pathName)
        for fileName in dirList:
            iphoneDB = os.path.join(pathName, fileName)
            if isMessageTable(iphoneDB):
                try:
                    print '\n[*] --- Found Messages ---'
                    print iphoneDB
                    printMessage(iphoneDB)
                except:
                    pass
            
if __name__ == '__main__':
    main()