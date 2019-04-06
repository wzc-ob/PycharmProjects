# -*- coding:utf-8 -*-
#
from ftplib import FTP
bufsize = 1024
def Get(filename):
    command = 'RETR' + filename
    FTP.retrbinary(command,open(filename,'wb').write,bufsize)
    print('下载成功')
def Put(filenames):
    command = 'RETR' + filenames
    filehandler = open(filenames,'rb')
    FTP.storbinary(command,filehandler,bufsize)
    filehandler.close()
def PWD():
    print(ftp.pwd())
def Size():
    print(ftp.size())
def Help():
    print('''
    ====================================
         Simple Python FTp
    ==================================== 
    cd
    delete
    dir
    get
    help
    mkdir
    put
    pwd
    rename
    rmdir
    size   
    ''')
server = input('请输入FTP服务器地址：')
ftp = FTP(server)
username = input('请输入用户名：')
password = input('请输入密码：')
ftp.login(username,password)
print(ftp.getwelcome())
action = {'dir':ftp.dir,'pwd':PWD,'cd':ftp.cwd,'get':Get,'put':Put,'help':Help,'rmdir':ftp.rmd,'mkdir':ftp.mkd,'delete':ftp.delete,'size':Size,'rename':ftp.rename}
while True:
    print('pyftp>',  )
    cmds = input()
    cmd = str.split(cmds)
    try:
        if len(cmd) ==1:
            if str.lower(cmd[0]) == 'quit':
                break
            else:
                action[str.lower(cmd[0])]()
        elif len(cmd) ==2:
            action[str.lower(cmd[0])]()
        elif len(cmd) ==3:
            action[str.lower(cmd[0])](cmd[1],cmd[2])
        else:
            print('输入错误')
    except:
        print('命令出错')
ftp.quit()