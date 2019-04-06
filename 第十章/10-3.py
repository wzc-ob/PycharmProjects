def dalay_fun(x,y):
    def caculator():
        return  x+y
    return caculator
if __name__ == '__main__':
    print('返回一个求和的函数，并不求和。')
    msum  = dalay_fun(3,4) #调用外层函数，并不计算，实际返回一个函数对象
    print()
    print('调用并求和：')
    print(msum())  #实际求值得调用