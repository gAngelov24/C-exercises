# Maximum Number of Non-Overlapping Intervals : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'maximizeNonOverlappingMeetings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY meetings as parameter.
#

def maximizeNonOverlappingMeetings(meetings):
    # Write your code here
    # Step 1: Sort meeting times by end time
    sM = sorted(meetings, key=lambda x: x[1])
    if len(meetings) < 1:
        return 0
    count = 0
    last_end = 0
    
    # Step 2: Select meeting and set count and last_end
    for i in range(len(sM)):
        if sM[i][0] >= last_end: # if new start time is >= last end time: count++
            count+=1
            last_end = sM[i][1]
    return count
            
    
    

if __name__ == '__main__':
    meetings_rows = int(input().strip())
    meetings_columns = int(input().strip())

    meetings = []

    for _ in range(meetings_rows):
        meetings.append(list(map(int, input().rstrip().split())))

    result = maximizeNonOverlappingMeetings(meetings)

    print(result)
