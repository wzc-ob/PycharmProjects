import subprocess
print('call() test :',subprocess.call(['Python','protest.py']))
print('')
print('check_call() test:',subprocess.check_call(['Python','protest.py']))
print('')
print('getstatusoutput() test:',subprocess.getstatusoutput(['Python','protest.py']))
print('')
print('getoutput() test :',subprocess.getoutput(['python','protest.py ']))
print('')
print('check_output() test :',subprocess.check_output(['python','protest.py']))

