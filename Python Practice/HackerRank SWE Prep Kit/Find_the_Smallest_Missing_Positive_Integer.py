# Find the Smallest Missing Positive Integer : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def findSmallestMissingPositive(orderNumbers):
    # Write your code here
    # Goal is to find the smallest positve integer not in the array
    # orderedNumbers = [3, 4, -1, 1] -> return 2
    # orderedNumbers = [] -> return 1
    # orderedNumbers = [1] -> return 2
    # CONSTANTS
    L = len(orderNumbers)
    
    # Step 1: Place intergers into correct idx
    i = 0
    while i < L:
        val = orderNumbers[i] # current value
        correct_idx = val - 1
        
        # check if we can place val into correct_idx
        # 1 <= val <= L AND orderNumbers[correct_idx] != val
        if 1 <= val <= L and orderNumbers[correct_idx] != val:
            orderNumbers[i] = orderNumbers[correct_idx]
            orderNumbers[correct_idx] = val
        else:
            i+=1
    
    # Step 2: Loop through arr and return either i + 1
    for i in range(L):
        if orderNumbers[i] != (i+1):
            return i+1
    
    # Step 3: if arr is "full" return L + 1
    return L+1

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
