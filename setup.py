
import os
os.system('/bin/bash --rcfile act.sh')


#Getting username and dir path:
user = os.path.expanduser('~')
path = os.getcwd()
print(path)
'''
#Building App:
os.system('pyinstaller --onefile -w aaP.py')

#Adding App to path
file = open(f'{user}/.bashrc','a+')
file.write('\n#Adding path for aminoacidProfiler:')
file.write(f'\nexport PATH="{path}/dist/:$PATH"')
file.close()
#os.system(f'open {user}/.bashrc')'''




