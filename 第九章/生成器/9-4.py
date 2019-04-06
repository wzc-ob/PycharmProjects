def myYield(n):
    while n>0:
        rcv = yield n
        n-=1
        if rcv is not None:
            n = rcv
if __name__ == '__main__':
    my_yield  = myYield(3)
    print(my_yield.__next__())
    print(my_yield.__next__())
    print('传给生成器一个值，重新初始化生成器：')
    print(my_yield.send(10))
    print(my_yield.__next__())

