# Next Greater Element with Position Offset : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'findNextGreaterElementsWithDistance' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY readings as parameter.
#

def findNextGreaterElementsWithDistance(readings):
    results = []
    for i in range(len(readings)):
        cur = readings[i]
        pair = []
        for j in range(i, len(readings)):
            if cur < readings[j]:
                pair.append(readings[j])
                pair.append(j-i)
                #print("i =", i, "- j =", j, "- pair =", pair)
                break
        if len(pair) == 0:
            pair.append(-1)
            pair.append(-1)
        results.append(pair)
        #print("results at i =", i, "- ",results)
    
    return results

if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = int(input().strip())
        readings.append(readings_item)

    result = findNextGreaterElementsWithDistance(readings)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
