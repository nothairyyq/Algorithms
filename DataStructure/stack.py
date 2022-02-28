

class Stack:
    def __init__(self):
        self.stack=[]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self,item):
        self.stack.append(item)
        print("Pushed item: " + item)
    
    def pop(self):
        if(self.isEmpty()):
            return "Underflow"
        return self.stack.pop()
    
    def display(self):
        print(self.stack)

if __name__ == "__main__":
    stack=Stack()
    print(stack.pop())
    stack.push(str(1))
    stack.push(str(2))
    stack.push(str(3))
    stack.push(str(4))
    stack.display()
    stack.pop()
    stack.display()
