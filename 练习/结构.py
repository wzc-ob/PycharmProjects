# coord = 0
# increment = 1
# limit = 99
# while(True):
#  coord = coord + increment if coord<limit else 0
#  print(coord)

# while True:
#     command = input('Enter a command[rwq]:')
#     if 'q' in command.lower():break
#     if command.lower()=='r':
#         print('r')
#     elif command.lower()=='w':
#         print('w')
#     else:
#         print('Invalid command, Try again')

#所有迭代执行完毕后，else代码块就会被执行，如果使用break
#或者return推出循环，它就不会被执行
# for i in range(5):
#     print(i)
#     if i == 3:
#         break
# else:
#     print(i)


# for number ,line in enumerate(open('1.txt')):
#     print(number,'\t',line,end=''

#上下文管理器
# with open('1.txt','r') as f:
#     for line in f.readlines():
#         print(line,end='')

# with open('1.txt','w') as tmp:
#     # print('HELLO','WORLD',end='END',sep='-',file=tmp)
#     tmp.writelines(['sadfasgsadgsag\n','adgasdgsa','asdghsag'])

