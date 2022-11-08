
import os

#Getting username and dir path:
user = os.path.expanduser('~')
path = os.getcwd()

#Installing necessary requiremnts:
try:
    os.sysconf(f'pip install -r {path}/requirements.txt')
except:
    os.sysconf(f'pip3 install -r {path}/requirements.txt')
 
#Building App:
os.system('pyinstaller --onefile -w aaP.py')

#Adding App to path
file = open(f'{user}/.bashrc','a+')
file.write('\n#Adding path for aminoacidProfiler:')
file.write(f'\nexport PATH="{path}/dist/:$PATH"')
file.close()
#os.system(f'open {user}/.bashrc')