#10. Queue Data Structure Class : w3resource
# Write a Python program to create a class representing a queue data structure. 
# Include methods for enqueueing and dequeueing elements.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        # self.data = None
        self.tail = None
    def enqueue(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    def dequeue(self):
        if self.head is None or self.tail is None:
            return None
        else:
            curr = self.tail
            tmp = curr.data
            self.tail = curr.prev
            return tmp
    def peak(self):
        if self.head is None:
            return None
        else:
            return self.tail.data
    def printQueue(self):
        if self.head is None or self.tail is None:
            print("[]")
            return
        output = "["
        curr = self.tail
        while curr is not None:
            if curr.prev is None: 
                output += (str(curr.data) + "]")
            else:
                output += (str(curr.data) + ", ")
            curr = curr.prev
        print(output)
        
q = Queue()

for i in range(5):
    print("Enqueue:", i)
    q.enqueue(i)
    q.printQueue()

print("Dequeue:", q.dequeue(), "- ANS =",0)
q.printQueue()
print("Dequeue:", q.dequeue(), "- ANS =",1)
q.printQueue()
print("Dequeue:", q.dequeue(), "- ANS =",2)
q.printQueue()
print("Dequeue:", q.dequeue(), "- ANS =",3)
q.printQueue()
print("Dequeue:", q.dequeue(), "- ANS =",4)
q.printQueue()
print("Dequeue:", q.dequeue(), "- ANS = None")



