# Pivoted Search : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'searchRotatedTimestamps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def searchRotatedTimestamps(nums, target):
    # Write your code here
    if len(nums) <= 0:
        return -1
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    nums = sorted(nums)
    left = 0
    right = len(nums) - 1
    mid = (left+right)//2
    #print(nums)
    while True:
        # print("left =", left, "- right =", right, "- mid =", mid)
        # print("nums[mid] =", nums[mid])
        if left > right:
            return -1
        if nums[mid] == target:
            return hashmap[nums[mid]]
        elif nums[mid] > target:
            right = mid-1
            mid = (left+right)//2
        else:
            left = mid+1
            mid = (left+right)//2
    
            

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = searchRotatedTimestamps(nums, target)

    print(result)
