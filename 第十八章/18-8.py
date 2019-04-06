# -*- coding:utf-8 -*-
#
class BTree():
    def __init__(self,value):
        self.left = None
        self.data  = value
        self.right = None
    def insertLeft(self,value):
        self.left = BTree(value)
        return self.left
    def insertRight(self,value):
        self.right = BTree(value)
        return self.right
    def show(self):
        print(self.data)
def inorder(node):
    if node.data:
        if node.left:
            inorder(node.left)
        node.show()
        if node.right:
            inorder(node.right)
def rinorder(node):
    if node.data:
        if node.right:
            rinorder(node.right)
        node.show()
        if node.left:
            rinorder(node.left)

def insert(node,value):
    if value > node.data:
        if node.right:
            insert(node.right,value)
        else:
            node.insertRight(value)
    else:
        if node.left:
            insert(node.left,value)
        else:
            node.insertLeft(value)
if __name__ == '__main__':
    a = [3,5,7,20,43,2,15,30]
    Root = BTree(a[0])
    node = Root
    for i in range(1,len(a)):
        insert(Root,a[i])
    print('****************************')
    print('           从小到大')
    print('****************************')
    inorder(Root)
    print('****************************')
    print('           从大到小')
    print('****************************')
    rinorder(Root)


