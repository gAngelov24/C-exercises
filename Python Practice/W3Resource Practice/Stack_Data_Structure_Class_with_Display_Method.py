# 9. Stack Data Structure Class with Display Method : w3resource

# Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing, popping and displaying elements.

class Stack:
    def __init__(self):
        self.stack_ = []
    def push(self, data):
        self.stack_.append(data)
    def pop(self):
        if len(self.stack_) == 0:
          return None
        tmp = self.stack_[-1]
        self.stack_.pop()
        return tmp
    def peek(self):
        if len(self.stack_) == 0:
            return None 
        return self.stack_[-1]
    def printStack(self):
        if len(self.stack_) == 0:
            print("None")
        for i in range(len(self.stack_)-1, -1, -1):
            print(self.stack_[i])
            
stack = Stack()
stackLC = []
print("push: [0, 1, 2, 3, 5, 6]")

stackLC = [x for x in range(7)]
#print(stackLC)

for i in range(6):
    stack.push(i)
    
stack.printStack()
print("pop =", stack.pop(), "- new stack =")
stack.printStack()
print("pop =", stack.pop(), "- new stack =")
stack.printStack()
print("pop =", stack.pop(), "- new stack =")
stack.printStack()
print("pop =", stack.pop(), "- new stack =")
stack.printStack()
print("pop =", stack.pop(), "- new stack =")
stack.printStack()
print("pop =", stack.pop(), "- new stack =")
stack.printStack()