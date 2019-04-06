import subprocess
prcs = subprocess.Popen(['python','protest.py'],stdout = subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,shell=True)
prcs.communicate('These string are from stdin')
print('subprocess pid:',prcs.pid)
print('\nSTDOUT:')
print(str(prcs.communicate()[0]))
print('STDERR')
print(prcs.communicate()[1])