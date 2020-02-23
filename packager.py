import json,os,subprocess,shutil

#Setting Up Colored ANSI Warnings
TYELLOW='\033[33m'
TGREEN='\033[32m'
TRED='\033[31m'
ENDC = '\033[m' # reset to the defaults

with open('dependencies.json') as f:
  data = json.load(f)
try:
    cwd = str(os.getcwd())
    os.system('rm -R '+cwd+'/package_elem')
    os.system('curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"')
    os.system('python3 get-pip.py --user')
    for elem in data['packages']:
        runt='pip install --target '+cwd+'/package_elem '+elem
        subprocess.check_call(runt,shell=True)
    value = data.get('scripts')
    if value:
        print("\n************************************\\n")
        print("\nLambda Scripts found: Copying to package_elem")
        dest=cwd+"/package_elem"
        for elem in value:
            shutil.copy2(elem,dest)
        print("\n************************************\\n")
    else:
        print('\n'+TYELLOW+'WARNING: No Lambda Handler Found.\nNOTE: Please add Lambda Hander files to the Zip'+ENDC)
        print('\n'+TYELLOW+'Proceeding to Zip only Dependencies...'+ENDC)
    print("\n************************************\n")
    print("ZIPPING STARTS.....")
    os.system('rm '+cwd+'/function.zip')
    shutil.make_archive(cwd+'/function', 'zip', cwd+'/package_elem')
    print("\n"+TGREEN+"Zip File Created at the location "+cwd+"/function.zip"+ENDC)
    print("\n************************************\n")
except OSError as e:
    print(TRED+'ERROR: '+str(e)+ENDC)
except Exception as err:
    print(TRED+'ERROR: '+str(err)+ENDC)    
print("Cleaning up...")
os.system('rm -R '+cwd+'/package_elem')
print("\n~End of Script~")