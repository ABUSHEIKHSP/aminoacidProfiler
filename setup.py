#!/usr/bin/python3

import os

os.system('pip3 install tk')
os.system('pip3 install pytz')
os.system('pip3 install pyinstaller')
os.system('sudo apt install git')
os.system('pyinstaller --onefile -w aaP.py')

user = os.path.expanduser('~')
print(user)
path = os.getcwd()
print(path)


file = open(f'{user}/.bashrc','a+')
file.write('\n#Adding path for aminoacidProfiler:')
file.write(f'\nexport PATH="{path}/dist/:$PATH"')
file.close()

os.system(f'open {user}/.bashrc')