
import os, subprocess

try:
    subprocess.run('sudo killall apt')
    subprocess.run('chmod 744 bash_setup.sh','chmod 744 bash_setup.sh' )
except:
    pass

#Getting username and dir path:
user = os.path.expanduser('~')
path = os.getcwd()
print(path)

#Installing necessary requiremnts:

os.system(f'pip3 install -r {path}/requirements.txt')

 
#Building App:
os.system('pyinstaller --onefile -w aaP.py')


#Adding App to path
file = open(f'{user}/.bashrc','a+')
file.write('\n#Adding path for aminoacidProfiler:')
file.write(f'\nexport PATH="{path}/dist/:$PATH"')
file.close()
#os.system(f'open {user}/.bashrc')