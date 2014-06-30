import zipfile
from threading import Thread
from multiprocessing import Process, Queue

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Password = ' + password + '\n'
    except:
        pass
    
def main_multi2():
    zFile = zipfile.ZipFile('tmp/evil.zip')
    passFile = open('tmp/dictionary.txt')
    
    result = Queue()
    for line in passFile:
        result.put(line.strip('\n'))
    
    pr1 = Process(target=extractFile, args=(zFile, result.get()))
    pr2 = Process(target=extractFile, args=(zFile, result.get()))
    pr1.start()
    pr2.start()
    pr1.join()
    pr2.join()