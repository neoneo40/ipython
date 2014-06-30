
import zipfile
from threading import Thread
from multiprocessing import Process, Queue

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
#         print '[+] Password = ' + password + '\n'
    except:
        pass
    
def main_original():
    zFile = zipfile.ZipFile('tmp/evil.zip')
    passFile = open('tmp/dictionary.txt')
    for line in passFile:
        password = line.strip('\n')
        extractFile(zFile, password)
        break
    