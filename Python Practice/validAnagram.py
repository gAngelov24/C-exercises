# Check Valid Anagram : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'isAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def isAnagram(s, t):
    # Write your code here
    if len(s) != len(t):
        return 0
    sHM = {}
    freqM = [] # [[s,1], [i, 1], [char, count]]
    count = 0
    for i in range(len(s)):
        curr = s[i]
        if curr not in sHM:
            sHM[curr] = count
            count+=1
            freqM.append([curr, 0])
            # print("sHM =", sHM, "- freqM =", freqM)
        if s[i] in sHM:
            idx = sHM[curr]
            freqM[idx][1]+=1
    # print("sHM =", sHM, "- freqM =", freqM)
    
    for i in range(len(t)):
        curr = t[i]
        if curr in sHM:
            idx = sHM[curr]
            freqM[idx][1]-=1
            if freqM[idx][1] < 0:
                return 0
        else:
            return 0
    for i in range(len(freqM)):
        if freqM[i][1] != 0:
            return 0
    return 1

if __name__ == '__main__':
    s = input()

    t = input()

    result = isAnagram(s, t)

    print(result)
