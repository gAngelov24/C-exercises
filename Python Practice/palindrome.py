# Check Palindrome by Filtering Non-Letters : HackerRank

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    # Write your code here
    # code = abc123cba
    # Push(a), push(b), push(c), ignore(123), pop(c), pop(b), pop(a), if stack is empty return 1, else return 0
    stack = []
    codeNew = []
    if len(code) == 1:
        return 1
    if len(code) == 0:
        return 0
    
    for i in range(len(code)): # push only proper values to stack as lowercase
        if code[i].isalpha():
            stack.append(code[i].lower())
            codeNew.insert(0, code[i].lower())
            
    # print("Stack: ", stack)
    # print("codeNew: ", codeNew)
    for i in range(len(codeNew)-1, -1, -1): # traverse code 
        if codeNew[i] == stack[-1]:
            stack.pop()
            #print("Stack at i = ", i, ": ", stack)
        
        
        
        # if len(stack) == 0:
        #     stack.append(code[i].lower())
        #     #print("Stack at i = ", i, ": ", stack)
        # elif code[i].lower() != stack[-1] and code[i].isalpha():
        #     stack.append(code[i].lower())
        #     #print("Stack at i = ", i, ": ", stack)
        # elif code[i].lower() == stack[-1]:
        #     stack.pop()
        #     #print("Stack at i = ", i, ": ", stack)
        # else:
        #     continue
    ret = 0
    # print("Final Stack: ", stack)
    if len(stack) == 0:
        ret = 1
    return ret
    
            
            
    
    
    

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
