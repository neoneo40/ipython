import zipfile

zFile = zipfile.ZipFile('ch01/evil.zip', 'r')
try:
    zFile.extractall(path='tmp', pwd='orange')
except Exception, e:
    print e