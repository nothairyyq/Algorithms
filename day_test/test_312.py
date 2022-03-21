from logging import root
from platform import node


class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def re_insert(self,root,data):
        if root.data == data:
            return False
        if data<root.data:
            if root.left:
                return self.re_insert(root.left,data)
            else:
                root.left =Node(data)
                return True
        else:
            if root.right:
                return self.re_insert(root.right,data)
            else:
                root.right = Node(data)
                return True

    def insert(self,data):
        if self.root:
            return self.re_insert(root,data)
        else:
            self.root = Node(data)
            return True