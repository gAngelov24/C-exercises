# Task Scheduler with Cooldown and Multiple Machines : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'calculateMinimumTimeUnits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY tasks
#  2. INTEGER m
#  3. INTEGER k
#

def calculateMinimumTimeUnits(tasks, m, k):
    n = len(tasks)
    if n == 0:
        return 0
    
    # Count frequency of each task type
    freq = {}
    for t in tasks:
        freq[t] = freq.get(t, 0) + 1
    
    # If there is no cooldown, just pack tasks as tightly as possible
    if k == 0:
        return (n + m - 1) // m
    
    # Lower bound 1: Total capacity constraint
    # In T time units with m machines, we can do at most m*T tasks
    T_capacity = (n + m - 1) // m
    
    # Lower bound 2: Cooldown constraint
    # For each task type, if we optimally distribute across m machines,
    # each machine gets ceil(count/m) tasks of that type.
    # With cooldown k, we need (k+1) time units between consecutive tasks of same type.
    # So for q tasks of one type on one machine, we need: (q-1)*(k+1) + 1 time units
    
    T_cooldown = 0
    for cnt in freq.values():
        # How many of this task type per machine (ceiling division)
        tasks_per_machine = (cnt + m - 1) // m
        
        # Time needed for this task type with optimal distribution
        # If a machine has q tasks of this type, it needs (q-1)*(k+1) + 1 time
        time_for_this_type = (tasks_per_machine - 1) * (k + 1) + 1
        
        T_cooldown = max(T_cooldown, time_for_this_type)
    
    # The answer must satisfy both constraints
    return max(T_capacity, T_cooldown)

if __name__ == '__main__':
    tasks_count = int(input().strip())

    tasks = []

    for _ in range(tasks_count):
        tasks_item = int(input().strip())
        tasks.append(tasks_item)

    m = int(input().strip())

    k = int(input().strip())

    result = calculateMinimumTimeUnits(tasks, m, k)

    print(result)
