#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
# Solution for https://www.hackerrank.com/challenges/picking-numbers/problem

def pickingNumbers(input_list):
    i_count_list = [0] * 100
    
    for i in input_list:
        i_count_list[i]+= 1

    max_len = 0
    for first,second in zip(range(99),range(1,100)):
        if i_count_list[first] or i_count_list[second]:
            len_set = i_count_list[first]+ i_count_list[second]
            if len_set > max_len:
                max_len = len_set
    
    return max_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    fptr.write(str(result) + '\n')
    fptr.close()
