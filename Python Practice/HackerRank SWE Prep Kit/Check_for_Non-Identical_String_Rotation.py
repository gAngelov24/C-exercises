# Check for Non-Identical String Rotation : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'isNonTrivialRotation' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def isNonTrivialRotation(s1, s2):
    # Write your code here
    if s1 == s2:
        return 0
    elif len(s1) != len(s2):
        return 0
    # s1 = abcde
    # s2 = edcba
    s1Arr = list(s1)
    s2Arr = list(s2)
    i = 0
    #print("s1Arr: ", s1Arr)
    while i < len(s1Arr):
        tmp = s2Arr[-1]
        s2Arr.insert(0, tmp)
        s2Arr.pop()
        #print("s2Arr: ", s2Arr)
        if s2Arr == s1Arr:
            return True
        i+=1
    return False
    
    
    
    

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = isNonTrivialRotation(s1, s2)

    print(int(result))
