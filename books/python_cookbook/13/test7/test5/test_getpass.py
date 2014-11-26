
import getpass

# user = getpass.getuser()
user = input('Enter your username: ')
print(user)
passwd = getpass.getpass()
print(passwd)

def svc_login(user, passwd):
    if user == 'user' and passwd == 'passwd':
        return True
    return False

if svc_login(user, passwd):
    print('Yay!')
else:
    print('Boo!')