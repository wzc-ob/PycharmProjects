from foo import foo_fun
name = 'Current module'
def bar():
    print('当前模块中的函数bar：')
    print('变量name：',name)
def call__foo_fun(fun):#定义调用传入函数作为参数的函数
    fun()              #调用传入的函数
if __name__ == '__main__':
    bar()
    print()
    foo_fun()
    print()
    call__foo_fun(foo_fun)