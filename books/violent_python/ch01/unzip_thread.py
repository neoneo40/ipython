import zipfile
from threading import Thread

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Password = ' + password + '\n'
    except:
        pass
    
def main():
    zFile = zipfile.ZipFile('ch01/evil.zip')
    passFile = open('ch01/dictionary.txt')
    for line in passFile:
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
        
if __name__ == '__main__':
    main()