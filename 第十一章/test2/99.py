for a in range(1,10):
    for b in range(a,10):
        print('%d*%d=%2d'%(a,b,a*b),end="  ")

    print()

for a in range(1,10):
    for c in range(1, a):
        print(end="        ")
    for b in range(a,10):
        print('%d*%d=%2d'%(a,b,a*b),end="  ")
    print()
for a in range(1,10):
    for b in range(1,a+1):
        print('%d*%d=%2d' % (a, b, a * b), end="  ")
    print()

for a in range(1,10):
    for c in range(1,10-a):
        print(end="        ")
    for b in range(1,a+1):
        print('%d*%d=%2d' % (a, b, a * b), end="  ")
    print()
