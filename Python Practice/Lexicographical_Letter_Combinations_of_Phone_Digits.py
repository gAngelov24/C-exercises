# Lexicographical Letter Combinations of Phone Digits : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'minTasksToCancelForNoConflict' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING digits as parameter.
#

def minTasksToCancelForNoConflict(digits):
    # Write your code here
    ldig = list(digits)
    for i in range(len(ldig)):
        ldig[i] = int(ldig[i])
    cur = 0
    numMap = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    output = []
    #print(ldig)
    # input 203
    # s = a
    
    def helper(ldig, s, curr):
        if len(s) >= len(ldig) or curr >= len(ldig):
            output.append(s)
            return
        else:
            #print("ELSE: curr =", curr)
            for i in range(len(numMap[ldig[curr]])):
                #print("FOR: curr=", curr)
                curChar = numMap[ldig[curr]][i]
                news = s + curChar
                nextCur = curr+1
                helper(ldig, news, nextCur)
    helper(ldig, '', cur)
    return output

if __name__ == '__main__':
    digits = input()

    result = minTasksToCancelForNoConflict(digits)

    print('\n'.join(result))
