# -*- coding:utf-8 -*-
#
def BinarySearch(l,key):
    low = 0
    high = len(l)-1
    i = 0
    while(low<=high):
        i = i+1
        mid = (high+low)//2
        if (l[mid]<key):
            low = mid+1
        elif(l[mid]>key):
            high = mid-1
        else:
            print('use %d time(s)'%i)
            return mid
    return '无该搜索结果'
if __name__ == '__main__':
    l = [1,5,6,9,10,51,62,65,70]
    print(BinarySearch(l,2))
    print(BinarySearch(l,10))
    print(BinarySearch(l,65))
    print(BinarySearch(l,70))