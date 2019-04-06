for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and k!=i:
                print('%d'%(i*100+j*10+k),end=" ")

for i in range(100):
    for j in range(100):
        if i*i-168 == j*j-100:
            print(i*i-168)