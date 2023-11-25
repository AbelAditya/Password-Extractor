import subprocess
import os

p1 = subprocess.run('netsh wlan show profiles', shell=True, capture_output=True, text=True)
a1 = p1.stdout

x1 = a1.find('All')
l = a1[x1:].split('All User Profile     : ')
path = os.getcwd()
f = open(f'{path}\\pwd.txt', 'w')
for i in range(1,len(l)):
    p = subprocess.run(f'netsh wlan show profile name="{l[i].strip()}" key=clear', shell=True, capture_output=True, text=True)
    a = p.stdout
    z = a.find('Key Content')
    z1 = a.find('Cost')
    f.write(f'{l[i].strip()} : {a[z+24:z1]}')

f.flush()
f.close()
