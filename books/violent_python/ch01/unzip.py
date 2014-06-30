import zipfile

zFile = zipfile.ZipFile('ch01/evil.zip', 'r')
zFile.extractall(path='tmp', pwd='secret')