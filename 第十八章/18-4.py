# coding:utf-8 -*-
#
class BTree:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None
    def insertLeft(self,value):
        self.left = BTree(value)
        return self.left
    def insertRight(self,value):
        self.right = BTree(value)
        return self.right
    def show(self):
        print(self.data)
if __name__ == '__main__':
    Root = BTree('Root')
    A = Root.insertLeft('A')
    C = A.insertLeft('C')
    D = A.insertRight('D')
    F = D.insertLeft('F')
    G = D.insertRight('G')
    B = Root.insertRight('B')
    E = B.insertRight('E')
    Root.show()
    Root.left.show()
    Root.right.show()
    A = Root.left
    A.left.show()
    Root.left.right.show()
    A.right.left.show()
