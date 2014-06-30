import crypt
import hashlib

def testPass(cryptPass):
    salt=cryptPass.split('$')[2]
    print '[i] salt = ' + salt
    myPass=cryptPass.split('$')[3]
    print 'myPass ', myPass
    dictFile = open('ch01/dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, '$6$' + salt + '$')
        print cryptWord
        cryptWord = cryptWord.split('$')[3]
        if cryptWord==myPass:
            print '[+] Found password: ' + word + '\n'
            return
        print '[-] Password not found.\n'
        return

def main():
    passwords = 'ch01/shadow.txt'
    passFile = open(passwords)
    for line in passFile:
        # ':' 이 있을 때만
        if ':' in line:
            # :의 앞부분은 user: victim, root
            user = line.split(':')[0]
            # : 뒤의 부분이 HX~
            cryptPass = line.split(':')[1].strip(' ')
            print '[*] Cracking Password For: ' + user
            # : 뒤의 부분을 testPass에 넘겨줌. 우리가 풀어야 할 암호문
            testPass(cryptPass)

            
if __name__ == '__main__':
    main()