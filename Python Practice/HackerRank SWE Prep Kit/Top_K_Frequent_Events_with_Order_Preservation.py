# Top K Frequent Events with Order Preservation : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'getTopKFrequentEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY events
#  2. INTEGER k
#

def getTopKFrequentEvents(events, k):
    #print("Events =", events, "- k =", k)
    if events is None or len(events) <= 0 or k == 0:
        return []
    freq = {}
    first_occurance = {}
    
    for i in range(len(events)):
        if events[i] not in freq:
            freq[events[i]] = 0
            first_occurance[events[i]] = i
        freq[events[i]] += 1
    
    unique_events = list(freq.keys())
    
    # Sort by frequency (descending), then by first occurrence (ascending)
    unique_events.sort(key=lambda x: (-freq[x], first_occurance[x]))
    
    # Return top k
    return unique_events[:k]
        
        
        

if __name__ == '__main__':
    events_count = int(input().strip())

    events = []

    for _ in range(events_count):
        events_item = int(input().strip())
        events.append(events_item)

    k = int(input().strip())

    result = getTopKFrequentEvents(events, k)

    print('\n'.join(map(str, result)))
