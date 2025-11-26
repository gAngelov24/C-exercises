# Count Elements Greater Than Previous Average : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    # Write your code here
    # input = {4, 100, 200, 150, 300}
    # responceTimes = {100, 200, 150, 300}
    if len(responseTimes) < 2: # if responseTimes is empty return 0
        return 0
    count = 0 # init count
    total = responseTimes[0] # init a running sum
    #print("init total = ", total)
    ave = responseTimes[0]
    #print("init ave = ", ave) # should be equal to init total
    for i in range(1, len(responseTimes)):
        #print(i, " ", responseTimes[i])
        ave = total/(i)
        #print("average = ", ave)
        if responseTimes[i] > ave:
            count+=1
            #print("count incremented")
        total += responseTimes[i]
        #print("total = ", total)
        
    #print(count)
    return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
