# Remove Elements Within K Distance : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'debounceTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY timestamps
#  2. INTEGER K
#

def debounceTimestamps(timestamps, K):
    # Write your code here
    i = 1
    while i < len(timestamps):
        curr = timestamps[i]
        prev = timestamps[i-1]
        if curr - prev >= K:
            i+=1
            continue
        timestamps.remove(curr)
    return len(timestamps)

if __name__ == '__main__':
    timestamps_count = int(input().strip())

    timestamps = []

    for _ in range(timestamps_count):
        timestamps_item = int(input().strip())
        timestamps.append(timestamps_item)

    K = int(input().strip())

    result = debounceTimestamps(timestamps, K)

    print(result)
