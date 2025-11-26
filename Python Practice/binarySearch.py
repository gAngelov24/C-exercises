# Target Index Search : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'binarySearch' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def binarySearch(nums, target):
    # Write your code here
    #print(nums)
    if len(nums) <= 0:
        return -1
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    # nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    low = 0
    high = len(nums)-1
    mid = (low + high) // 2
    while (low < high):
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            low = mid + 1
            mid = (low+high)//2
        else:
            high = mid - 1
            mid = (low+high)//2
    #print("mid: ", mid, ", nums[mid] = ", nums[mid])
    if nums[mid] == target:
        return mid
    return -1

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = binarySearch(nums, target)

    print(result)
