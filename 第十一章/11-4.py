import os
perfix  = 'Python'
length = 2
base = 1
format = 'mdb'



def PadLeft(str,num,padstr):
    stringlength = len(str)
    n = num - stringlength
    if n>=0:
        str = padstr*n+str
    return str

print('the files in %s will be renamed'%os.getcwd())
all_files = os.listdir(os.getcwd())
print([f for f in all_files if os.path.isfile(f)])
input = input('press y to continue\n')
if input.lower()!='y':
    exit()
filenames = os.listdir(os.curdir)

i = base -1
for filename in filenames:
    i = i+1

    if filename !="rename.py" and os.path.isfile(filename):
        name = str(i)
        name = PadLeft(name ,length,'0')
        t = filename.split('.')
        m = len(t)
        if format =='':
            os.rename(filename,perfix+name+'.'+t[m-1])
        else:
            if t[m-1]== format:
                os.rename(filename,perfix+name+'.'+t[m-1])
            else:i = i-1
    else:
        i= i-1
all_files = os.listdir(os.getcwd())
print([f for f in all_files if os.path.isfile(f)])