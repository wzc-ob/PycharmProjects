import random
##以下定义三个分支函数
def path_a():
    print('路径分支A')
def path_b():
    print('路径分支B')
def path_c():
    print('路径分支C')
if __name__ == '__main__':
    path_dict = {}
    path_dict['a'] = path_a
    path_dict['b'] = path_b
    path_dict['c'] = path_c
    paths = 'abc'
    for i in range(4):
        path = random.choice(paths)
        print('选择了路径：',path)
        path_dict[path]()
