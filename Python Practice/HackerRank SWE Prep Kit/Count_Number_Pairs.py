# Count Number Pairs : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'countAffordablePairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER budget
#

def countAffordablePairs(prices, budget):
    # Write your code here
    n = len(prices)
    #print(prices, budget)
    count = 0
    if n <= 1:
        return 0
    for i in range(n):
        if prices[i] > budget:
            break
        for j in range(i+1, n):
            if prices[j] > budget:
                break
            if prices[i] + prices[j] <= budget:
                #print("Prices[",i,"] =", prices[i], ", Prices[",j,"] =", prices[j], " | ", prices[i], "+", prices[j], "=", prices[i] + prices[j])
                count+=1
    return count

if __name__ == '__main__':
    prices_count = int(input().strip())

    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    budget = int(input().strip())

    result = countAffordablePairs(prices, budget)

    print(result)
