import zipfile
zFile = zipfile.ZipFile('ch01/evil.zip')
dictionary = 'ch01/dictionary.txt'
passFile = open(dictionary)
for line in passFile:
    password = line.strip('\n')
    try:
        zFile.extractall(pwd=password)
        print '[+] Password = ' + password + '\n'
        exit(0)
    except Exception, e:
        # no operation
        pass