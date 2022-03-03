"""
Doubly Linked List(DDL) contains an extra pointer: previous pointer
Advantages: 1. DLL can be traversed in both forward and backward direction
            2. delete operation is more efficient(if pointer to the node deleted is given)
            3. we can quickly insert a new node before a given node
"""
import gc #garbage collection

#Node of a Doubly Linked List
class Node:
    # Constructor to create a new node
    def __init__(self, next=None, prev = None, data= None):
        self.next = next    #reference to next node 
        self.prev = prev    #reference to previous node
        self.data = data

# Class to create a DLL
class DoublyLinkedList:
    #Constructor for empty DLL
    def __init__(self):
        self.head = None
    
    # Adding a node at the front of the list
    def push(self,new_data):

        #1. allocate the node
        #2. put in the data
        new_node = Node(data=new_data)

        #3. new node next and prev pointer
        new_node.next=self.head
        new_node.prev=None

        #4.original head node pointer changing
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    # Adding a node after a given node
    # Given a node as prev_node,insert
    def insertAfter(self,prev_node,new_data):
        #1. check the given prev_node is Null
        if prev_node is None:
            print("This node is not exist")
            return

        #2. allocate node
        #3. put data
        new_node = Node(data=new_data)

        #4. change new node 2 pointer
        new_node.next = prev_node.next
        new_node.prev = prev_node
        #5. change prev node next pointer
        prev_node.next = new_node
        #6. change next node prev pointer
        if new_node.next is not None:
            new_node.next.prev = new_node

    # Adding a node at the end: append()
    def append(self,new_data):
        #1. allocate node
        #2. put data
        new_node = Node(data=new_data)

        #3. check linked list is empty
        #   Else traverse till the last node
        last = self.head
        if self.head is None:
            new_node.next = None
            new_data.prev = None
            self.head = new_node
            return
        
        while (last.next != None):
            last = last.next

        # 4. change last node pointer
        last.next = new_node

        # 5. change new node pointer
        new_node.prev = last
        new_node.next = None
    
    def deleteNode(self,deleNode):
        #Base case: linkedList is empty 
        #           deleNode is empty
        if self.head is None or deleNode is None:
            return
        
        # If deleted node is head node
        if deleNode == self.head:
            self.head = self.head.next

        # If deleted node is not last node
        if deleNode.next is not None:
            deleNode.next.prev = deleNode.prev
        
        # If deleted node is not first node
        if deleNode.prev is not None:
            deleNode.prev.next=deleNode.next
        gc.collect() #free the memory occupied by dele

    def deleNodePos(self,n):
        # if linked list in none
        # or n is none
        if self.head == None or n<=0:
            return

        current = self.head
        i = 0

        while(current != None and i < n):
            current = current.next
            i+=1

        if(current == None):
            return
        self.deleteNode(current)


        # traverse to the node at position n


    def showList(self,node):
        print("\nTraversal in forward direction")
        while node:
            print("{}".format(node.data))
            last = node
            node = node.next

        print("\nTraversal in reversal direction")
        while last:
            print("{}".format(last.data))
            last=last.prev

if __name__ == "__main__":
    list = DoublyLinkedList()
    list.push(1)
    print(list.head.data)
    list.insertAfter(list.head,2)
    print(list.head.next.data)
    list.append(5)
    print(list.head.next.next.data)
    list.showList(list.head)
    list.deleteNode(list.head)
    list.showList(list.head)
    list.push(2)
    list.push(5)
    list.push(8)
    list.push(10)
    list.showList(list.head)
    list.deleNodePos(2)
    list.showList(list.head)

    
