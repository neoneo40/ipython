import zipfile

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        return password
    except:
        return
    
def main():
    zFile = zipfile.ZipFile('ch01/evil.zip')
    passFile = open('ch01/dictionary.txt')
    for line in passFile:
        password = line.strip('\n')
        guess = extractFile(zFile, password)
        if guess:
            print '[+] Password = ' + password + '\n'
            exit(0)
            
if __name__ == '__main__':
    main()