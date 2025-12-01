# Custom Fibonacci Sequence : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'getAutoSaveInterval' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER n as parameter.
#

def getAutoSaveInterval(n):
    # Write your code here
    # fib(3) = fib(2) + fib(1) = fib(1)
    # def fib(n):
    #     if n == 1:
    #         return 2
    #     elif n == 0:
    #         return 1
    #     else:
    #         return fib(n-1) + fib(n-2)
    # return fib(n)
    if n == 0:
        return 1
    if n == 1:
        return 2
    intervals = [1, 2]
    for i in range(2, n+1):
        intervals.append(intervals[i-1]+intervals[i-2])
    #print(intervals)
    return intervals[len(intervals)-1]
        

if __name__ == '__main__':
    n = int(input().strip())

    result = getAutoSaveInterval(n)

    print(result)
