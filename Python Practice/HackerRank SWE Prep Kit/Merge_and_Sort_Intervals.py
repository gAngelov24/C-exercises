# Merge and Sort Intervals : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    # Write your code here
    #print(intervals)
    if len(intervals) <= 0:
        return []
    #print(intervals)
    sInter = sorted(intervals)
    # output = [intervals[0]]
    # print(output)
    #print(sInter)
    #print(len(sInter))
    prevEnd = sInter[0][1]
    start = -1
    i = 1
    while i < len(sInter):
        start = sInter[i][0]
        # print(sInter)
        if start <= prevEnd:
            # print("if")
            # print("i =", i, "- Start:", start, "- prevEnd: ", prevEnd)
            if prevEnd <= sInter[i][1]:
                sInter[i-1][1] = sInter[i][1]
                prevEnd = sInter[i][1]
            sInter.remove(sInter[i])
            continue
        else:
            # print("else")
            # print("i =", i, "- Start:", start, "- prevEnd: ", prevEnd)
            prevEnd = sInter[i][1]
            i+=1
            
    return sInter
            
            
        

if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
