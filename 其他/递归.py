def fun(a):
    if a<0:
            print('xuowu')
    elif a==1 or a ==0:
        b =1
    else:
        b = a * fun(a - 1)
    return b
if __name__ == '__main__':
    a = int(input())
    print(fun(a))


