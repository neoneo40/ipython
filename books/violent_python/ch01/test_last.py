import zipfile
from threading import Thread
from multiprocessing import Process, Queue

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Password = ' + password + '\n'
    except:
        pass
    
def main_original():
    zFile = zipfile.ZipFile('tmp/evil.zip')
    passFile = open('tmp/dictionary.txt')
    for line in passFile:
        password = line.strip('\n')
        extractFile(zFile, password)
        break
    
def main_thread():
    zFile = zipfile.ZipFile('tmp/evil.zip')
    passFile = open('tmp/dictionary.txt')
    for line in passFile:
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

def main_multi():
    zFile = zipfile.ZipFile('tmp/evil.zip')
    passFile = open('tmp/dictionary.txt')
    
    for line in passFile:
        password = line.strip('\n')
        result = Queue()
        pr1 = Process(target=extractFile, args=(zFile, password))
        pr2 = Process(target=extractFile, args=(zFile, password))
        pr1.start()
        pr2.start()
        pr1.join()
        pr2.join()

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
    
if __name__ == '__main__':
    main_original()