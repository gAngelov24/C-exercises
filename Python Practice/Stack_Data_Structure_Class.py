# 6. Stack Data Structure Class : w3resource
# Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.stack_ = []
    def push(self, data):
        good = 0
        self.stack_.append(data)
        if self.stack_[-1] == data:
            good = 1
        return good
    def pop(self):
        top = self.stack_[-1]
        self.stack_.remove(top)
        return top
    def peak(self):
        return self.stack_[-1]
    def get(self):
        return self.stack_
    
stack = Stack()

for i in range(10):
    print("push(",i,")")
    stack.push(i)

print("Stack =", stack.get())

print("peak()", stack.peak(), "- ANS = 9")
print("pop()", stack.pop(), "- ANS = 9")
print("peak()", stack.peak(), "- ANS = 8")
print("pop()", stack.pop(), "- ANS = 8")
print("pop()", stack.pop(), "- ANS = 7")
print("pop()", stack.pop(), "- ANS = 6")
print("pop()", stack.pop(), "- ANS = 5")
print("peak()", stack.peak(), "- ANS = 4")