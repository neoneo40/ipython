import pyPdf
import optparse
from pyPdf import PdfFileReader

def printMeta(fileName):
    pdfFile = PdfFileReader( file(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print '[*] PDF MetaData For: ' + str(fileName)
    for metaItem, value in docInfo.items():
        print '[+] ' + metaItem + ':' + value
        
def main():
    parser = optparse.OptionParser('usage %prog ' + '-F <PDF file name>')
    parser.add_option('-F', dest='fileName', type='string', 
                      help = 'specify PDF file name')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print parser.usage
    else:
        printMeta(fileName)

if __name__ == '__main__':
    main()