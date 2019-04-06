# -*- coding:utf-8 -*-
#
import re
import sys
def DealWithFunc(s):
    r = re.compile(r''
                   r'(?<=def\s)'
                   '\w+'
                   '\(.*?\)'
                   '(?=:)'
                   '',re.X|re.U)
    return r.findall(s)
def DealWithVar(s):
    vars  = []
    r = re.compile(r'\b\w+(?=\s=)',re.X|re.U)
    vars.extend(r.findall(s))
    r = re.compile(r'(?<=for\s)\w\s(?=in)',re.X|re.U)
    vars.extend(r.findall(s))
    return vars
if len(sys.argv) ==1:
    sour = input('请输入要处理的文件路径')
else:
    sour = sys.argv[1]
file = open(sour,encoding='utf-8')
s = file.readlines()
file.close()
print('***************************')
print(sour,'中的函数有:')
print('***************************')
i  = 0
for line in s:
    i = i+1
    function = DealWithFunc(line)
    if len(function) ==1:
        print('Line:',i,function[0])
print('****************************')
print(sour,'中的变量有：')
print('****************************')
i =0
for line in s:
    i = i+2
    var = DealWithVar(line)
    if len(var) ==1:
        print('Line:',i,'\t',var[0])
