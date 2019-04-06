# coding:utf-8 -*-
#
class BTree:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

    def insertLeft(self, value):
        self.left = BTree(value)
        return self.left

    def insertRight(self, value):
        self.right = BTree(value)
        return self.right

    def show(self):
        print(self.data)
def preirder(node):            #前序遍历
    if node.data:
        node.show()
        if node.left:
            preirder(node.left)
        if node.right:
            preirder(node.right)
def inorder(node):             #中序遍历
    if node.data:
        if node.left:
            inorder(node.left)
        node.show()
        if node.right:
            inorder(node.right)
def postorder(node):             #后序遍历
    if node.data:
        if node.left:
            postorder(node.left)
        if node.right:
            postorder(node.right)
        node.show()

if __name__ == '__main__':
    Root = BTree('Root')
    A = Root.insertLeft('A')
    C = A.insertLeft('C')
    D = A.insertRight('D')
    F = D.insertLeft('F')
    G = D.insertRight('G')
    B = Root.insertRight('B')
    E = B.insertRight('E')
    print('***********************')
    print('Binary Tree Pre-Travresal')
    print('***********************')
    preirder(Root)
    print('***********************')
    print('Binary Tree In-Travresal')
    print('***********************')
    inorder(Root)
    print('***********************')
    print('Binary Tree Post-Travresal')
    print('***********************')
    postorder(Root)