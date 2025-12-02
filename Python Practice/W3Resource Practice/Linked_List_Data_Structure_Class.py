# 7. Linked List Data Structure Class : w3resource
# Write a Python program to create a class representing a linked list data structure. 
# Include methods for displaying linked list data, inserting and deleting nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.next = None
    def insert(self, node_data):
        node = Node(node_data)
        if self.head is None:
            self.head = node
        else:
            prev = None
            curr = self.head
            while curr is not None:
                prev = curr
                curr = curr.next
            prev.next = node
    def deleteIdx(self, idx):
        i = 0
        prev = None
        curr = self.head
        if idx == 0:
            tmp = curr.data
            self.head = curr.next
            return tmp
        while i < idx:
            prev = curr
            curr = curr.next
            i+=1
        prev.next = curr.next
        return curr
    def delete(self, num):
        if self.head is None:
            return None
        prev = None
        curr = self.head
        while curr is not None:
            if curr.data == num and prev is None:
                self.head = curr.next
                return curr.data
            elif curr.data != num:
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                return curr.data
    def printSLL(self):
        curr = self.head
        output = ""
        while curr is not None:
            output += (str(curr.data) + " -> ")
            curr = curr.next
        output += "None"
        print(output)

sll = SinglyLinkedList()

for i in range(10):
    print("Inserting:", i)
    sll.insert(i)
    sll.printSLL()

print("Delete head using deleteIdx")
sll.deleteIdx(0)
sll.printSLL()

print("Delete head using delete")
sll.delete(1)
sll.printSLL()

print("Delete 5")
sll.delete(5)
sll.printSLL()

print("Delete tail using deleteIdx")
sll.deleteIdx(6)
sll.printSLL()

print("Delete head using delete")
sll.delete(8)
sll.printSLL()