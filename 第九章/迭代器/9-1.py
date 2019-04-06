class Myterator:
    def __init__(self,x=2,xmax=100):
        self.__mul,self.__x = x,x
        self.__xmax=xmax
        print(self.__mul,self.__x,x)
        print(self.__xmax)
    def __iter__(self):
        return  self
    def __next__(self):
        if self.__x and self.__x!=1:
           self.__mul*= self.__x
           if self.__mul <=self.__xmax:
                return self.__mul
           else:
                raise StopIteration
        else:
            raise StopIteration
if __name__ == '__main__':
 myiter = Myterator()
 for i in myiter:

     print('迭代数据元素为：',i)
