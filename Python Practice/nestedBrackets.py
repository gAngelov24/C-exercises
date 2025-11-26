# Validate Properly Nested Brackets : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

def areBracketsProperlyMatched(code_snippet):
    # Write your code here
    stack = []
    
    for i in range(len(code_snippet)):
        c = code_snippet[i]
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
        elif c == ')':
            if len(stack) <= 0 or stack[-1] != '(':
                return 0
            else:
                stack.pop()
        elif c == ']':
            if len(stack) <= 0 or stack[-1] != '[':
                return 0
            else:
                stack.pop()
        elif c == '}':
            if len(stack) <= 0 or stack[-1] != '{':
                return 0
            else:
                stack.pop()
            
    if len(stack) == 0:
        return 1
    else:
        return 0
                

if __name__ == '__main__':
    code_snippet = input()

    result = areBracketsProperlyMatched(code_snippet)

    print(int(result))
