import subprocess
processes = []
psum = 5
for i in range(psum):
    processes.append(subprocess.Popen(['python','protest9.py'],stdout = subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess,universal_newlines=True,shell=True))
processes[0].communicate(' 0 bouquet of flowers!')
for before,after in zip(processes[:psum],processes[1:]):
    after.communicate(before.communicate()[0])
print('\nSum of Processes :%d'%psum)
print()
for item in processes:
    print(item.communicate()[0])
