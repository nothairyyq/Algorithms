'''
implement Binary Search Tree
Operation: search O(log(n))
           insert O(log(n))
           maximum O(h) = O(log n)
           minimum O(h) = O(log n)
           successor, predecessor O(h) = O(log n)
           traversal: order,preorder,postorder
           delete: O(h) = O(log n)
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    '''
    Search operation using recursion
    Complexity O(log N)
    '''
    def search(self,key):
        return self.re_search(self.root,key)
    def re_search(self,root,key):
        if root == None:
            return False
        if root.data == key:
            return True
        if key < root.data:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)
    # minimal and maximum
    def minimal(self,root):
        current = root
        while current.left != None:
            current = current.left
        return current
    def maximum(self,root):
        current = root
        while current.right != None:
            current = current.right
        return current

    def successor(self,root,node):
        if node.right != None:
            return self.minimal(node.right)
        
        p = node.parent
        while p != None and node == p.right:
            node = p
            p = p.parent
        return p
    
    def predecessor(self,root,node):
        if node.left != None:
            return self.maximum(node.left)
        p=node.parent
        while p != None and p.left == node:
            node = p
            p=p.parent
        return p
        
    
    '''
    Insert operation using recursion
    O(logN)
    '''
    def insert(self,data):
        if self.root:
            return self.re_insert(self.root,data)
        else:
            self.root = Node(data)
            return True
    def re_insert(self,root,data):
        if root.data == data:
            return False
        if data < root.data:
            if root.left:
                return self.re_insert(root.left,data)
            else:
                root.left = Node(data)
                return True
        else:
            if root.right:
                return self.re_insert(root.right,data)
            else:
                root.right = Node(data)
                return True

    # Traversal 3 ways
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(str(root.data),end=' ')
            self.inorder(root.right)
    def preorder(self,root):
        if root:
            print(str(root.data),end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
   
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(str(root.data),end=' ')

    def delete(self,key):
        return self._deleteNode(self.root,key)
    def _deleteNode(self,root,key):
        # Base Case
        if root == None:
            return root

        # key in left sub-tree
        if key < root.data:
            root.left = self._deleteNode(root.left,key)
        
        # key in right sub-tree
        elif key > root.data:
            root.right = self._deleteNode(root.right,key)
        
        # current node to be deleted
        else:
            # 1. node has 1/0 child
            if root.left == None:
                temp = root.right
                root = None
                return temp
            elif root.right == None:
                temp = root.left
                root = None
                return temp
            
            #2.node has 2 children: get the inorder successor
            temp = self.minimal(root.right)
            root.data = temp.data

            #delete the successor
            root.right = self._deleteNode(root.right,temp.data)
        return root


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(45)
    tree.insert(24)
    tree.insert(12)
    tree.insert(41)
    tree.insert(33)
    tree.insert(42)
    tree.insert(67)
    tree.insert(64)
    tree.insert(66)
    tree.insert(99)
    print(tree.minimal(tree.root))
    print(tree.maximum(tree.root))
    print(tree.search(45))
    tree.inorder(tree.root)
    print()
    tree.preorder(tree.root)
    print()
    tree.postorder(tree.root)
    print()

    succ = tree.successor(tree.root,tree.root)
    print(succ.data)
    pred = tree.predecessor(tree.root,tree.root)
    print(pred.data)

    #no child
    print("\ndelete 99")
    tree.root = tree.delete(99)
    tree.inorder(tree.root)

    #1 child
    print("\ndelete 64")
    tree.root = tree.delete(64)
    tree.inorder(tree.root)

    #2child 
    print("\ndelete 24")
    tree.root = tree.delete(24)
    tree.inorder(tree.root)

    #root
    print("\ndelete 45")
    tree.root = tree.delete(45)
    tree.inorder(tree.root)
