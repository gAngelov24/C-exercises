# Max Unique Substring Length in a Session : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'maxDistinctSubstringLengthInSessions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING sessionString as parameter.
#

def maxDistinctSubstringLengthInSessions(sessionString):
    # Write your code here
    n = len(sessionString)
    if n == 0 or sessionString[0] == '*':
        return 0
    seen = {}
    maxCount = 0
    count = 0
    i = 0
    while i < n:
        if sessionString[i] not in seen and sessionString[i] != '*':
            seen[sessionString[i]] = i
            count+=1
        elif sessionString[i] == '*':
            if count > maxCount:
                maxCount = count
            seen.clear()
            count = 0
        else:
            #print(seen)
            if count > maxCount:
                maxCount = count
            seen.clear()
            seen[sessionString[i]] = i
            count = 1
        #print("Count =", count, "Curr Char:", sessionString[i])
        i+=1
    if count > maxCount:
        return count
    return maxCount
    

if __name__ == '__main__':
    sessionString = input()

    result = maxDistinctSubstringLengthInSessions(sessionString)

    print(result)
