import itertools
for i in itertools.count(1,3):#从1开始3为步数
    print(i)
    if i>=10:break

x= 0
for i in itertools.cycle(['a','b']):
    print(i)
    x+=1
    if x>=6:break
for i in itertools.repeat('a',3):
     print(i)

print(list(itertools.repeat(3,3)))
print(list(itertools.chain([1,3],[2,3])))
print(list(itertools.compress([1,2,3,4,5],[1,[],True,False,4])))
print(list(itertools.dropwhile(lambda  x:x>6,[8.9,1,2,8,9])))#结果为假后的序列后的值
print(list(itertools.takewhile(lambda  x:x>10,[18,19,1,21,8,9,])))#与上相反
print(list(itertools.filterfalse(lambda  x:x>6,[8.9,1,2,8,9])))#处理为假的元素


for its  in itertools.tee([0,1],2):
    for it in its:
       print(it)
print(list(itertools.product([1,2,3],[1,2],[3])))#排列出所有排列
#print(list(itertools.product('abc','abc','abc'))
print(list(itertools.permutations([1,2,3],2)))
print(list(itertools.permutations('abc',2)))
print(list(itertools.combinations('abc',2)))