fileObj = open('hello.txt', 'w')
fileObj.write('Hello world!')
fileObj.close()

import subprocess
import platform

plat = platform.system()

if plat == 'Darwin':
    subprocess.Popen(['open', 'hello.txt'])
elif plat == 'Linux':
    subprocess.Popen(['open', 'hello.txt'])
elif plat == 'Windows':
    subprocess.Popen(['start', 'hello.txt'])