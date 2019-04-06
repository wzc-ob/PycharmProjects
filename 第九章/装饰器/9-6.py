def abc(fun):
    def wrapper(*args,**kwargs):
        print('开始运行。。。')
        fun(*args,**kwargs)
        print('运行结束。。')
    return wrapper
@abc
def demo_decoration(x):
    a =[]
    for i in range(x):
        a.append(i)
    print(a)
@abc
def hello(name):
    print('hello',name)
if __name__ == '__main__':
    demo_decoration(5)
    print()
    hello('John')
