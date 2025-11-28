# Generate Valid Angle Bracket Sequences : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'generateAngleBracketSequences' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER n as parameter.
#

def generateAngleBracketSequences(n):
    # Write your code here
    results = [] 

    def backtrack(curr, open_count, close_count):
        if len(curr) == 2 * n:
            results.append(curr)
            return
        if open_count < n:
            backtrack(curr + "<", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(curr + ">", open_count, close_count + 1)

    backtrack("", 0, 0)
    return results
            

if __name__ == '__main__':
    n = int(input().strip())

    result = generateAngleBracketSequences(n)

    print('\n'.join(result))
