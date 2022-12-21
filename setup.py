#!pyenv/bin/python3
#!/pyenv/bin/pip3

import os

os.system('pip3 install -r requirements.txt ')

#Getting username and dir path:
user = os.path.expanduser('~')
path = os.getcwd()
print(path)

#Building App:
os.system('pyinstaller --onefile -w aaP.py')

#Adding App to path
file = open(f'{user}/.bashrc','a+')
file.write('\n#Adding path for aminoacidProfiler:')
file.write(f'\nexport PATH="{path}/dist/:$PATH"')
file.close()
#os.system(f'open {user}/.bashrc')'''




