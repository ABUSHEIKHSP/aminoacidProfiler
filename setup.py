
import os, subprocess

#Getting username and dir path:
user = os.path.expanduser('~')
path = os.getcwd()
print(path)

#Checking for pip:
try:
    subprocess.run('pip3 install -r requirements.txt', check = True)
except subprocess.CalledProcessError:
    subprocess.run('python3 get-pip.py --isolated', check = True)
    
'''    
#Installing necessary requiremnts:
try:
    os.system(f'pip3 install -r {path}/requirements.txt')
except:
    os.system(f'pip install -r {path}/requirements.txt')'''


 
#Building App:
os.system('pyinstaller --onefile -w aaP.py')


#Adding App to path
file = open(f'{user}/.bashrc','a+')
file.write('\n#Adding path for aminoacidProfiler:')
file.write(f'\nexport PATH="{path}/dist/:$PATH"')
file.close()
#os.system(f'open {user}/.bashrc')