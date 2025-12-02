# Min-Tracking Stack Implementation : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'processCouponStackOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def processCouponStackOperations(operations):
    # Write your code here
    stack = [] # stack
    minStack = [] # tracks order of mins 
    output = [] # output
    for i in range(len(operations)):
        if operations[i] == 'pop':
            # check if stack is empty
            if len(stack) == 0:
                return -1
            # if not empty pop top item
            if stack[-1] == minStack[0]:
                minStack.remove(stack[-1])
            stack.pop()
            # print("Stack: ", stack)
            # print("min Array: ", minStack)
        elif operations[i] == 'top':
            # check if stack is empty
            if len(stack) == 0:
                output.append(-1)
            else:
                # if not empty ret [-1]
                output.append(stack[-1])
        elif operations[i] == 'getMin':
            # check if stack is empty
            if len(stack) == 0:
                output.append(-1)
            # if not empty ret min
            output.append(minStack[0])
        else:
            inp = int(operations[i][5:])
            stack.append(inp)
            if len(minStack) == 0:
                minStack.append(inp)
            else:
                for i in range(len(minStack)):
                    if inp < minStack[i]:
                        minStack.insert(i, inp)
                        break
            # print("Stack: ", stack)
            # print("min Array: ", minStack)            
            
    return output
            

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    result = processCouponStackOperations(operations)

    print('\n'.join(map(str, result)))
