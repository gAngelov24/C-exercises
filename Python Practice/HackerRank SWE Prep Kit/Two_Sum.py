# Two Sum : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'findTaskPairForSlot' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY taskDurations
#  2. INTEGER slotLength
#

def findTaskPairForSlot(taskDurations, slotLength):
    # Write your code here
    output = [-1, -1]
    seen = {} # hash map
    for i in range(len(taskDurations)):
        needed = abs(slotLength - taskDurations[i])
        if needed in seen:
            return [seen[needed], i]
        seen[taskDurations[i]] = i
        
    return output

if __name__ == '__main__':
    taskDurations_count = int(input().strip())

    taskDurations = []

    for _ in range(taskDurations_count):
        taskDurations_item = int(input().strip())
        taskDurations.append(taskDurations_item)

    slotLength = int(input().strip())

    result = findTaskPairForSlot(taskDurations, slotLength)

    print('\n'.join(map(str, result)))
