import json
import os
import subprocess
import shutil

#Setting Up Colored ANSI Warnings
TYELLOW = '\033[33m'
TGREEN = '\033[32m'
TRED = '\033[31m'
ENDC = '\033[m' # reset to the defaults

with open('dependencies.json') as f:
    data = json.load(f)
try:
    CWD = str(os.getcwd())
    os.system('rm -R '+CWD+'/package_elem')
    os.system('curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"')
    os.system('python3 get-pip.py --user')
    for elem in data['packages']:
        runt = 'pip install --target '+CWD+'/package_elem '+elem
        subprocess.check_call(runt, shell=True)
    value = data.get('scripts')
    if value:
        print("\n************************************\\n")
        print("\nLambda Scripts found: Copying to package_elem")
        dest = CWD+"/package_elem"
        for elem in value:
            shutil.copy2(elem, dest)
        print("\n************************************\\n")
    else:
        print('\n'+TYELLOW+'WARNING: No Lambda Handler Found.'+ENDC)
        print('\n'+TYELLOW+'NOTE: Please add Lambda Hander files to the Zip'+ENDC)
        print('\n'+TYELLOW+'Proceeding to Zip only Dependencies...'+ENDC)
    print("\n************************************\n")
    print("ZIPPING STARTS.....")
    os.system('rm '+CWD+'/function.zip')
    shutil.make_archive(CWD+'/function', 'zip', CWD+'/package_elem')
    print("\n"+TGREEN+"Zip File Created at the location "+CWD+"/function.zip"+ENDC)
    print("\n************************************\n")
except OSError as ErR:
    print(TRED+'ERROR: '+str(ErR)+ENDC)
except Exception as ErroR:
    print(TRED+'ERROR: '+str(ErroR)+ENDC)
print("Cleaning up...")
os.system('rm -R '+CWD+'/package_elem')
print("\n~End of Script~")
