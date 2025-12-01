# Find Peak Element in Bitonic Array : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'findPeakIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY counts as parameter.
#

def findPeakIndex(counts):
    # Write your code here
    # do binary search with a catch
    # split down middle, if counts[mid-1] <= counts[mid] and counts[mid+1] <= counts[mid]
    n = len(counts)
    if n <= 1:
        if n == 1:
            return 0
        elif n <= 0:
            return -1
    
    left = 0
    right = n - 1
    mid = (left+right)//2
    maxIdx = -1
    
    while True:
        if left > right:
            return maxIdx
        elif counts[mid-1] <= counts[mid] and counts[mid+1] <= counts[mid]:
            return mid
        elif counts[mid-1] <= counts[mid] and counts[mid+1] >= counts[mid]:
            left = mid+1
            mid = (left+right)//2
        else:
            right = mid-1
            mid = (left+right)//2
            
    
    
if __name__ == '__main__':
    counts_count = int(input().strip())

    counts = []

    for _ in range(counts_count):
        counts_item = int(input().strip())
        counts.append(counts_item)

    result = findPeakIndex(counts)

    print(result)
