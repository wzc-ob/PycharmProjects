import random
a = random.randint(0,500)
while True:
    while True:
        b = input('请输入一个0-500之间的数字：')
        try:
            b = int(b)
            break
        except ValueError:
            print('I said enter an integer')
    if a == int(b):
        print('猜对了')
        quit()
    elif a > int(b):
        print('你猜的数字小了')
    else:
        print('你猜的数大了')

