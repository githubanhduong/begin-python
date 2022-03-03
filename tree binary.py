# create a new tree binary
from inspect import stack


class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def insert(self, data):
    if self.data is None:
        self.data = data
    else:
        if data < self.data:
            self.left = Node(data)
        else:
            self.left.insert(data)
        if data > self.data:
            self.right = Node(data)
        else:
            self.right.insert(data)


## A function to do Preorder tree traversal
def PreOrder(root):
    if root:
        print(root.data, end=" ")

        PreOrder(root.left)

        PreOrder(root.right)


## A function to do InOrder tree traversal
def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)


## A function to do PostOrder tree traversal
def PostOrder(root):
    if root:
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data, end=" ")


#A function to do search in a tree
def Search(root, key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return Search(root.right, key)
    return Search(root.left, key)
