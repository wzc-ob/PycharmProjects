# class A(object):
#     def __init__(self,a,b):
#         self._a = a
#         self._b = b
#     def __call__(self,num):
#         print('call',num + self._a)
#     def myprint(self):
#         print('a = ',self._a,'b = ',self._b)
# a1 = A(10,20)
# a1.myprint()
# a1(80)

# class B():
#     def fn(self):
#         print('B fn')
#     def __init__(self):
#         print('B init')
# class A():
#     def fn(self):
#         print('A fn')
#     def __new__(cls,a):
#         print('NEW',a)
#         if a>10:
#             return   super(A,cls).__new__(cls)
#         return B()
#     def __init__(self,a):
#         print("init",a)
# a1 = A(5)
# a1.fn()
# a2 = A(20)
# a2.fn()


# class Base(object):
#     def __init__(self):
#         print("enter Base")
#         print("leave Base")
# class A(Base):
#     def __init__(self):
#         print("enter A")
#         super(A, self).__init__()
#         print("leave A")
# class B(Base):
#     def __init__(self):
#         print("enter B")
#         super(B, self).__init__()
#         print("leave B")
# class C(A, B):
#     def __init__(self):
#         print("enter C")
#         super(C, self).__init__()
#         print("leave C")
# c = C()

# num = 9
# def f1():
#     num = 20
# def f2():
#     print(num)
# f2()
# f1()
# f2()
#a,b,c 代表新郎 ，x,y,z代表新娘
list = ['x','y','z']
x =1
y =2
z =3
for a in range(1,4):
    for b in range(1,4):
       for c in range(1,4):
           if a!=1 and c!=1 and c!=3 and a!=b and b!=c and a!=c:
              print('%d%d%d'%(a,b,c))
              print('%s将嫁给a'%list[a-1])
              print('%s将嫁给b'%list[b-1])
              print('%s将嫁给c'%list[c-1])



              #  ywnwvyichcaqigdg