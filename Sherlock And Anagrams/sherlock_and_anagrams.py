#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    
    n = len(s)
    min_sub = 1
    count = 0
    count = helper(min_sub, s, count, n)
    
    return count

def helper(sub_len, s, count, n):
    
    #base case
    #if the lenght of the substring is equal the lenght of the string
    #there are not more substring, therefore return count
    if (sub_len == len(s)):
        return count
    
    #we loop accordingly with the size of the string and the size of the substring
    #(eg,. if n = 4 and sub_len is 1, we just need to check three time)
    #(eg,. if n = 4 and sub_len is 2, we just need to check two times)
    for i in range(n - sub_len):
        
        #get the first or 'left' substring in the string
        #based on its len, always adding to i so it keeps
        #shifting right as it loops thourgh
        left_sub = s[i:i+sub_len]
        
        #sort substring
        left_sub = ''.join(sorted(left_sub))
        
        #the right substring always strats one position after the 'left' substring
        #we loop again base on the size of the string and the size of the substring
        #(eg,. if n = 4 and sub_len is 1, we just need to check three time)
        #(eg,. if n = 4 and sub_len is 2, we just need to check two times)
        #we add one to it because we're starting at one position after the left_sub
        #note: if s[start:end] where end falls out of bounds
        #it just returns whatever is after start, python won't through 
        #an out of bound error
        for j in range(i+1, n - sub_len +1):
            
            #right substring always start one index after the left_sub index
            #we get it based on its len, always adding to j so it keeps
            #shifting right as it loops thourgh
            right_sub = s[j:j+sub_len]
            
            #sort substring
            right_sub = ''.join(sorted(right_sub))
            
            #if they're equal, they're anagrams of each other
            if left_sub == right_sub:
                
                count +=1
    
    #recursive call
    return helper(sub_len + 1, s, count, n)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
