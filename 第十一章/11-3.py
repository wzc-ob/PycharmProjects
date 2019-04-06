import os
filenames = []
for a,b,files in os.walk('test2'):
    if files:
        filenames.append([file[:-4] for file in files])
fname = 'testexam'
i = 0
for files in filenames:
    f = open(fname+str(0)+'.xls','w')
    for name in files:
        f.write(name[-9:]+'\t'+name[:-9]+'\n')
    f.close()
    i+=1
print('成功生成')