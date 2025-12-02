# Queue from Two Stacks : HackerRank

import math
import os
import random
import re
import sys


# Complete the 'processRequestQueueOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY operations
#  2. INTEGER_ARRAY values
#

def processRequestQueueOperations(operations, values):
    inStack = []
    outStack = []
    output = []
    i = 0
    size = 0
    for op in operations:
        if op == 'enqueue':
            #print("enqueue: ")
            inStack.append(values[i])
            size += 1
            # print("inStack =", inStack, "- outStack =", outStack)
            # print("output =", output)
        elif op == 'dequeue':
            #print("dequeue: ")
            if len(outStack) == 0:
                for j in range(len(inStack)-1, -1, -1):
                    outStack.append(inStack[j])
                    inStack.pop()
                output.append(outStack[-1])
                outStack.pop()
                size-=1
            else:
                output.append(outStack[-1])
                outStack.pop()
                size-=1
            # print("inStack =", inStack, "- outStack =", outStack)
            # print("output =", output)
        elif op == 'peek':
            #print("peek: ")
            if len(outStack) == 0:
                for j in range(len(inStack)-1, -1, -1):
                    outStack.append(inStack[j])
                    inStack.pop()
                output.append(outStack[-1])
            else:
                output.append(outStack[-1])
            # print("inStack =", inStack, "- outStack =", outStack)
            # print("output =", output)
        else:
            #print("size: ")
            output.append(size)
        i+=1
            
    return output
            
    

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    values_count = int(input().strip())

    values = []

    for _ in range(values_count):
        values_item = int(input().strip())
        values.append(values_item)

    result = processRequestQueueOperations(operations, values)

    print('\n'.join(map(str, result)))
