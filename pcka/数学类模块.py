import random
print(random.random())
print(random.randint(0,10))#随机整数
print(random.choice((1,2,3,4)))#从元组中随机返回一个值
alst = [1,2,3,4,5]
random.shuffle([1,2,3,4,5])#随机乱序
print(alst)