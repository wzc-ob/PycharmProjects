def abc(myclass):
    class InnerClass:
        def __init__(self,z=0):
            self.z  = 0
            self.wrapper = myclass()
        def position(self):
            self.wrapper.position()
            print('z axis:',self.z)
    return InnerClass

@abc
class coordination:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def position(self):
        print('x axis:',self.x)
        print('y axis:',self.y)

if __name__ == '__main__':
    coor = coordination()
    coor.position()