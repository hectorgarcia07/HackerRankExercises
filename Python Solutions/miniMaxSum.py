#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    result = sum(arr)
    resultOfSums = []
    
    for num in arr:
        resultOfSums.append(result - num)
    resultOfSums.sort()
    print(f'{resultOfSums[0]} {resultOfSums[4]}')
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)