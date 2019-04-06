import fileinput
def demo_fileinput():
    with fileinput.input(['fpa.txt','fpb.txt']) as lines:
        for line in lines:
            print('总第%d行，'%fileinput.lineno(),'文件%s中第%d行'%(fileinput.filename(),fileinput.filelineno()))
            print(line.strip())
if __name__ == '__main__':
            demo_fileinput()
import os
print(os.getcwd())#获取当前目录
print(os.listdir())#当前目录的内容
#os.mkdir('test2')#创建目录
#os.rmdir('test2')#删除目录
print(os.path.isdir('fpa.txt'))#判断路径是否为目录
print(os.path.isdir('test2'))
print(os.path.isfile('fpa.txt'))#判断某一路径是否为文件
for i in os.walk('.\\'):
    print(i)