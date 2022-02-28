
class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue)==0

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if(self.isEmpty()):
            return "underflow"
        return self.queue.pop()

    def display(self):
        print(self.queue)

if __name__ == "__main__":
    queue=Queue()
    print(queue.dequeue())
    queue.enqueue(str(1))
    queue.enqueue(str(2))
    queue.enqueue(str(3))
    queue.enqueue(str(4))
    queue.display()
    queue.dequeue()
    queue.display()

    