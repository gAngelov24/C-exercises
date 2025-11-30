# Longest Arithmetic Subsequence with Given Difference : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'findLongestArithmeticProgression' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def findLongestArithmeticProgression(arr, k):
    # Write your code here
    if len(arr) < 1:
        return 0
    hashmap = {} # arr hashmap
    minV = arr[0]
    headsM = {} # head stored in hashmap
    heads = []
    for i in range(len(arr)): # init hashmap for constant lookup time
        hashmap[arr[i]] = i
        if arr[i] < minV:
            minV = arr[i]
    for i in range(len(arr)):
        # is there a value which is arr[i] - k, if not [i] is a head
        if (arr[i] - k) in hashmap:
            continue
        else:
            if arr[i] - k in headsM:
                continue
            else:
                headsM[arr[i]] = i
                heads.append(arr[i])
    
    count = 1
    maxC = 1 # max count
    i = 0
    notEnd = True
    arr.remove(minV)
    #print(hashmap)
    #print(heads)
    #print("minV =", minV)
    while i < len(heads):
        start = heads[i]
        #print(start)
        while notEnd:
            need = start + k
            #print("need =", need)
            if need in hashmap:
                count+=1
                start+=k
            else:
                notEnd = False
        #print(count)
        if count > maxC:
            maxC = count
        count = 1
        notEnd = True
        i+=1
    return maxC
        
    

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    result = findLongestArithmeticProgression(arr, k)

    print(result)
